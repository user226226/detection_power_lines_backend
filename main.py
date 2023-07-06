from typing import Union
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import codecs

app = FastAPI()


@app.get("/")
def read_root():
    f=codecs.open("index.html", 'r')
    content = f.read()
    return HTMLResponse(content=content)