import cv2 
import os
from glob import glob

#sort and get all .jpg files
images = sorted(glob("*,jpg"))

if not images:
    print("No .jpg files found")
    exit()
    
# read first image to get dimensions 
frame = cv2.imread(images[0])
height, width, layers = frame.shape

# define codec, create VideoWriter object
out = cv2.VideoWriter("retrived.avi", cv2.VideoWriter_fourcc(*'XVID'), 10, (width, height))

for image in images:
    img = cv2.imread(image)
    if img is None:
        print(f"Skipping unread{image}")
        continue
    out.write(img)
    
out.release()
print(f"saved as retrieved.avi")