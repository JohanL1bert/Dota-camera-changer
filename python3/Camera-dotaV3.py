import re
import time

filename = ("client.dll")


def read_file():
    with open(filename, mode = 'rb') as r:
        find_size = re.search(b'r_propsmaxdist\x00\x00\d{4}', r.read())
        return find_size 



def view_camera_distance(copy_size):
    view = copy_size[0].decode("ascii")
    view_size = view[16:20]
    return view_size


def changer_cam(copy_size):
    with open(filename, mode = 'rb') as s:
        file_read = s.read()
        decode_cam_distance = copy_size[0].decode("ascii")
        copy_cam_distance = decode_cam_distance[:-4]
        encode_camera = ((copy_cam_distance + str(num_cam)).encode("ascii"))
        pattern = (b'r_propsmaxdist\x00\x00\d{4}')
        new_camera = re.sub(pattern, encode_camera, file_read)


    with open(filename, mode = 'wb') as b:
        b.write(new_camera)


copy_size = read_file()



#TODO: Write check camera distance when overwriting
print("Hints: the original camera distance is 1200")
print("Your camera distance", view_camera_distance(copy_size))
while True:
    try:
        num_cam = int(input("Type only 4 digits numbers, no letters: "))
        if len(str(num_cam)) == 4 and num_cam <= 1900 and num_cam >= 1001:
            changer_cam(copy_size)
            print("Seems to be complete")
            time.sleep(2)
            exit()
        else:
            print("Only 4 digits number from range 1001 and 1900")
    except ValueError:
        print("No letters, only numbers")
