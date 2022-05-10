from multiprocessing import context
from re import template
from fastapi import FastAPI,Request, From
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="/code")

@app.get("/")
def form_post(request: Request):
    return template.TemplateResponse('form.html', context={'request': request})
