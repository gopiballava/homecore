import cherrypy
import webbrowser
import os
import simplejson
import sys
import time
import pinject

MEDIA_DIR = os.path.join(os.path.abspath("."), u"html")


def all_subclasses(cls):
    return set(cls.__subclasses__()).union(
        [s for c in cls.__subclasses__() for s in all_subclasses(c)])

class Bar(object):
	def bar(self):
		return "baer"


class pin(object):
	@pinject.copy_args_to_internal_fields
	def __init__(self, bar):
		pass
	def foo(self):
		print('Foo!')
		print(self._bar.bar())


class AjaxApp(object):
	def __init__(self):
		self._start_time = time.time()
		self._obj_graph = pinject.new_object_graph()
# 		foo = self._obj_graph.provide(pin)
		foo = self._obj_graph.provide(getattr(sys.modules[__name__], 'pin'))
		foo.foo()

	@cherrypy.expose
	def index(self):
		return open(os.path.join(MEDIA_DIR, u'battery.html'))

	@cherrypy.expose
	@cherrypy.tools.json_out()
	def submit(self, name):
		cherrypy.response.headers['Content-Type'] = 'application/json'
		return dict(title="Hello, %s" % name)
#		  return simplejson.dumps(dict(title="Hello, %s" % name))

	@cherrypy.expose
	def param_div(self, name):
		if name == 'clock':
			return '{}'.format(time.asctime())
		elif name == 'duration':
			return '{} seconds ago'.format(int(time.time() - self._start_time))
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
