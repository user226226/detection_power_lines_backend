import torch
import cv2
import numpy as np

class LAPDetector:
    def __init__(self, model_path):
        self.model = torch.hub.load('ultralytics/yolov5', 'custom',
                path=model_path, force_reload=True)
    

    def predict(self, image: np.ndarray):
        target_w = 832
        h, w, _ = image.shape
        scale_factor = target_w / w
        
        target_h = int(scale_factor * h)
        image = cv2.resize(image, (target_w, target_h))[:, :, ::-1]

        result = self.model(image)

        return result
