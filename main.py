import time
import cv2
from camera import Camera
from models import ModelLoader
from arduino_comm import ArduinoComm
from detection_logic import is_dirt_detected, is_trash_detected

def main():
    # Initialize components
    camera = Camera()
    acin_model = ModelLoader("path/to/acin_model.tflite")
    trashnet_model = ModelLoader("path/to/trashnet_model.tflite")
    arduino = ArduinoComm(0x08)  # Arduino I2C address

    try:
        while True:
            # Capture frame
            frame = camera.capture_frame()
            if frame is None:
                print("Failed to capture frame.")
                continue

            # Run inference
            acin_output = acin_model.run_inference(frame)
            trashnet_output = trashnet_model.run_inference(frame)

            # Make decisions
            if is_dirt_detected(acin_output):
                print("Dirt detected, activating cleaning mechanism.")
                arduino.send_command(1)  # Command 1: Activate cleaning
            elif is_trash_detected(trashnet_output):
                print("Trash detected, initiating pickup.")
                arduino.send_command(2)  # Command 2: Trash pickup
            else:
                print("No dirt or trash detected, moving forward.")
                arduino.send_command(3)  # Command 3: Move forward

            # Debugging display
            cv2.imshow("Smart Cleaning Bot Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("Interrupted by user. Exiting...")
    finally:
        camera.cleanup()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
