from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, FileResponse
from model import get_predict_image

import codecs

app = FastAPI()

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
    try:
        contents = file.file.read()
        with open("images/select_image.jpg", "wb") as f:
            f.write(contents)
        
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()   
    
    return get_predict_image("images/select_image.jpg")

@app.get("/images/select_image.jpg")
async def get_result_image():
    return FileResponse('images/select_image.jpg')

@app.get("/images/result_image.jpg")
async def get_result_image():
    return FileResponse('images/result_image.jpg')