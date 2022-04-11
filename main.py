from asyncio.base_subprocess import ReadSubprocessPipeProto
import json
from time import sleep
from xmlrpc.client import ResponseError
from h11 import CLIENT
import requests
import os
import datetime
import Google
from Google import Create_Service
from googleapiclient.http import MediaFileUpload



file  = open("data-escape/link.txt",encoding='utf8')
for i in file:
	url = "https://tiktok-video-downloader.p.rapidapi.com/api/downloader"

	querystring = {"url":f"{i}"}

	headers = {
		"X-RapidAPI-Host": "tiktok-video-downloader.p.rapidapi.com",
		"X-RapidAPI-Key": "{key}"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	response_json = response.json()
	x = json.dumps(response_json)
	y = json.loads(x)
	url = y["data"]["destinationUrl"]
	nicname = y["data"]["authorId"]
	video_id =  y["data"]["videoId"]

	file_name = video_id + ".mp4"
	print(file_name)
	try:
		r = requests.get(url, allow_redirects=True)
		sleep(3)
		open(file_name,"wb").write(r.content)
		sleep(3)
		os.system(f"python upload_video.py --file=\"{file_name}\" --title=\"{nicname} new tiktok video #Shorts \" --description=\"{nicname} new video #Shorts  #tiktok\"  --keywords=\"{nicname},tiktok,video,shorts\"  --category=\"22\" --privacyStatus=\"public\" --noauth_local_webserver")
		sleep(25)
		os.system(f"rmdir {file_name}")
	except:
		pass


