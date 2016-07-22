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
#Dank MEMEMEMEMEMMEMES
import webapp2	
form = """
<form method ="post">
	<label>
		Name <span style="display:inline-block; width: 150;"></span>                     
		<input type ="text" name = "name" value = "%(name)s">
	</label>
	<br>
	<br>
	<label>
		What are u having with us <span style="display:inline-block; width: 20;"></span>  
		<select name = "sandwich_type">
			<option value = "Chicken"> Chicken sandwich 6$</option>
			<option value = "Veggie"> Veggie sandwich 5$ </option>
			<option value = "Gchicken"> Grilled Chicken 7$ </option>
		</select>
	</label>
	<br>
	<br>

	<label>
		Want toppings ?<span style="display:inline-block; width: 87;"></span>
		<label>
		   <u> Extracheese </u>
			<input type ="checkbox" name = "extracheese" >
		</label>
		
		<label>
		   <u> Avacado </u>
			<input type ="checkbox" name = "avacado" >
		</label>
		<label>
		   <u> Eggs </u>
			<input type ="checkbox" name = "eggs" >
		</label>

	</label>
	<br>
	<br>
	<div style ="color : red"> %(error)s </div>
	<input type = "submit">
</form>
"""


class MainHandler(webapp2.RequestHandler):
	
	def write_form(self,error ="",name =""):
		self.response.write(form %{"error":error,"name":name})

	def get(self):
		self.write_form()

	def post(self):
		
		name = self.request.get('name')
		
		extracheese = self.request.get('extracheese')
		avacado = self.request.get('avacado')
		eggs = self.request.get('eggs')

		total = 0
		sandwich_type = self.request.get('sandwich_type')
		if sandwich_type == 'Chicken':
			total = total + 6
		if sandwich_type == 'Veggie':
			total = total + 5
		if sandwich_type == 'Gchicken':
			total = total + 7

		if extracheese:
			total = total + 1
		if avacado:
			total = total + 1
		if eggs:
			total = total + 1

		final_variable = "Thanks "+name+" for your business your total balance is :"+str(total - 1) 

		if not name :
			self.write_form("u need to put ur name there")
		elif not(extracheese or avacado or eggs):
			self.write_form("please select one we have this as complementary",name)
		else:
			self.redirect('/thanks?q='+final_variable) 		


class ThanksHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(self.request.get('q'))

		
app = webapp2.WSGIApplication([
	('/', MainHandler),('/thanks',ThanksHandler)
], debug=True)
