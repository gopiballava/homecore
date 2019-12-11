import cherrypy

# "http://192.168.88.62:8192/reading/temperature/%x:%x:%x:%x:%x:%x:%x:%x/%d",

class Measurements(object):
	def __init__(self):
		pass
		
	@cherrypy.expose
	def reading(self, type, id, value):
		temp_c = float(value) / 100
		temp_f = (( 9./5) * temp_c) + 32
		print("====>    {}     {:.1f}C   {:.1f}F".format(id, temp_c, temp_f))


def main(argv):
	cherrypy.config.update( {'server.socket_host': '0.0.0.0',
							'server.socket_port':  8192,
							})
	cherrypy.quickstart(Measurements())

if __name__ == '__main__':
    main([])
