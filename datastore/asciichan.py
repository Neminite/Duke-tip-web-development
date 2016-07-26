# this code is taken from a udacity course CS253 Web Development
#************************* boiler plate code can be used in each ********************************
import os 
import webapp2
import jinja2  # template language

from google.appengine.ext import db


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

#**********************************************************************************************************

#this is a record containing 3 properties 
class Art(db.Model):
	title = db.StringProperty(required = True)
	art = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)



class MainPage(Handler):

	def render_front(self,title = "",art ="",error = ""):
		arts = db.GqlQuery("select * from Art order by created desc")

		self.render('front.html',title = title,art = art,error = error,arts = arts)

	def get(self):
		self.render_front()

	def post(self):
		title =  self.request.get('title')
		art = self.request.get('art')

		if title and art :
			 a = Art(title = title, art = art)
			 a.put()
			 self.render_front()
		else:
			error = "we need both artwork and title"
			self.render_front(title = title, art = art ,error = error)

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
