#python 2.7.6
import re, time
filename = "client.dll"


def find_fuc():
  with open(filename, mode='rb') as r:
      strings = re.findall('dota_camera_pitch_max_teamspec\x00\x00\d{4}', r.read())
      def_cam = ''.join(strings)[31:36]
      return def_cam



def changer_cam():
  with open (filename, mode ='rb') as s:
    file_read = s.read() 
  with open(filename, mode='rb+') as outfile:
    res = re.compile('dota_camera_pitch_max_teamspec\x00\x00\d{4}')
    cam = res.sub('dota_camera_pitch_max_teamspec\x00\x00'+ (str(num_cam)), file_read)
    outfile.write(cam)


def edit():
  global num_cam
  print "Your size", find_fuc()
  print "Type 4-digits number in range 1001 to 1800"
  while True:
    try:
      num_cam = int(raw_input())
      if len(str(num_cam)) == 4 and num_cam <= 1900 and num_cam >=1001:
        changer_cam()
        print "Complete""\n", "Your new size is:", find_fuc()
        time.sleep(3)
        exit()
      else:
        print "Only 4-digit numbers"
    except ValueError:
      print "No words, only numbers" 

edit()


#testing
