#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os
import cv2


# In[2]:


allImgs = [None] * 32
dirt = "results/label2city_2048/test_latest/stuttgart_00/"
for file in os.listdir(dirt):
    idx = int(file.split("_")[5])
    if not allImgs[idx]: allImgs[idx] = {
        "real": "",
        "fake": "",
    }
    allImgs[idx][file.split("_")[0]] = dirt + file


# In[3]:


video_name = 'video.webm'

images = [img for img in os.listdir(dirt) if (img.endswith(".jpg") and "fake" in img)]
images.sort()
#print(images)


# In[4]:


frame = cv2.imread(os.path.join(dirt, images[0]))
height, width, layers = frame.shape

frame_rate = 15
fourcc = cv2.VideoWriter_fourcc(*'vp80')
video = cv2.VideoWriter(video_name, fourcc, frame_rate, (width, height))

for image in images:
    video.write(cv2.imread(os.path.join(dirt, image)))

cv2.destroyAllWindows()
video.release()


# In[5]:


from IPython.display import HTML

HTML("""
    <video alt="test" width=400 height=200 controls>
        <source src="video.webm" type="video/mp4">
    </video>
""")


# In[ ]:


get_ipython().run_line_magic('notebook', 'inline')
count = 0
for img in allImgs:
    if img:
        count += 1

fig, ax = plt.subplots(count, 2, figsize=(30,30))
idx = 0
for img in allImgs:
    if not img: continue
    ax[idx, 0].imshow(mpimg.imread(img["real"]))
    ax[idx, 1].imshow(mpimg.imread(img["fake"]))
    idx += 1


# In[ ]:


int("000001")

