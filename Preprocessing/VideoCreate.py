import os
from moviepy.editor import *

clips = []

i = 1
while i < 321:
    clips.append(ImageClip('frames/Frame'+str(i)+'.jpg').set_duration(00.03))
    i = i+1

video = concatenate(clips, method='compose')
video.write_videofile('7.mp4', fps=30)

