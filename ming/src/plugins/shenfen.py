from nonebot import on_command, on_keyword
from nonebot.adapters.cqhttp import Bot, Event, Message
import requests, re
from nonebot.rule import to_me
weather = on_command("身份证查询", rule=to_me(),priority=5)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="请告诉我你的身份证，我会对你的身份证进行识别")
async def handle_city(bot: Bot, event: Event, state: dict):
    city = state["city"]
    city_weather = await get_weather(city)
    await weather.send(message=Message(city_weather))


async def get_weather(city: str):
    cityname = city
    url = 'http://api.yanxi520.cn/api/query.php?msg='+cityname
    d = requests.get(url=url, timeout=5).text
    return d
