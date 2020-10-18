import cv2
imgcaptur=cv2.VideoCapture(0)
result=True
while(result):
    ret,frame=imgcaptur.read()
    cv2.imwrite('test.jpg',frame)
    result=False
    print("Image Captured")

imgcaptur.release()
