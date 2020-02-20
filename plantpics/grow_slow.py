import sys
import os
from twython import Twython

# go here and create a new app: https://apps.twitter.com
# then click "key and access tokens" to generate them
# put them inside the quotes below

CONSUMER_KEY = 'GHZDmMbE2sPFjPH5hLNeiu9Ip'
CONSUMER_SECRET = 'Y0QzlB5NJhnbmaJAvcqIQv9XYXOi674nTwutD6Jmh3ArC2No75'
ACCESS_KEY = '1227071587700092929-29yXcXDNyJRuEdot9EnypdubzKyiXj'
ACCESS_SECRET = 'dj5OfDMRoWtdEUij7TdnnJtOGykd5f8iFegJu7Svoy5o5'


# this runs the following script from the command line that takes the photo and saves it
# it will only work for USB webcams,
# you'll have to do something different if you're using a pi-cam

os.system ("fswebcam -d/dev/video0 -r1280x960 --no-banner plantpic.jpg")

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
photo = open('plantpic.jpg','rb')
image_ids = api.upload_media(media=photo)
api.update_status(status='', media_ids=image_ids['media_id'])

os.system ("mv plantpic.jpg $(date +%Y%m%d%H%M%S).jpg")