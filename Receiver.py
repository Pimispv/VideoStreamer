import cv2
import zmq
import base64
import numpy as np

def receive_video():
    """Receives video frames from the server and displays them."""
    
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://192.168.1.123:5555")   # Replace with the server's IP if different
    socket.setsockopt_string(zmq.SUBSCRIBE, '')  # Subscribe to all messages
    socket.RCVTIMEO = 5000  # Set a 5-second timeout for receiving data

    while True:
        try:
            # Receive the base64 encoded frame from the server
            data = socket.recv()
        except zmq.Again:
            print("Timeout! No data received within the time limit.")
            continue
        
        # Decode base64 back to binary
        try:
            jpg_as_bytes = base64.b64decode(data)
            jpg_as_np = np.frombuffer(jpg_as_bytes, dtype=np.uint8)
            frame = cv2.imdecode(jpg_as_np, cv2.IMREAD_COLOR)
            
            # Ensure the frame is decoded correctly before displaying
            if frame is not None:
                cv2.imshow('Client', frame)
            else:
                print("Error: Frame is None. Failed to decode.")
        except Exception as e:
            print(f"Error during decoding: {e}")
            continue
        
        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up
    cv2.destroyAllWindows()

def main():
    """Main function to start the video receiving process."""
    receive_video()

if __name__ == "__main__":
    main()
