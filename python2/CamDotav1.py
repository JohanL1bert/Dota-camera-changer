#!/usr/bin/env python2.7.6
import re, time
filename = "client.dll"
with open(filename, mode='rb') as s:
    d = s.readlines()


with open(filename, mode='rb') as r:
    total = [ 1134, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500 ]
    type (total)
    strings = re.findall('dota_camera_pitch_max\x00\x00\x00\d{4}', r.read())
    c = ''.join(strings)[24:28]
    ab = int(c)
    print ab
               


tex = ("Camera_zise 1 - 1134\n"
       "Camera_zise 2 - 1150\n"
       "Camera_zise 3 - 1200\n"
       "Camera_zise 4 - 1250\n"
       "Camera_zise 5 - 1300\n"
       "Camera_zise 6 - 1350\n"
       "Camera_zise 7 - 1400\n"
       "Camera_zise 8 - 1450\n"
       "Camera_zise 9 - 1500\n")

print tex
x = int(input ())


with open(filename, mode='wb') as outfile:
    for line in d:
        res = re.compile('dota_camera_pitch_max\x00\x00\x00\d{4}')
        index = total[x-1]
        cam = res.sub('dota_camera_pitch_max\x00\x00\x00'+ (str(index)), line)
        outfile.write(cam)

time.sleep(10)
