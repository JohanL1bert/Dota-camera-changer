import re
import time


filename = ("client.dll")


def read_file():
    with open(filename, mode = 'rb') as r:
        find_size = re.search(b'Maximum visible distance\x00\x00\x00\x00\d{4}', r.read())
        return find_size 

    
def view_camera_distance(copy_size):
    view = copy_size[0].decode("ascii")
    return view


def find_pattern(view):
    view_size = re.search(r'[0-9]{4}', view).group()
    return view_size


def changer_cam(copy_size):
    with open(filename, mode = 'rb') as s:
        file_read = s.read()
        decode_cam_distance = copy_size[0].decode("ascii")
        copy_cam_distance = decode_cam_distance[:-4]
        encode_camera = ((copy_cam_distance + str(num_cam)).encode("ascii"))
        pattern = (b'Maximum visible distance\x00\x00\x00\x00\d{4}')
        new_camera = re.sub(pattern, encode_camera, file_read)


    with open(filename, mode = 'wb') as b:
        b.write(new_camera)



#TODO: Write check camera distance when overwriting
copy_size = read_file()
print("Hints: the original camera distance is 1200")
decode_value = view_camera_distance(copy_size)
print("Your camera distance:", find_pattern(decode_value))
while True:
    try:
        num_cam = int(input("Type only 4 digits numbers, no letters: "))
        if len(str(num_cam)) == 4 and num_cam <= 1900 and num_cam >= 1001:
            changer_cam(copy_size)
            print("___________________")
            copy_size = read_file()
            decode_value = view_camera_distance(copy_size)
            print("Your camera distance:", find_pattern(decode_value))
            time.sleep(2)
            exit()
        else:
            print("Only 4 digits number from range 1001 and 1900")
    except ValueError:
        print("No letters, only numbers")
