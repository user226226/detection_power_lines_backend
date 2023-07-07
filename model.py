from roboflow import Roboflow

def get_predict_image(path: str):
    rf = Roboflow(api_key="MvcIZgKbt2jU2rC8bRXy")
    project = rf.workspace().project("detection-power-lines")
    model = project.version(1).model

    result_model = model.predict(path, confidence=40, overlap=30)
    result_model.save("images/result_image.jpg")
    return result_model.json()