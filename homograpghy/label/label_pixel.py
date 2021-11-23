import cv2
import numpy as np
img = cv2.imread(r'D:\jupyter notebook\cv\homograpghy\test_data\test.jpg')
xs =[]
ys = []
def on_EVENT_LBUTTONDOWN(event, x, y,flags, param):
     if event == cv2.EVENT_LBUTTONDOWN:
         xy = "%d,%d" % (x, y)
         xs.append(x)
         ys.append(y)
         cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
         cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0, 0, 0), thickness=1)
         cv2.imshow("image", img)

cv2.namedWindow("image")
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.imshow("image", img)
cv2.waitKey(0)
data=np.stack([xs,ys],axis=1)
with open(r"D:\jupyter notebook\cv\homograpghy\test_data\test.txt","w") as f:
     np.savetxt(f,data)