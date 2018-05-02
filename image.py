from cv2 import *


def incCount(count):
    f=open('count.txt','w')
    f.write(str(count))

def getCount():
    try:
        f=open('count.txt','r')
        count=int(f.read())
        return count+1
    except:
        f=open('count.txt','w')
        f.write('1')
        return 1

def imageCaputre():
    cam = VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()
    if s:    # frame captured without any errors
        namedWindow("cam-test")
        imshow("cam-test",img)
        waitKey(0)
        destroyWindow("cam-test")
        count=getCount()
        imwrite("filename{}.jpg".format(count),img)
        incCount(count)
        cam.release()

