import cv2

# Read image
img = cv2.imread(r"C:\Users\sravy\Downloads\COMPUTER VISION\watch.jpg")

# Approximate coordinates of the watch
x = 95
y = 10
w = 285
h = 180

# Draw rectangle
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

# Display label
cv2.putText(img, "Watch", (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8, (0, 255, 0), 2)

# Show result
cv2.imshow("Detected Watch", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
