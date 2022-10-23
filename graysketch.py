import cv2 as cv
#module imported as cv
import numpy as np
def sketch(image):
    img_gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    img_gray_blur=cv.GaussianBlur(img_gray,(5,5),0)
    canny_edges=cv.Canny(img_gray_blur,10,70)
    ret, mask=cv.threshold(canny_edges,70,255,cv.THRESH_BINARY_INV)
    
    return mask
cap=cv.VideoCapture(0)
while True:
    ret,frame=cap.read()
    cv.imshow("sketch",sketch(frame))
    if cv.waitKey(1)& 0xFF==ord('d'):
        break
cap.release()
cv.destroyAllWindows()
