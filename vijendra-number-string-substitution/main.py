#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

html = """
<form method = 'post'>
<h2>I can count upto n ^ 2</h2>
<br> give me the value of n
<input type="text" name="n">
<br>
<ul>
    %(value)s
</ul>
</form>
"""
value = "<li> %(i)s </li>"
class MainHandler(webapp2.RequestHandler):
	def write_form(self,value = ''):
		self.response.write(html%{'value' : value})

	def get(self):
		self.write_form()
	
	def post(self):
		n = int(self.request.get('n',20))
		final_string =''
		for i in range(1,n+1):
			final_string = final_string + value%{'i' : i**2}
		self.write_form(final_string)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
