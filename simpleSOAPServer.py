

from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer

def adder(a,b):
    "Add two values"
    return a+b

def networkStatus(a):
    if a > 5:
        return "good"
    else:
        return "bad"

dispatcher = SoapDispatcher(
    'my_dispatcher',
    location = "http://localhost:8008/",
    action = 'http://localhost:8008/', # SOAPAction
    #namespace = "http://example.com/sample.wsdl", prefix="ns0",
    trace = True,
    ns = True)

# register the user function
dispatcher.register_function('Adder', adder,
    returns={'AddResult': int},
    args={'a': int,'b': int})

# register the user function
dispatcher.register_function('NetworkStatus', networkStatus,
    returns={'Status': basestring},
    args={'a': int})




print "Starting server..."
httpd = HTTPServer(("", 8008), SOAPHandler)
httpd.dispatcher = dispatcher
httpd.serve_forever()

