import cherrypy
import webbrowser
import os
import simplejson
import sys
import time

MEDIA_DIR = os.path.join(os.path.abspath("."), u"html")

class AjaxApp(object):
   @cherrypy.expose
   def index(self):
      return open(os.path.join(MEDIA_DIR, u'battery.html'))

   @cherrypy.expose
   @cherrypy.tools.json_out()
   def submit(self, name):
      cherrypy.response.headers['Content-Type'] = 'application/json'
      return dict(title="Hello, %s" % name)
#       return simplejson.dumps(dict(title="Hello, %s" % name))

   @cherrypy.expose
   def param_div(self, name):
       return '<hr>{}<hr>'.format(time.asctime())
		
config = {
	'/html':
		{'tools.staticdir.on': True,
		'tools.staticdir.dir': MEDIA_DIR,},
	'/': {
		'tools.encode.on': True,
		'tools.encode.encoding': 'utf-8',
		},
}
			
def open_page():
	webbrowser.open("http://127.0.0.1:8080/")

if __name__ == '__main__':
#	cherrypy.engine.subscribe('start', open_page)
	cherrypy.tree.mount(AjaxApp(), '/', config=config)
	cherrypy.config.update({
		'tools.encode.on': True,
		'tools.encode.encoding': 'utf-8',
		'tools.encode.text_only': False,
		})
	cherrypy.engine.start()
