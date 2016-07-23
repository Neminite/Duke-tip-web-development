import os 
import webapp2
import jinja2  # template language

from google.appengine.ext import db

# always copy these 2 lines below
template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir)
								,autoescape = True)

		

class Comment(db.Model):
	name = db.StringProperty(required = True)
	comment = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)


class Handler(webapp2.RequestHandler):
	def write(self,*a,**kw):
		self.response.out.write(*a,**kw)

	
	def render_str(self,template,**params):   # here it takes template - that is directory name and **params taking extra parameters
		t = jinja_env.get_template(template)
		return t.render(params)
	
	def render(self,template,**kw):
		self.write(self.render_str(template,**kw))

class ChatPage(Handler):

	def render_front(self,name = "",comment ="",error = ""):
		comments = db.GqlQuery("select * from Comment order by created desc")

		self.render('front.html',name = name,comment = comment,error = error,comments = comments)

	def get(self):
		self.render_front()

	def post(self):
		name = self.request.get('name')
		comment = self.request.get('comment')

		if name and comment :
			 a = Comment(name = name, comment = comment)
			 a.put()
			 self.render_front()
		else:
			error = "we need both comment and name"
			self.render_front(name = name, comment = comment ,error = error)

class MainHandler(Handler):
	def get(self):
		self.render('main.html')

class StoreHandler(Handler):
	def get(self):
		self.render('Web.html')

class TipsHandler(Handler):
	def get(self):
		self.render('Pokemon.html')


app = webapp2.WSGIApplication([
    ('/chat', ChatPage), ("/", MainHandler), ("/store", StoreHandler), ("/tips", TipsHandler)
], debug=True)
