import cherrypy
import json
import io
import tarfile
from io import BytesIO
# curl -k https://micropython.org/pi/micropython-pystone_lowmem/json
# {"info": 
#     {"version": "3.4.2.post4"}, 
# "releases": 
#     {"3.4.2.post4": [{"url": "https://micropython.org/pi/pystone_lowmem/pystone_lowmem-3.4.2.post4.tar.gz"}
#     ]
#     }
#     }%
"""
Micropython test


"""


class Packaging(object):
    def __init__(self):
        pass

    @cherrypy.expose
    def pi(self, package_name, json_string):
        if json_string != "json":
            raise Exception
        return json.dumps(
            {"info": 
                {"version": "1.2.3"}, 
            "releases": 
                {"1.2.3": [{"url": "https://127.0.0.1/pkg/foo.tar.gz"}
                ]
                }
            }
            )

    @cherrypy.expose
    def pkg(self, name):
        print("Got request for {}".format(name))
        file_out = BytesIO()
        tar = tarfile.open(mode = "w:gz", fileobj = file_out)

        # tar = tarfile.open(fileobj=io_bytes, mode='w:gz')
        tar.add('packaging.py')
        tar.close()
        return file_out.getvalue()
        # return io_bytes

def main(argv):
    cherrypy.config.update({'server.socket_host': '0.0.0.0',
                            'server.socket_port':  443,
                            'server.ssl_module': 'builtin',
                            'server.ssl_certificate': 'ssl/cert.pem',
                            'server.ssl_private_key': 'ssl/privkey.pem',
                            })
    cherrypy.quickstart(Packaging())


if __name__ == '__main__':
    main([])
