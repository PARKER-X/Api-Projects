# {e0a8f641eec576db55848eb85593028a}
# main.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import aiohttp

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_weather(request: Request):
    #API KEY
    api_key = "e0a8f641eec576db55848eb85593028a"

    # API URL
    
    url = f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={api_key}"
    print(url)

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            print(data)

    # Extract weather information from the response
    temperature = data["weather"]
   
    # Render the HTML template with weather data
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "temperature": temperature},
    )
