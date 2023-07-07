from roboflow import Roboflow

rf = Roboflow(api_key="MvcIZgKbt2jU2rC8bRXy")
project = rf.workspace().project("detection-power-lines")
model = project.version(1).model

def get_predict_image(path: str):
    result_model = model.predict(path, confidence=40, overlap=30)
    result_model.save("images/predict_image_roboflow.jpg")
    return result_model.json()