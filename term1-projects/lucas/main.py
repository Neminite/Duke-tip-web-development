#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#	 http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from html import *



class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write(subHtml)
class PageHandler(webapp2.RequestHandler):
	def post(self):
		output(self)
class WpHandler(webapp2.RequestHandler):
	def get(self):
		f=open("first.html","r")
		self.response.write(f.read())

class PizzaHandler(webapp2.RequestHandler):
	def get(self):
		p=open("pizza.html","r")
		self.response.write(p.read())

class PizzapHandler(webapp2.RequestHandler):
	def get(self):
		p=int(self.request.get("s_type"))
		extracheese=self.request.get("avacado")
		avacado=self.request.get("extracheese")
		eggs=self.request.get("eggs")
		name=self.request.get("name")
		if extracheese:
			p=p+1
		if avacado:
			p=p+1
		if eggs:
			p=p+1
		self.response.write("Thank you "+str(name)+" for ordering food from us. The total is $"+str(p))



app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/page', PageHandler),
	('/mypage',WpHandler),
	('/pizza',PizzaHandler),
	('/pp',PizzapHandler)
], debug=True)

	#	f=open("first.html","r")
	#   self.response.write(f.read())