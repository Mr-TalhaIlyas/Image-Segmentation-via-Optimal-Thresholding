# Image Segmentation via Optimal Thresholding

This repo segments the bean plant images via applying threshold on RGB values.
It involves following steps,

* Find RGB values -lets say [x,y,z]- in cases of bean plant we want to segment green color plant so RGB values will be [0, 255, 0].
* Now we will convert these values from RGB[x,y,z] space to HSV[a,b,c] space.
* Now we'll define upper and lower bound/thresholds as [a-30,50,50]->lower, [a+10,b,c]->upper bound
* We can also make these limits as hyperparameteres like in the code I defined alpha and beta
```python
    alpha = 10
    beta = 30
    color = thresh_color_rgb #RGB Format
    hsv_color = cv2.cvtColor(color,cv2.COLOR_RGB2HSV)
    # upper bound on thresholding color
    upper = (hsv_color + np.uint8([[[alpha,0,0]]])).squeeze()
    # lower bound on thresholding color
    lower = np.array([hsv_color[0,0,0]-beta,50,50]).astype(np.uint8)
```

* There might also some weed segmented in the image also so we can morphological operators to remove them.

```python
   opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
```

## Results

Following are some results,

## Failed Cases

Following is one case where we have a lot weed in the background and it also got segmented as plant.