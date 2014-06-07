import osimport urllibimport loggingfrom google.appengine.api import usersfrom google.appengine.ext import ndbimport jinja2import webapp2JINJA_ENVIRONMENT = jinja2.Environment(	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),	extensions=['jinja2.ext.autoescape'],	autoescape=True)DEFAULT_RECIPE_NAME = 'soooo tasty'		def recipe_key(n = DEFAULT_RECIPE_NAME):	return ndb.Key('Recipe', n)	class Ingredient(ndb.Model):	i = ndb.StringProperty()	amount = ndb.IntegerProperty()	type = ndb.StringProperty()	class Recipe(ndb.Model):	name = ndb.StringProperty('n')	"""ingredients = ndb.StructuredProperty(Ingredient, repeated=True)"""	ingredients = ndb.StructuredProperty(Ingredient, repeated=True)	instructions = ndb.StringProperty('inst', repeated=True)class AddRecipe(webapp2.RequestHandler):	def post(self):		n = self.request.get('recipeName')		i = self.request.get_all("ing")		a = self.request.get_all("amt")		t = self.request.get_all("type")		recipe = Recipe()		recipe.name = self.request.get('recipeName')				for x, y, z in i, a, t:			recipe.ingredients =  [Ingredient(x,y,z)]		recipe.instructions = self.request.get_all('step')		recipe.put()						ing = self.request.get_all('ing')		inst = self.request.get_all('inst')		logging.info(ing)		logging.info(inst)		query_params = {'recipeName' : n}		for ingredient in ing:			query_params['ing'] = ingredient				self.redirect('/upload?' + urllib.urlencode(query_params))	class Upload(webapp2.RequestHandler):	def get(self):		template = JINJA_ENVIRONMENT.get_template('upload.html')		self.response.write(template.render())		class MainPage(webapp2.RequestHandler):	def get(self):		template = JINJA_ENVIRONMENT.get_template('index.html')		self.response.write(template.render())		application = webapp2.WSGIApplication([	('/', MainPage),	('/upload', Upload),	('/addrecipe', AddRecipe),], debug=True)def main():    # Set the logging level in the main function    # See the section on Requests and App Caching for information on how    # App Engine reuses your request handlers when you specify a main function    logging.getLogger().setLevel(logging.DEBUG)    webapp.util.run_wsgi_app(application)if __name__ == '__main__':    main()