# import cv2
# import numpy as np
# import easyocr
# reader = easyocr.Reader(['en'], gpu=False) # this needs to run only once to load the model into memory
#
#
#
#
# # Load image, grayscale, apply sharpening filter, Otsu's threshold
# image = cv2.imread('D:\infosys_intern\STMS\data\ss2.png')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# sharpen_kernel = np.array([[-1,-1,-1], [-1,10,-1], [-1,-1,-1]])
# sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
# thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
#
#
# cv2.imwrite('thresh_and_sharpen.png', thresh)
#
# # OCR
# result = reader.readtext(thresh, detail = 0)
#
# print(result)
#
# cv2.imshow('sharpen', sharpen)
# # cv2.imshow('thresh', thresh)
# cv2.waitKey()


import cv2
import numpy as np
import pytesseract

# Set path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\pardh\Tesseract-OCR\tesseract.exe"

# Load image, grayscale, apply sharpening filter, Otsu's threshold
image = cv2.imread('X:/Infosys_STMS/Smart_Traffic_Management_System/Output/Testing/noplate1.jpg')

if image is None:
    print("Error: Image not found!")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sharpen_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
    thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    # OCR
    data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 6')
    print(data)  # Uncomment this to see the OCR result

    cv2.imwrite('X:/Infosys_STMS/Smart_Traffic_Management_System/Output/Results/thresh_and_sharpen.png', thresh)

    # Show images
    cv2.imshow('sharpen', sharpen)
    cv2.imshow('thresh', thresh)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()  # Close all OpenCV windows
