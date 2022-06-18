import cv2
image = cv2.imread("palm.jpg")
#cv2.imshow("palm",image) #to view the palm in python
#cv2.waitKey(0)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,40,55,apertureSize = 3)
edges = cv2.bitwise_not(edges)

#cv2.imshow("edges in palm",img) # to view the Lines in palm
#cv2.waitKey(0)

cv2.imwrite("palmlines.jpg", edges)
palmlines = cv2.imread("palmlines.jpg")
img = cv2.addWeighted(palmlines, 0.3, image, 0.7, 0) # Blending the above image and original image

cv2.imshow("edges in palm",img) #to view the palm lines 
cv2.waitKey(0)