from roboflow import Roboflow
rf = Roboflow(api_key="MvcIZgKbt2jU2rC8bRXy")
project = rf.workspace().project("detection-power-lines")
model = project.version(1).model

# infer on a local image
print(model.predict("images/image.jpg", confidence=40, overlap=30).json())

# visualize your prediction
model.predict("images/image.jpg", confidence=40, overlap=30).save("images/prediction.jpg")