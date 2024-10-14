from fastapi import FastAPI
import logging 

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()


@app.get("/")
async def root():
    logger.debug("Hello World")
    return [{"hello":"world"}]