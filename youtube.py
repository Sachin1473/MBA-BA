''' This script works like IDM. You can download the whole playlist by copying just one link'''

from __future__ import unicode_literals # Module __future__ makes your code cross-Python-version compatible

import youtube_dl #Need to install youtube module from cmd, Command: pip install youtube_dl 

ydl_opts = {}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:

    ydl.download(['']) #Update the required link within ''
    
