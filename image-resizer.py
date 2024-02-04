import cv2
#Configurable Parameters
source = "flower.jpg"
destination = 'newImage.png'
src = cv2.imread(source,cv2.IMREAD_UNCHANGED)

#Percent by which image is resized
scalePercent=50

#cv2.imshow("Title",src)

#Calculate the 50% of original dimensions
newWidth = int(src.shape[1]*scalePercent/100)
newHeight = int(src.shape[0]*scalePercent/100)

dsize = (newWidth,newHeight)

#Resize Image
result = cv2.resize(src,dsize)

cv2.imwrite('newImage.png',result)
#cv2.waitKey(0)
