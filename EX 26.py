import cv2

def reverse_video(input_video_path, output_video_path):
    # Open the input video
    cap = cv2.VideoCapture(input_video_path)

    # Check if the video is opened successfully
    if not cap.isOpened():
        print("Error: Could not open input video.")
        return

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Define codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps,
                          (frame_width, frame_height))

    # Read all frames
    frames = []

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    # Release the input video
    cap.release()

    # Reverse the frames
    frames.reverse()

    # Write reversed frames to output video
    for frame in frames:
        out.write(frame)

    # Release output video
    out.release()

    print("Reversed video saved successfully!")
    print("Output File:", output_video_path)


# ------------------------------
# Example Usage
# ------------------------------

input_path = r"C:\Users\sravy\Videos\Screen Recordings\Screen Recording 2025-11-26 112601.mp4"

output_path = r"C:\Users\sravy\Videos\Screen Recordings\output2_reversed.mp4"

reverse_video(input_path, output_path)
