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
from google.appengine.ext import db
import os
import jinja2
# always copy these 2 lines below
template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir)
								,autoescape = True)



class Art(db.Model):
	title = db.StringProperty(required = True)
	art = db.TextProperty(required = True)
	room= db.TextProperty(required=True)
	created = db.DateTimeProperty(auto_now_add = True)


class Handler(webapp2.RequestHandler):
	def write(self,*a,**kw):
		self.response.out.write(*a,**kw)
	
	def render_str(self,template,**params):   # here it takes template - that is directory name and **params taking extra parameters
		t = jinja_env.get_template(template)
		return t.render(params)
	
	def render(self,template,**kw):
		self.write(self.render_str(template,**kw))

class ForumDiscuss(Handler):
        
	def render_front(self,title = "",art ="",error = ""):
		arts = db.GqlQuery("select * from Art order by created desc")

		self.render('discuss.html',title = title,art = art,error = error,arts = arts)

	def get(self):
		self.render_front()

	def post(self):
		title =  self.request.get('title')
		art = self.request.get('art')

		if title and art :
			 a = Art(title = title, art = art,room='discuss')
			 a.put()
			 self.render_front()
		else:
			error = "Please input both a username and a mesage."
			self.render_front(title = title, art = art ,error = error)

class ForumSuggest(Handler):
        
	def render_front(self,title = "",art ="",error = ""):
		arts = db.GqlQuery("select * from Art order by created desc")

		self.render('suggestions.html',title = title,art = art,error = error,arts = arts)

	def get(self):
		self.render_front()

	def post(self):
		title =  self.request.get('title')
		art = self.request.get('art')

		if title and art :
			 a = Art(title = title, art = art,room='suggest')
			 a.put()
			 self.render_front()
		else:
			error = "Please input both a username and a mesage."
			self.render_front(title = title, art = art ,error = error)
class HomeHandler(webapp2.RequestHandler):
    def get(self):
        f = open('home.html')
        f = f.read()
        self.response.write(f)
class NewsHandler(webapp2.RequestHandler):
    def get(self):
        f = open('devlog.html')
        f = f.read()
        self.response.write(f)
class ForumHandler(webapp2.RequestHandler):
    def get(self):
        f = open('forum.html')
        f = f.read()
        self.response.write(f)
class WikiHandler(webapp2.RequestHandler):
    def get(self):
        f = open('wiki.html')
        f = f.read()
        self.response.write(f)
class ForumDevsHandler(webapp2.RequestHandler):
    def get(self):
        f = open('forumdevs.html')
        f = f.read()
        self.response.write(f)
class GameHandler(webapp2.RequestHandler):
    def get(self):
        f = open('xzonepage.html')
        f = f.read()
        self.response.write(f)

app = webapp2.WSGIApplication([
    ('/', HomeHandler),('/news', NewsHandler),('/forum',ForumHandler),('/wiki',WikiHandler),('/forumdevs', ForumDevsHandler),('/game', GameHandler),
    ('/forumdiscuss', ForumDiscuss),('/forumsuggest', ForumSuggest)
], debug=True)
