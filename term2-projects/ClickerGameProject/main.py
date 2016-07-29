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

	# here it takes template - that is directory name and **params taking extra parameters
	def render_str(self,template,**params):   
		t = jinja_env.get_template(template)
		return t.render(params)
	
	def render(self,template,**kw):
		self.write(self.render_str(template,**kw))
		
class Art(db.Model):
	title = db.StringProperty(required = True)
	art = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)

class MainHandler(Handler):
	def get(self):
		self.render('Game.html')
		def setCookie(self, name, value):
			self.response.set_cookie(name, value)
		def getCookie(self, name, default=""):
			if name in self.request.cookies:
				return self.request.cookies[name]
			return default

class ProjectHandler(Handler):
	def get(self):
		self.render('project.html')

class ForumHandler(Handler):

	def render_front(self,title = "", art ="",error = "", errortype = ""):
		arts = db.GqlQuery("select * from Art order by created desc")

		self.render('forum.html',title = title,art = art,error = error,errortype = errortype, arts = arts)

	def get(self):
		self.render_front()

	def post(self):
		title =  self.request.get('title')
		art = self.request.get('art')

		if title and art :
			if len(art) > 300 or len(title) > 100:
				errortype = "Anti Spam > "
				error = "Message is too long."
				self.render_front(title = title , art = art ,error = error ,errortype = errortype)
			else:
					specialcolor = title
			 		a = Art(title = title, art = art)
			 		a.put()
			 		self.render_front()
		else:
			errortype = "Error > "
			error = "We need both name and message."
			self.render_front(title = title, art = art ,error = error ,errortype = errortype)


class CreatorsHandler(Handler):
	def get(self):
		self.render('creators.html')

class JokesHandler(Handler):
	def get(self):
		self.render('jokes.html')
class DukeTipHandler(Handler):
	def get(self):
		self.render('duketip.html')
app = webapp2.WSGIApplication([
	('/', ProjectHandler),('/game', MainHandler),('/forum', ForumHandler),('/creators', CreatorsHandler),
	('/jokes', JokesHandler),('/duketip', DukeTipHandler)
], debug=True)


