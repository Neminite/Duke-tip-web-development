
import webapp2
import os 
import jinja2
from google.appengine.ext import db

# always copy these 2 lines below
template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir)
								,autoescape = True)
class Handler(webapp2.RequestHandler):
	def write(self,*a,**kw):
		self.response.out.write(*a,**kw)

	def render_str(self,template,**params):   
		t = jinja_env.get_template(template)
		return t.render(params)
	
	def render(self,template,**kw):
		self.write(self.render_str(template,**kw))

class Forum(db.Model):
	name = db.StringProperty(required = True)
	title = db.StringProperty(required = True)
	body = db.StringProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)
	
class MainHandler(Handler):
    def get(self):
        self.render('Home.html')

class FifaHandler(Handler):
    def get(self):
        self.render('Fifa.html')

class LeagueHandler(Handler):
    def get(self):
        self.render('League.html')

class DestinyHandler(Handler):
    def get(self):
        self.render('Destiny.html')

class OverwatchHandler(Handler):
    def get(self):
        self.render('Overwatch.html')

class NBAHandler(Handler):
    def get(self):
        self.render('NBA.html')

class ForumHandler(Handler):
	def render_front(self,title = "",name ="",error = "", body = ""):
		posts = db.GqlQuery("select * from Forum order by created desc")

		self.render('Forum.html',title = title, name = name,error = error,body = body, posts = posts)

	def get(self):
		self.render_front()

	def post(self):
		title =  self.request.get('title')
		name = self.request.get('name')
		body = self.request.get('body')

		if title and name and body:
			 a = Forum(title = title, name = name, body = body)
			 a.put()
			 self.render_front()
		else:
			error = "Please type in a name, a topic, and a body."
			self.render_front(title = title, name = name ,error = error, body = body)

class TipHandler(Handler):
    def get(self):
        self.render('Tip.html')

class AboutHandler(Handler):
    def get(self):
        self.render('About.html')

class ContactHandler(Handler):
    def get(self):
        self.render('Contact.html')




app = webapp2.WSGIApplication([
    ('/', MainHandler), ('/fifa', FifaHandler), ('/league', LeagueHandler), ('/destiny', DestinyHandler), ('/overwatch', OverwatchHandler), ('/nba', NBAHandler), ('/forum', ForumHandler), ('/tip', TipHandler), ('/about', AboutHandler), ('/contact', ContactHandler)
], debug=True)