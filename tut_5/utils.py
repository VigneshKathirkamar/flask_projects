import cv2
import numpy as np
import matplotlib.pyplot as plt

def colorHistogram(img,histogram_path):
    chans = cv2.split(img)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title("'Flattened' Color Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    # loop over the image channels
    for (chan, color) in zip(chans, colors):
        # create a histogram for the current channel and plot it
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.savefig(histogram_path+'/histogram.png')    

def getContours(imgDil,imgContour):
    """
    Contours work best on binary images, so pass binary images to findContours function
    
    """
    contours,heirarchy = cv2.findContours(imgDil,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_TC89_KCOS)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print("Area of contours",area)
        if area > 1000:
            # cv2.drawContours(imgContour,contours,-1,(255,0,255),6)
            peri = cv2.arcLength(cnt,True)
            print("perimeter is ",peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,False)
            # print("Lenght of approx is",len(approx))
            x,y,w,h = cv2.boundingRect(approx)
            # if area > 33000 and area < 37000:
            if len(approx) < 6:
            #if peri > 500 and peri < 600:
                cv2.putText(imgContour,'Crown2',(x+w//2,y+h//2),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
                cv2.drawContours(imgContour,contours,-1,(0,0,255),6)
            # if area > 9000 and area < 19000:
            if len(approx) >= 6:
            #if peri > 600 and peri < 700:
                # print("gReatere than 8")
                cv2.drawContours(imgContour,contours,-1,(255,0,255),6)
                cv2.putText(imgContour,'Moon',(x+w//2,y+h//2),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1,cv2.LINE_AA)
                
            # elif area > 30000 and area < 33000:
            if len(approx) > 5 and len(approx) < 7:
                cv2.putText(imgContour,'Crown1',(x+w//2,y+h//2),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1,cv2.LINE_AA)

def box_detection(grayImg):

    thresh_inv = cv2.threshold(grayImg, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]

    # Blur the image
    blur = cv2.GaussianBlur(thresh_inv,(1,1),0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
    # find contours
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    mask = np.ones(grayImg.shape[:2], dtype="uint8") * 255
    for c in contours:
        # get the bounding rect
        x, y, w, h = cv2.boundingRect(c)
        if w*h>1000:
            cv2.rectangle(mask, (x, y), (x+w, y+h), (0, 0, 255), -1)

    res_final = cv2.bitwise_and(grayImg, grayImg, mask=cv2.bitwise_not(mask))
    return res_final

def binaryImage(img):
    rows,cols = img.shape[:2]
    for i in range(rows):
        for j in range(cols):
            if img[i,j,0]<img[i,j,1] and img[i,j,1]>img[i,j,2] and img[i,j,0]>=0 and img[i,j,1] > 50 and img[i,j,2] >=0:
                img[i,j,:]=255
            else:
                img[i,j,:]=0
    return img

def houghCircles(img):

    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                                param1=150,param2=30,minRadius=50,maxRadius=220)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
    return img

def StackImages(scale,ImgArray):
    """
    This function is to view images side by side for comparision
    """
    rows = len(ImgArray)
    cols = len(ImgArray[0])
    rowsAvailable = isinstance(ImgArray[0],list)
    width = ImgArray[0][0].shape[1]
    height = ImgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0,rows):
            for y in range(0, cols):
                if ImgArray[x][y].shape[:2] == ImgArray[0][0].shape[:2]:
                    ImgArray[x][y] = cv2.resize(ImgArray[x][y],(0,0),None,scale, scale)
                else:
                    ImgArray[x][y] = cv2.resize(ImgArray[x][y],(ImgArray[0][0].shape[1],ImgArray[0][0].shape[0]),None,scale,scale)
                if len(ImgArray[x][y].shape) == 2:
                    ImgArray[x][y] = cv2.cvtColor(ImgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height,width,3),np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0,rows):
            hor[x] = np.hstack(ImgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0,rows):
            if ImgArray[x].shape[:2] == ImgArray[0].shape[:2]:
                ImgArray[x] = cv2.resize(ImgArray[x],(0,0),None,scale,scale)
            else:
                ImgArray[x] = cv2.resize(ImgArray[x],(ImgArray[0].shape[1],ImgArray[0].shape[0]),None,scale,scale)
            if len(ImgArray[x].shape) == 2:
                ImgArray[x] = cv2.cvtColor(ImgArray[x],cv2.COLOR_GRAY2BGR)
        hor = np.hstack(ImgArray)
        ver = hor
    return ver

def maskImg(img):

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_green = np.array([24,54,0])
    upper_green = np.array([254,255,149])
    mask = cv2.inRange(hsv_img,lower_green,upper_green)
    result =  cv2.bitwise_and(img,img,mask=mask)
    return result