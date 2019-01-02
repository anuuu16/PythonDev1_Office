import requests
import base64
import sys
import json

GOOGLE_API_KEY = "AIzaSyDU0Z0gMI4FlBxk1SL6m3iCNhOZizQOByw"
GOOGLE_CLOUD_VISION_URL = "https://vision.googleapis.com/v1/images:annotate"

file="C:/Users/anubhav.singh/Desktop/Vision/img1.jpg"

img = open(file, "rb")
b64_string = base64.b64encode(img.read())
img.close()

req_data = {
  "requests":[
    {
      "image":{
        "content":b64_string
      },
      "features":[
        {
          "type":"LABEL_DETECTION",
          "maxResults":1
        }
      ]
    }
  ]
}

r = requests.post("%s?key=%s" % (GOOGLE_CLOUD_VISION_URL, GOOGLE_API_KEY), json.dumps(req_data), headers={'content-type': 'application/json'})

print (r.text)
