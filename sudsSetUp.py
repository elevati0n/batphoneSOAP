import suds 
import logging

from suds.client import Client

def enableLogging():

	logging.basicConfig(level=logging.INFO)


	#Set the logging level to DEBUG on this module to see soap messages (in & out) and http headers.
	logging.getLogger('suds.client').setLevel(logging.DEBUG)

	#Set the logging level to DEBUG on this module to see more details about soap messages (in & out) and http headers.
	logging.getLogger('suds.client').setLevel(logging.DEBUG)

	#Set the logging level to DEBUG on this module to see digestion of the schema(s).
	logging.getLogger('suds.client').setLevel(logging.DEBUG)

	#Set the logging level to DEBUG on this module to see digestion WSDL.
	logging.getLogger('suds.client').setLevel(logging.DEBUG)

	print "okay the script ran"

	return

def GetWeather(str = "Boston"):
	enableLogging()

	url = 'http://graphical.weather.gov/xml/SOAP_server/ndfdXMLserver.php?wsdl'

	client = Client(url)

	#client.set_options(port='WeatherForecastSoap')

	print client

	client.service['ndfdXMLPort'].getWeatherByPlaceName("Boston")

	return client


def __main__():
	client = GetWeather(str = "Boston")

	return client


def bank():
	enableLogging()

	url = 'http://www.thomas-bayer.com/axis2/services/BLZService?wsdl'

	client = Client(url)

	client.set_options(service='BLZService', port='BLZServiceSOAP11port_http')

	return client
















