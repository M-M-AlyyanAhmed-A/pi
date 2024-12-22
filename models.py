import numpy as np
import cv2
import tflite_runtime.interpreter as tflite

class ModelLoader:
    def __init__(self, model_path):
        self.interpreter = tflite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

    def preprocess_frame(self, frame):
        target_shape = self.input_details[0]['shape'][1:3]
        resized_frame = cv2.resize(frame, target_shape)
        normalized_frame = resized_frame / 255.0
        return np.expand_dims(normalized_frame.astype(np.float32), axis=0)

    def run_inference(self, frame):
        input_tensor = self.preprocess_frame(frame)
        self.interpreter.set_tensor(self.input_details[0]['index'], input_tensor)
        self.interpreter.invoke()
        return self.interpreter.get_tensor(self.output_details[0]['index'])
