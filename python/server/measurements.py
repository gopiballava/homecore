import cherrypy

# "http://192.168.88.62:8192/reading/temperature/%x:%x:%x:%x:%x:%x:%x:%x/%d",

class Measurements(object):
	def __init__(self):
		pass
		
	@cherrypy.expose
	def reading(self, type, id, value):
		print(type, id, value)


def main(argv):
	cherrypy.config.update( {'server.socket_host': '0.0.0.0',
							'server.socket_port':  8242,
							})
	cherrypy.quickstart(Measurements())