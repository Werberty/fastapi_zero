from http import HTTPStatus

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi_zero.schemas import Message

app = FastAPI(title='API do BETYM')


# Diretório contendo arquivos estáticos
app.mount(
    '/static', StaticFiles(directory='fastapi_zero/static'), name='static'
)

# Diretório contendo os templates Jinja
templates = Jinja2Templates(directory='fastapi_zero/templates')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}


@app.get('/{nome}', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_root_html(request: Request, nome: str):
    return templates.TemplateResponse(
        request=request, name='index.html', context={'nome': nome}
    )
