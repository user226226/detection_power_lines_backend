from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
import codecs

app = FastAPI()

@app.get("/")
async def read_root():
    f=codecs.open("./pages/main.html", 'r')
    content = f.read()
    return HTMLResponse(content=content)

@app.get("/styles/main.css")
async def get_auth_style():
    return FileResponse('styles/main.css')

@app.post("/image")
async def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open("images/result_image.jpg", "wb") as f:
            f.write(contents)
        with open("images/select_image.jpg", "wb") as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()    
    return "ok"

@app.get("/images/select_image.jpg")
async def get_result_image():
    return FileResponse('images/select_image.jpg')

@app.get("/images/result_image.jpg")
async def get_result_image():
    return FileResponse('images/result_image.jpg')