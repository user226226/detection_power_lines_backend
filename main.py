from typing import Union
from fastapi import FastAPI, File, UploadFile
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
