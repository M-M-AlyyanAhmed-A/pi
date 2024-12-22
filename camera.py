import cv2

class Camera:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def capture_frame(self):
        ret, frame = self.camera.read()
        if not ret:
            return None
        return frame

    def cleanup(self):
        self.camera.release()
