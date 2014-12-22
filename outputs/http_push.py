import output
import datetime
import requests

class Print(output.Output):
        requiredData = ["url_root"]
        optionalData = []

	def __init__(self,data):
		self.url_root = data["url_root"]

	def outputData(self,dataPoints):
		print ""
		theDateTime = str(datetime.datetime.now())
		print "Time: " + theDateTime

		urlString = "time=" + theDateTime

		for i in dataPoints:
			print i["name"] + ": " + str(i["value"]) + " " + i["symbol"]
			urlString = urlString + "&" + i["name"] + "=" + str(i["value"]) + "," + i["symbol"]

		full_url = self.url_root + "?" + urlString
		print full_url

		r = requests.get(full_url)

		return True
