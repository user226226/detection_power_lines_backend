import torch
import cv2
import numpy as np
from PIL import Image

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
        tensors = result.xyxy[0]
        json = []
        for tensor in tensors:
            x_start = float(tensor[0])
            y_start = float(tensor[1])
            x_end = float(tensor[2])
            y_end = float(tensor[3])
            predict = float(tensor[4])
            width = x_end - x_start
            height = y_end - y_start
            path = f'images/predict_image_{x_start}{y_start}.jpg'
            result = Image.fromarray(result.render()[0])
            result.save(path)

            json.append({
            "x": x_start,
            "y": y_start,
            'width': width,
            'height': height,
            'predict': predict,
            'imageURL': path
        })
            
        return {'result': json}
