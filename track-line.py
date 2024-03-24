import cv2
import pytesseract

# Read the image
image = cv2.imread('Lar.png')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to convert the image to binary
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Use pytesseract to extract text from the binary image
custom_config = r'--oem 3 --psm 6'  # Configure OCR engine
numbers = pytesseract.image_to_string(thresh, config=custom_config)

# Print the extracted numbers
print("Extracted Numbers:", numbers)

# Display the image with detected numbers
cv2.imshow('Detected Numbers', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
