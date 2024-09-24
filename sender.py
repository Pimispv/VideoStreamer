import cv2
import zmq
import base64
import numpy as np

# Create ZMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://0.0.0.0:5555")  # Bind to all interfaces on port 5555

def send_video():
    """Sends video frames over ZMQ."""
    cap = cv2.VideoCapture(0)  # Change the index if needed (e.g., 1 for external webcam)
    
    if not cap.isOpened():
        print("Error: Could not open video source.")
        return
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Failed to read video frame.")
            break
        
        # Encode frame to JPEG format
        _, buffer = cv2.imencode('.jpg', frame)
        
        # Convert to base64 string
        jpg_as_text = base64.b64encode(buffer).decode('utf-8')
        
        # Send the base64 string over ZMQ
        socket.send_string(jpg_as_text)

        # Show the frame on the server side for reference
        cv2.imshow('Server', frame)
        
        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

def main():
    """Main function to run the video stream sender."""
    send_video()

if __name__ == "__main__":
    main()
