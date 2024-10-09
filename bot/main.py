import os
from dotenv import load_dotenv
import discord
from module.weather import weather
from module.youtube import start_youtube_download
import requests
import logging

load_dotenv()


logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def get_gip_addr():
    #server の global IP Address を return
    res = requests.get("http://ipaddr.show")
    return res.text

@client.event
async def on_ready():
    logger.info('start discord bot')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    match message.content:
        case "?get_ip": 
            logger.info(f"command=?get_ip msg={get_gip_addr()}")
            await message.channel.send(get_gip_addr())
        case "?hello":
            logger.info("command=?hello msg=Hello!")
            await message.channel.send("Hello!")
        case "?tokyo_weather":
            logger.info(f"command=?tokyo_weather msg={weather('tokyo')}")
            await message.channel.send(weather("tokyo"))
        case "?aichi_weather":
            logger.info(f"command=?aichi_weather msg={weather('aichi')}")
            await message.channel.send(weather("aichi"))
        case "?help":
            logger.info("command=?help")
            await message.channel.send(
                "```\n"\
                "?get_ip: このサーバのglobal IPアドレスを返します。\n" \
                "?hello: return 'Hello!'\n" \
                "?tokyo_weather 東京都の天気を返します。\n" \
                "?aichi_weather 愛知県の天気を返します。\n" \
                "?yd_[https://www.youtubeから始まるURL]\n"
                "?help: return command list.\n"
                "```"
            )
    
    if message.content.startswith("?yd_https://www.youtube"):
        url = message.content[4:]
        logger.debug(f"url -> {url}")
        await message.channel.send(start_youtube_download(url))

client.run(os.environ["MUSIC_TOKEN"])