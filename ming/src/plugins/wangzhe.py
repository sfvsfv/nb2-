from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event
import requests, re
from nonebot.rule import to_me
weather = on_command("王者",rule=to_me(), priority=5)


# weather=on_keyword({'天气'})
@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="你想查询王者哪位英雄的相关问题")
async def handle_city(bot: Bot, event: Event, state: dict):
    city = state["city"]
    city_weather = await get_weather(city)
    await weather.finish(city_weather)


async def get_weather(city: str):
    cityname = city
    # print(cityname)
    url = 'http://xiaoapi.cn/api/wzry.php?msg=' + cityname
    d = requests.get(url=url, timeout=5).text
    tu = re.findall("(.*)发送", d)[0]
    return str(tu)
