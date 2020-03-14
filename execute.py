#9-22
#23-30
#31-43
#54-59
#75-150

import cv2
import numpy as np
import os

def video(video_name, imgs):
    imgs = list(map(lambda img: (img*255).astype(np.uint8), imgs))
    frame = imgs[0]
    height, width, layers = frame.shape

    frame_rate = 7.5
    #fourcc = cv2.VideoWriter_fourcc(*'vp80')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # note the lower case
    video = cv2.VideoWriter(video_name, fourcc, frame_rate, (width, height))

    for img in imgs[1:]:
        video.write(img)

    cv2.destroyAllWindows()
    video.release()

def load_data(start = 1, end = 151):
    a = np.load("model.pth")
    b = list(filter(
        lambda file: int(file.split("_")[-1].split(".")[0]) <= end and int(file.split("_")[-1].split(".")[0]) >= start,
        os.listdir("results/gta/test_latest/test_A")
    ))
    
    b.sort()
    
    real_ints = np.load("names.npy")[2:]
    fakes = list(filter(
        lambda fake: int(fake.split("_")[-1].split(".")[0]) in real_ints,
        b
    ))

    imgs = []

    for img in zip(a[2:], fakes):
        _a, _b_name = img
        _b = cv2.imread("results/gta/test_latest/test_A/{}".format(_b_name))

        imgs.append((_a/350 + _b/1200))

    return imgs

video("output.mp4", load_data())

'''
a = cv2.imread("output_1/00014.png")
b = cv2.imread("output_2/fake_B_00014.jpg")

a = cv2.resize(a, (b.shape[1], b.shape[0]), interpolation = cv2.INTER_AREA)

#cv2.imshow("Resized image", (a/300 + b/700))
cv2.imshow("Resized image", (a/350 + b/850))
cv2.waitKey(0)
cv2.destroyAllWindows()
'''