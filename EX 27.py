import cv2

def detect_faces(image_path):
    # Load the pre-trained Haar Cascade classifier
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # Read the image
    image = cv2.imread(image_path)

    # Check if the image is loaded
    if image is None:
        print("Error: Image not found!")
        return

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    print("Number of faces detected:", len(faces))

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the output
    cv2.imshow("Face Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Example usage
detect_faces(r"C:\Users\sravy\Downloads\COMPUTER VISION\FACE_IMAGE.jpg")
