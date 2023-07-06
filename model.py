from roboflow import Roboflow
rf = Roboflow(api_key="MvcIZgKbt2jU2rC8bRXy")
project = rf.workspace().project("detection-power-lines")
model = project.version(1).model

# infer on a local image
print(model.predict("images/image.jpg", confidence=40, overlap=30).json())

# visualize your prediction
model.predict("images/image.jpg", confidence=40, overlap=30).save("images/prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())