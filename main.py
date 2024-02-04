import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, FileResponse
# from model import get_predict_image
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
    return detector.predict(asarray(Image.open(path)))

@app.get("/images/{image_name}")
async def get_result_image(image_name: str):
    return FileResponse(f'images/{image_name}')

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
