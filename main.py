from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, FileResponse
import codecs

app = FastAPI()

@app.get("/")
def read_root():
    f=codecs.open("./pages/main.html", 'r')
    content = f.read()
    return HTMLResponse(content=content)

@app.get("/styles/main.css")
async def get_auth_style():
    return FileResponse('styles/main.css')

@app.post("/image")
def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open("uploaded_" + file.filename, "wb") as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
        

    return "Ok"