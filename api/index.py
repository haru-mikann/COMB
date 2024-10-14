from fastapi import FastAPI

# import os
# from dotenv import load_dotenv

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# load_dotenv()
# os.environ[""]

app = FastAPI()

@app.get("/")
async def root():
    logger.debug("hello:world")
    return [{"hello":"world"}]