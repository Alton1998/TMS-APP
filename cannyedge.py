# server ip=172.16.73.152
import json
import requests
import numpy as np
import cv2
import math
import webbrowser
import time
hl, = plt.plot([], [])
cap=cv2.VideoCapture(0)#declaring camera Instance 0
cap1=cv2.VideoCapture(1)# declaring camera Instance 1
cap2=cv2.VideoCapture(2)# delaring camera Instance 2
cap3=cv2.VideoCapture(3)# declaring camera Instance 3

#function to send data inform of json send(protocol,ip,api name,data)
def send(HTTP_SCHEMA,URI_PREFIX,URI_SUFFIX,data):
    #url for Api
    url = HTTP_SCHEMA + URI_PREFIX + URI_SUFFIX
    # content for json data
    data = {"Trafficdensity": data,
            "time": "02/07/2018 16:36:27"
            }
    # defining the type of content being sent
    headers = {'Content-type': 'application/json'}
    # Posting data
    r = requests.post(url, data=json.dumps(data), headers=headers, auth=('alton', 'armourofgod'))

#     finding density of traffic findDensity(reference_image,realtime_image,name of the camera)
def findDensity(image1,image2,camera):
    print("camera" + camera)
    # mean of reference of image
    print(np.mean(image1))
    # mean of image in realtime
    print(np.mean(image2))
    # mean=real_time_image-reference_image
    mean=np.mean(image2)-np.mean(image1)
    print(mean)
    return mean
# display canny edge picture generated display(image matrix,name of the window,name of the file to write to)
def display(image,name,imgname):
    # Converting image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #Sharpening image through Gaussian blur
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    # Performing Edge Detection
    edged = cv2.Canny(gray, 35, 125)
    # Writing the generated pixel matrix to a jpg file
    cv2.imwrite(imgname,edged)
    # displaying said matrix
    cv2.imshow(name,edged)
    return 1
while True:
    # Reading images frame by frame thus forming a live video feed
    ret,frame=cap.read()
    ret1, frame1 = cap1.read()
    ret2, frame2= cap2.read()
    cv2.imshow('frame', frame)
    cv2.imshow('frame1',frame1)
    cv2.imshow('frame2',frame2)
    display(frame,'edged','realtimedata111.jpg')
    # storing density values
    k = findDensity(cv2.imread('realtimedata11.jpg'), cv2.imread('realtimedata111.jpg'),'1')
    # sending the data
    send('http://','172.16.73.152','/TrafficAtA/',k)
    display(frame1,'edged2','realtimedata222.jpg')
    k1 = findDensity(cv2.imread('realtimedata22.jpg'), cv2.imread('realtimedata222.jpg'),'2')
    send('http://', '172.16.73.152', '/TrafficAtB/',k1)
    display(frame2,'edged3','realtimedata333.jpg')
    k2 = findDensity(cv2.imread('realtimedata33.jpg'), cv2.imread('realtimedata33.jpg'),'3')
    send('http://', '172.16.73.152', '/TrafficAtC/',k2)
    # calling the automate function present in the server
    webbrowser.open('http://172.16.73.152/automate/')
    time.sleep(5)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
