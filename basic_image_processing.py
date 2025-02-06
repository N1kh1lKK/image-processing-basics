import cv2

# Load an image
image = cv2.imread("/images/image1")  # Make sure you have an image in the same directory

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Show images
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
