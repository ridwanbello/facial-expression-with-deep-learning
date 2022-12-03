#PRE-PROCESSING CODE
# Importing necessary libraries
import cv2 
import numpy as np

# Create a function for CLAHE Histogram Equalization
def improve_contrast_image_using_clahe(bgr_image: np.array) -> np.array:
    hsv = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
    hsv_planes = cv2.split(hsv)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    hsv_planes[2] = clahe.apply(hsv_planes[2])
    hsv = cv2.merge(hsv_planes)
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
  
 #import cv2
import glob, os, errno

# Replace mydir with the directory you want
mydir = r'C:\Users\Ridwan Bello\Desktop\processing/all/expr/angry'

#check if directory exist, if not create it
try:
    os.makedirs(mydir)
except OSError as e:
    if e.errno == errno.EEXIST:
        raise
for fil in glob.glob("*.jpg"):
    image = cv2.imread(fil) 
    gray_image = improve_contrast_image_using_clahe(image)
    #gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert to greyscale
    cv2.imwrite(os.path.join(mydir,fil),gray_image) # write to location with same name
