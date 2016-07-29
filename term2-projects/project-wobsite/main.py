import webapp2
import time
import os
import jinja2 as jinja
from hashlib import sha1
from google.appengine.ext import db

pwd = "hello"
def hash(str):
    return sha1(str).hexdigest();

#jinja boilerplate
template_dir = os.path.join(os.path.dirname(__file__), 'website')
jinja_env = jinja.Environment(loader = jinja.FileSystemLoader(template_dir), autoescape=True)
#end

def adminParse(strn):
    return (("".join(ch for ch in strn.lower() if ch in "qwertyuiopasdfghjklzxcvbnm") in ("admin", "root")) | (strn == "42"))


class Comment(db.Model):
    name = db.StringProperty(required=True)
    body = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
class Pass(db.Model):
    pwd = db.StringProperty()

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def get_data(self, name):
        return self.request.get(name)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **variables):
        self.write(self.render_str(template, **variables))
    def setCookie(self, name, value):
        self.response.set_cookie(name, value)
    def getCookie(self, name, default=""):
        if name in self.request.cookies:
            return self.request.cookies[name]
        return default

class MainHandler(Handler):
    def get(self):
        self.render("index.html")

class ChatHandler(Handler):
    def render_page(self, error="", body="", name=""):
        time.sleep(0.2)
        posts = db.GqlQuery("select * from Comment order by created desc")
        self.render("chatroom.html", posts=posts, error=error, body=body, name=name)
    def get(self):
        self.render_page()
    def post(self):
        global pwd
        body = self.get_data("body").strip()
        name = self.get_data("name").strip()
        if adminParse(name):
            if body[:(16 + len(pwd))] == "sudo say -p " + pwd + " -m ":
                post = Comment(body="\n"+body[(16 + len(pwd)):], name="Admin")
                post.put()
                self.render_page()
            elif body == "sudo nuke -p " + pwd:
                self.nuke()
                self.render_page()
#            '''elif body[:(19 + len(pwd))] == "sudo thread -p " + pwd + " -n ":
#                threads = db.GqlQuery('select * from Thread order by created desc')
#                if body[(19 + len(pwd)):] not in [td.name for td in threads]:
#                    newthread = Thread(name=body[(19 + len(pwd)):])
#                    newthread.put()
#                    self.render_page()
#                else:
#                    self.render_page(error="That thread already exists!")
#            elif body[:(19 + len(pwd))] == "sudo thread -p " + pwd + " -d ":
#                try:
#                    self.delthread(body[(19 + len(pwd)):])
#                    self.render_page()
#                except Exception as e:'''
#                    self.render_page(error="Exception: %s" % e)
            else:
                self.render_page(error="One does not simply post as admin!", body=body)
        elif body and name:
            post = Comment(body="\n"+body, name=name)
            post.put()
            self.render_page()
        else:
            self.render_page(error="A body and a name are required to make a post.", body=body, name=name)
    def nuke(self):
        posts = db.GqlQuery('select * from Comment order by created desc')
        for p in posts:
            db.delete(p)
    def delthread(self, tname):
        threads = db.GqlQuery('select * from Thread order by created desc')
        for td in threads:
            if td.name == tname:
                db.delete(td)

class GameHandler(Handler):
    def get(self):
        self.render("games.html")
class ZergHandler(Handler):
    def get(self):
        self.render("zergrush.html")
class SkyHandler(Handler):
    def get(self):
        self.render("skyisfalling.html")
class ClickerHandler(Handler):
    def get(self):
        self.render("clicker.html")

class AboutHandler(Handler):
    def get(self):
        self.render("about.html")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/chatroom.html', ChatHandler),
    ('/games.html', GameHandler),
    ('/zergrush.html', ZergHandler),
    ('/skyfalling.html', SkyHandler),
    ('/clicker.html', ClickerHandler),
    ('/about.html', AboutHandler),
], debug=True)