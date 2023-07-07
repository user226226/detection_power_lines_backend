from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, FileResponse
from model import get_predict_image
from PIL import Image
from modelNew import LAPDetector
from numpy import asarray

import codecs

app = FastAPI()
detector = LAPDetector("weights/model.pt")

@app.get("/")
async def read_root():
    f=codecs.open("./pages/main.html", 'r', encoding="UTF-8")
    content = f.read()
    return HTMLResponse(content=content)

@app.get("/styles/main.css")
async def get_auth_style():
    return FileResponse('styles/main.css')

@app.post("/image")
async def upload(file: UploadFile = File(...)):
    path = "images/select_image.jpg"
    try:
        contents = file.file.read()
        with open(path, "wb") as f:
            f.write(contents)
        
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()   
    result = Image.fromarray(detector.predict(asarray(Image.open(path))))
    result.save("images/predict_image.jpg")
    return get_predict_image(path)

@app.get("/images/select_image.jpg")
async def get_result_image():
    return FileResponse('images/select_image.jpg')

@app.get("/images/result_image.jpg")
async def get_result_image():
    return FileResponse('images/result_image.jpg')