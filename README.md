# Tiktok Video Upload Youtube Script

> the main purpose of this script is to upload videos that you receive via tiktok to your channel using the youtube api
> _For instructions on installation, see  [Installation]. I highly recommend you follow them._
## Installation

### Step 1 (Installing Script)
```sh
git clone https://github.com/fatkz/tiktok-video-upload-youtube-script.git
cd tiktok-video-upload-youtube-script
pip3 install -r requirements.txt
```
### Step 2 (Token Set)

```sh
{
    "web": {
      "client_id": "",
      "client_secret": "",
      "redirect_uris": [],
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://accounts.google.com/o/oauth2/token"
    }
  }

```
1-) The {client_secret} and {client_id} values that you get from the Google api console are called "client_secrets.add it to the "json" file

```
headers = {
		"X-RapidAPI-Host": "tiktok-video-downloader.p.rapidapi.com",
		"X-RapidAPI-Key": "{key}"
	}
```

2-) 'main.py' fill in the 'X-RapidAPI-Key' section in the 'file

### Step 3 (Api Authentication)

```sh
python3 upload_video.py --file {filename}.mp4
```
to make api authorization, you can use any '.mp4' file 'upload_video.py ' give the file as you see above

### Step 4 (Upload Video)
```sh

python upload_video.py --file=\"{filename}.mp4\" --title=\"Summer vacation in California\" --description=\"Had fun surfing in Santa Cruz\"  --keywords=\"surfing,Santa Cruz\"  --category=\"22\" --privacyStatus=\"private\"

```
1-) the link is in the data escape file. create a file named txt and add the videos you want to upload from tiktok here

2-) then upload their videos to youtube with the test run code you saw above



## Not: Bugs will be fixed in the future

