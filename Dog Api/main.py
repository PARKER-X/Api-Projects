from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import httpx

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    url = "https://dog.ceo/api/breeds/image/random"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        dog_data = response.json()
    return templates.TemplateResponse("index.html", {"request": request, "dog_image": dog_data["message"]})
