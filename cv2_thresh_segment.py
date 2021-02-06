import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300
#%

def cv2_thresh_seg(img, thresh_color_rgb, apply_morph = True):
    '''

    Parameters
    ----------
    img : image to apply thresholding
    thresh_color_bgr : color value on which to apply threshold in RGB format
    apply_morph : Wheather to apply morphological operator. The default is Ture.

    Returns
    -------
    Thresholded Segmented Mask

    '''
    # if results arn't as desired try increasing or decreasing following varables
    alpha = 10
    beta = 30
    color = thresh_color_rgb #RGB Format
    hsv_color = cv2.cvtColor(color,cv2.COLOR_RGB2HSV)
    # upper bound on thresholding color
    upper = (hsv_color + np.uint8([[[alpha,0,0]]])).squeeze()
    # lower bound on thresholding color
    lower = np.array([hsv_color[0,0,0]-beta,50,50]).astype(np.uint8)
    
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    
    if apply_morph:
        #kernel = np.ones((5,5),np.uint8)
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(10,10))
        #kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        result = cv2.bitwise_and(image,image, mask= opening)
        result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        
    else:
        result = cv2.bitwise_and(image,image, mask= mask)
        result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        
    seg = np.ones((image.shape)) * [255, 255, 0] # RGB value of yellow color
    seg = np.where(result != 0, seg, result)
    
    return seg.astype(np.uint8)

thresh_color_rgb = np.uint8([[[0,255,0]]]) # RGB value on which to threshold

image = cv2.imread('C:/Users/Talha/Desktop/bean/KakaoTalk_20201116_160836253_23.png')

op = cv2_thresh_seg(image, thresh_color_rgb, apply_morph = True)
plt.imshow(op)

# dst = cv2.addWeighted(cv2.cvtColor(image,cv2.COLOR_BGR2RGB), 0.4, op, 0.7, 0.0)
# plt.imshow(dst)
#%%

########################################
#                   Test code
######################################## 
# Fro HSV Vlaues of colors
color = np.uint8([[[0,255,0]]]) #BGR Format
hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
print(hsv_color)
'''
After finding this value lets say [a,b,c] we'll define upper and lower bound as [a-30,50,50]->lower, [a+10,b,c]->upper bound
'''
#%%

image = cv2.imread('C:/Users/Talha/Desktop/image/a49.png')
#image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image)


lower = np.array([60-30,50,50])
upper = np.array([60+10,255,255])
# Convert BGR to HSV
#bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#hsv = image
mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(image,image, mask= mask)
result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
plt.imshow(result)
#%%
kernel = np.ones((10,10),np.uint8)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
plt.imshow(opening)
result = cv2.bitwise_and(image,image, mask= opening)
result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
plt.imshow(result)
#%%
seg = np.ones((image.shape)) * [255, 255, 0]
plt.imshow(seg)
seg = np.where(result != 0, seg, result)
plt.imshow(seg)



























