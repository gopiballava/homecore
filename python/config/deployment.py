import configparser

if __name__ == '__main__':
	conf = configparser.ConfigParser()
	conf.read('example_deploy.ini')
	print(conf)
	print(conf.sections)
	for section in conf.sections()import cherrypy
import webbrowser
import os
import simplejson
import sys

MEDIA_DIR = os.path.join(os.path.abspath("."), u"media")

class AjaxApp(object):
   @cherrypy.expose
   def index(self):
      return open(os.path.join(MEDIA_DIR, u'index.html'))

   @cherrypy.expose
   def submit(self, name):
      cherrypy.response.headers['Content-Type'] = 'application/json'
      return simplejson.dumps(dict(title="Hello, %s" % name))
		
config = {'/media':
   {'tools.staticdir.on': True,
   'tools.staticdir.dir': MEDIA_DIR,}
}
			
def open_page():
webbrowser.open("http://127.0.0.1:8080/")
cherrypy.engine.subscribe('start', open_page)
cherrypy.tree.mount(AjaxApp(), '/', config=config)
cherrypy.engine.start()f:
		print(section)
		print(dir(section))
"""
import configparser
conf = configparser.ConfigParser()
conf.read('example_deploy.ini')
"""