
# chron job this needs to be a separate file

import os

# take picture

os.system("fswebcam /home/jsun/sunnifer.github.io/plantpics/plantpic.jpg")

# rename file with time stamp

os.system("mv /home/jsun/sunnifer.github.io/plantpics/plantpic.jpg $(date +%Y%m%d%H%M%S).jpg")

# add time stamp

# append new photo to bottom of page for now

# update github