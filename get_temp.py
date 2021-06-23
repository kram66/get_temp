from urllib.request import urlopen
import json
from datetime import datetime
import requests as req
import http.client, urllib

token = "[your token]"
station_id = "[your station id]"
device_id = "[your device id]"
push_token = "[your push token]"
user = "[your user id]"

def sendnotification(MyTitle):
	conn = http.client.HTTPSConnection("api.pushover.net:443")
	conn.request("POST", "/1/messages.json",
	urllib.parse.urlencode({
	"token": push_token,
	"user": user,
	"message": "Weather " + MyTitle,
	}), { "Content-type": "application/x-www-form-urlencoded" })
	conn.getresponse()
	

rainurl = 'https://swd.weatherflow.com/swd/rest/observations/?device_id=' + device_id + '&token=' + token
response = urlopen(rainurl)
string = response.read().decode('utf-8')
json_obj = json.loads(string)
rain_lasthour = json_obj['summary']['precip_total_1h']
rain_yesterday = json_obj['summary']['precip_accum_local_yesterday']
feels_like = json_obj['summary']['feels_like']

if rain_lasthour > 0:
	msg = ", Take an umbrella, "
else:
	msg = ", no rain, "
if feels_like < 10:
	coat = " Put on a warm coat"
else:
	coat = " light jacket"
	
x = "Temp: " + str(feels_like) + " Rain: " +  str(rain_lasthour) + msg + coat

sendnotification(x)
