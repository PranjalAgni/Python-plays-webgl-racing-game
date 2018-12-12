import cv2
import numpy as np
from drawlanes import draw_lanes
from numpy import ones,vstack
from numpy.linalg import lstsq


# Region of Interest image processing 
def roi(img, vertices):
    mask = np.zeros_like(img)

    cv2.fillPoly(mask, vertices, 25)

    masked = cv2.bitwise_and(img, mask)

    return masked




def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    
    processed_img = cv2.GaussianBlur(processed_img,(5,5),0)
    
    vertices = np.array([[10,400],[10,300],[300,200],[500,200],[800,300],[800,500],
                         ], np.int32)

    # vertices = np.array([[26,426],[370,303],[400,200],[650,200],[609,291],[980,435],
    #                      ], np.int32)


    processed_img = roi(processed_img, [vertices])


    # cv2.imshow('processed_img', cv2.cvtColor(processed_img, cv2.COLOR_GRAY2BGR))

    # more info: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html
    #                                     rho   theta   thresh  min length, max gap:        
    # lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, np.array([]), 100, 5)

    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180)
    m1 = 0
    m2 = 0
    try:
        l1, l2, m1, m2 = draw_lanes(original_image,lines)
        cv2.line(original_image, (l1[0], l1[1]), (l1[2], l1[3]), [0,255,0], 30)
        cv2.line(original_image, (l2[0], l2[1]), (l2[2], l2[3]), [0,255,0], 30)
    except Exception as e:
        print(str(e))
        
    if lines is not None:
            for coords in lines:
                coords = coords[0]
                try:
                    cv2.line(processed_img, (coords[0], coords[1]), (coords[2], coords[3]), [255,0,0], 3)
                    
                except Exception as e:
                    print(str(e))

    else:
        pass


    return processed_img,original_image,m1,m2