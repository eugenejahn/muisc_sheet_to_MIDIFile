import numpy as np
import sys
import cv2 as cv
from matplotlib import pyplot as plt




# from opencv tutorial
# https://docs.opencv.org/3.4/dd/dd7/tutorial_morph_lines_detection.html 
def extract(img):

    # [gray]
    # Transform source image to gray if it is not already
    if len(img.shape) != 2:
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    else:
        gray = img


    gray = cv.bitwise_not(gray)
    bw = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                cv.THRESH_BINARY, 15, -2)
    # Show binary image
    # show_wait_destroy("binary", bw)
    # [bin]

    # [init]
    # Create the images that will use to extract the horizontal and vertical lines
    horizontal = np.copy(bw)
    vertical = np.copy(bw)
    # [init]

    # [horiz]
    # Specify size on horizontal axis
    cols = horizontal.shape[1]
    horizontal_size = cols // 30

    # Create structure element for extracting horizontal lines through morphology operations
    horizontalStructure = cv.getStructuringElement(cv.MORPH_RECT, (horizontal_size, 1))

    # Apply morphology operations
    horizontal = cv.erode(horizontal, horizontalStructure)
    horizontal = cv.dilate(horizontal, horizontalStructure)

    # Show extracted horizontal lines
    # show_wait_destroy("horizontal", horizontal)
    # [horiz]

    # [vert]
    # Specify size on vertical axis
    rows = vertical.shape[0]
    verticalsize = rows // 30

    # Create structure element for extracting vertical lines through morphology operations
    verticalStructure = cv.getStructuringElement(cv.MORPH_RECT, (1, verticalsize))

    # Apply morphology operations
    vertical = cv.erode(vertical, verticalStructure)
    vertical = cv.dilate(vertical, verticalStructure)

    # Show extracted vertical lines
    # show_wait_destroy("vertical", vertical)
    # [vert]

    # [smooth]
    # Inverse vertical image
    vertical = cv.bitwise_not(vertical)
    # show_wait_destroy("vertical_bit", vertical)

    '''
    Extract edges and smooth image according to the logic
    1. extract edges
    2. dilate(edges)
    3. src.copyTo(smooth)
    4. blur smooth img
    5. smooth.copyTo(src, edges)
    '''

    # Step 1
    edges = cv.adaptiveThreshold(vertical, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                cv.THRESH_BINARY, 3, -2)
    # show_wait_destroy("edges", edges)

    # Step 2
    kernel = np.ones((2, 2), np.uint8)
    edges = cv.dilate(edges, kernel)
    # show_wait_destroy("dilate", edges)

    # Step 3
    smooth = np.copy(vertical)

    # Step 4
    smooth = cv.blur(smooth, (2, 2))

    # Step 5
    (rows, cols) = np.where(edges != 0)
    vertical[rows, cols] = smooth[rows, cols]

    return vertical, horizontal