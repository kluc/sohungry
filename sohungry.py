import osimport urllibfrom google.appengine.api import usersfrom google.appengine.ext import ndbimport jinja2import webapp2JINJA_ENVIRONMENT = jinja2.Environment(	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),	extensions=['jinja2.ext.autoescape'],	autoescape=True)class AddIng(webapp2.RequestHandler):	def get(self):		print('f')	class Upload(webapp2.RequestHandler):	def get(self):		template = JINJA_ENVIRONMENT.get_template('upload.html')		self.response.write(template.render())		class MainPage(webapp2.RequestHandler):	def get(self):		template = JINJA_ENVIRONMENT.get_template('index.html')		self.response.write(template.render())		application = webapp2.WSGIApplication([	('/', MainPage),	('/upload', Upload),	('/add', AddIng),], debug=True)