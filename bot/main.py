import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from module.weather import weather
import logging
import httpx
import requests

load_dotenv()


logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="?", intents=intents)

def get_gip_addr():
    #server の global IP Address を return
    res = requests.get("http://ipaddr.show")
    return res.text

@client.event
async def on_ready():
    logger.info('start discord bot')

@client.command()
async def get_ip(ctx):
    logger.info(f"command=?get_ip msg={get_gip_addr()}")
    await ctx.send(get_gip_addr())

@client.command()
async def hello(ctx):
    logger.info("command=?hello msg=Hello!")
    await ctx.send("Hello!")

@client.command()
async def tokyo_weather(ctx):
    logger.info(f"command=?tokyo_weather msg={weather('tokyo')}")
    await ctx.send(weather("tokyo"))

@client.command()
async def aichi_weather(ctx):
    logger.info(f"command=?aichi_weather msg={weather('aichi')}")
    await ctx.send(weather("aichi"))

@client.command()
async def helpme(ctx):
    logger.info("command=?help")
    await ctx.send(
        "```\n"\
        "?get_ip: このサーバのglobal IPアドレスを返します。\n" \
        "?hello: return 'Hello!'\n" \
        "?tokyo_weather 東京都の天気を返します。\n" \
        "?aichi_weather 愛知県の天気を返します。\n" \
        "?yd_[https://www.youtubeから始まるURL]\n"
        "?help: return command list.\n"
        "```"
    )

@client.event
async def on_message(message):
    if message.content.startswith("?yd_https://www.youtube"):
        url = message.content[4:]
        logger.debug(f"url -> {url}")
        common_phrase = os.environ["COMMON_PHRASE"]
        header = {"Authorization": f"Bearer {common_phrase}"}
        payload = {'videoURL': url}
        async with httpx.AsyncClient() as client:
            try:
                r = await client.post(os.environ["POST_TARGET"], headers=header, json=payload)
                logger.debug(f"POST status code: {r.status_code}")

                if r.status_code == 200:
                    await message.channel.send("Download request sent successfully.")
                else:
                    error_text = r.text
                    await message.channel.send(
                        f"Error occurred!\nStatus Code: {r.status_code}\nDetails: {error_text}"
                    )
            except Exception as e: # for unexpected error
                logger.error(f"Unexpected error: {e}")
                await message.channel.send(f"Unexpected error occurred: {str(e)}")

client.run(os.environ["MUSIC_TOKEN"])
