#!/usr/bin/env python2.7.6
import re, time
filename = "client.dll"
with open(filename, mode='rb') as s:
    d = s.readlines()


with open(filename, mode='rb') as r:
    strings = re.findall('dota_camera_pitch_max\x00\x00\x00\d{4}', r.read())
    c = ''.join(strings)[24:28]
    print "Your size =", c


def complete():
  with open(filename, mode='wb') as outfile:
    for line in d:
      res = re.compile('dota_camera_pitch_max\x00\x00\x00\d{4}')
      cam = res.sub('dota_camera_pitch_max\x00\x00\x00'+ (str(x)), line)
      outfile.write(cam)

print "Type 4-digits number"
while True:
  try:
    x = int(raw_input())
    if len(str(x)) == 4:
      print "Complete""\n", "Your new size is:", x
      complete()
      time.sleep(3)
      exit()
    else:
      print "Only 4-digit numbers"
  except ValueError:
    print "No words, only numbers"




