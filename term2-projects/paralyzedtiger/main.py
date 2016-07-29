#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os 
import webapp2
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir)
                ,autoescape = True)

from google.appengine.ext import db



class Handler(webapp2.RequestHandler):
  def write(self,*a,**kw):
    self.response.out.write(*a,**kw)
  
  def render_str(self,template,**params):   # here it takes template - that is directory name and **params taking extra parameters
    t = jinja_env.get_template(template)
    return t.render(params)
  
  def render(self,template,**kw):
    self.write(self.render_str(template,**kw))

class MainHandler(Handler):
    def get(self):
        self.render('home.html')

class gameHandler(Handler):
    def get(self):
        self.render('game.html')

class forumHandler(Handler):
    def render_front(self,title = "",art ="",error = ""):
      arts = db.GqlQuery("select * from Art order by created desc")

      self.render('forum.html',title = title,art = art,error = error,arts = arts)

    def get(self):
      self.render_front()
    def post(self):
      title =  self.request.get('title')
      art = self.request.get('art')

      if title and art:
        a = Art(title = title, art = art)
        a.put()
        self.render_front()
      else:
        error = "we need both artwork and title"
        self.render_front(title = title, art = art ,error = error)


class Art(db.Model):
  title = db.StringProperty(required = True)
  art = db.TextProperty(required = True)
  created = db.DateTimeProperty(auto_now_add = True)

class aboutusHandler(Handler):
    def get(self):
        self.render('aboutus.html')

class tigerHandler(Handler):
    def get(self):
        self.render('tiger.html')

class redirectHandler(Handler):
    def get(self):
        self.render('redirect.html')

class tigergameHandler(Handler):
    def get(self):
        self.render('tigergame.html')

class twotigerHandler(Handler):
    def get(self):
        self.render('tigertwo.html')

class dropperHandler(Handler):
    def get(self):
        self.render('dropper.html')

class memeHandler(Handler):
    def get(self):
        self.render('meme.html')

class testHandler(Handler):
    def get(self):
        self.render('test.html')

class parkourHandler(Handler):
    def get(self):
        self.render('parkourtiger.html')

class tipHandler(Handler):
    def get(self):
        self.render('dtip.html')

class shootHandler(Handler):
    def get(self):
        self.render('shooter.html')
    
app = webapp2.WSGIApplication([
    ('/', MainHandler),('/games', gameHandler),('/shooter', shootHandler),('/duketip', tipHandler),('/tigerparkour', parkourHandler),('/memes', memeHandler),('/twotiger',twotigerHandler),('/forums', forumHandler),('/test',testHandler),('/tigerdropper',dropperHandler),('/aboutus', aboutusHandler),('/savethetigers', tigerHandler),('/gameredirect',redirectHandler),('/tigergame',tigergameHandler)], debug=True)
