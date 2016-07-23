import os 
import webapp2
import jinja2  # template language

from google.appengine.ext import db

# always copy these 2 lines below
template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir)
								,autoescape = True)



class Art(db.Model):
	title = db.StringProperty(required = True)
	art = db.TextProperty(required = True)
	room = db.TextProperty(required=True)
	created = db.DateTimeProperty(auto_now_add = True)

class Login(db.Model):
	username = db.StringProperty(required = True)
	password = db.StringProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)
class Profile(db.Model):
	name= db.StringProperty(required=True)
	biography= db.TextProperty(required=True)
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
		self.render('homePage.html')

class About(Handler):
	def get(self):
		self.render('about us.html')

class ChatA(Handler):

	def render_front(self,title = "",art ="",error = ""):
		arts = db.GqlQuery("select * from Art order by created desc")

		self.render('chatA.html',title = title,art = art,error = error,arts = arts)

	def get(self):
		self.render_front()

	def post(self):
		title =  self.request.get('title')
		art = self.request.get('art')
		if title and art :
			 a = Art(title = title, art = art,room = 'A')
			 a.put()
			 self.render_front()
		else:
			error = "we need both name and message."
			self.render_front(title = title, art = art ,error = error)

class ChatB(Handler):

	def render_front(self,title = "",art ="",error = ""):
		arts = db.GqlQuery("select * from Art order by created desc")

		self.render('chatB.html',title = title,art = art,error = error,arts = arts)
		
	def get(self):
		self.render_front()

	def post(self):
		title =  self.request.get('title')
		art = self.request.get('art')

		if title and art :
			 a = Art(title = title, art = art,room='B')
			 a.put()
			 self.render_front()
		else:
			errorB = "we need both name and message."
			self.render_front(title = titleB, art = artB ,error = errorB)
class ChatC(Handler):

	def render_front(self,title = "",art ="",error = ""):
		arts = db.GqlQuery("select * from Art order by created desc")

		self.render('chatC.html',title = title,art = art,error = error,arts = arts)
		
	def get(self):
		self.render_front()

	def post(self):
		title =  self.request.get('title')
		art = self.request.get('art')

		if title and art :
			a = Art(title = title, art = art,room='C')
			a.put()
			self.render_front()
		else:
			error = "we need both name and message."
			self.render_front(title = title, art = art ,error = error)
class LoginPage(Handler):
	def render_front(self,username = "",password ="",error = ""):
		accounts = db.GqlQuery("select * from Login order by created desc")

		self.render('logincode.html',username = username,password = password,error = error,accounts = accounts)

	def get(self):
		self.render_front()

	def post(self):
		username =  self.request.get('username')
		password = self.request.get('password')
		accounts = db.GqlQuery("select * from Login order by created desc")

		if not  username and password:
			error = "we need both username and password"
			self.render_front(username = username, password = password ,error = error)
		else:
			for account in accounts:
				if account.username==username:
					if account.password==password:
						#self.response.redirect('')
						error = "It is VALID! yay"
						self.render_front(username = username, password = password ,error = error)
					else:
						error = "Invalid Password"
						self.render_front(username = username, password = password ,error = error)			
				else:
					error = "Username Does Not Exist"
					self.render_front(username = username, password = password ,error = error)
			else:
				error="No accounts found"
				self.render_front(username = username, password = password ,error = error)

class User(db.Model):
	first_name = db.StringProperty(required = True)
	last_name = db.StringProperty(required = True)
	username = db.StringProperty(required = True)
	password = db.StringProperty(required = True)
	email = db.StringProperty(required = True)
	D_O_B = db.StringProperty(required = True)
	gender = db.StringProperty(required = True)

class RegisterPage(Handler):
	def get(self):
			self.render('registercode.html')
	def post(self):
		if self.request.get('passwordsignup_confirm') == self.request.get('passwordsignup'):
			first_name = self.request.get('firstnamesignup')
			last_name = self.request.get('lastnamesignup')
			username =  self.request.get('usernamesignup')
			password = self.request.get('passwordsignup')
			password_confirm = self.request.get('passwordsignup_confirm')
			email = self.request.get('emailsignup')
			gender = self.request.get('Gender')
			D_O_B = self.request.get('month')+"/"+self.request.get('day')+"/"+self.request.get('year')
			user = User(first_name=first_name, last_name=last_name,username=username,password=password,email=email,D_O_B=D_O_B, gender=gender)
			user.put()
			login = Login(username=username,password=password)
			login.put()

app = webapp2.WSGIApplication([
    ('/', MainHandler),('/register',RegisterPage),('/login',LoginPage),('/roomA',ChatA),('/roomB',ChatB),('/roomC',ChatC),('/about',About)
], debug=True)



