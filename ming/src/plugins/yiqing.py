from nonebot import on_command
from nonebot.adapters.cqhttp import Event
import requests
from nonebot.adapters.cqhttp import Bot, Message
from nonebot.rule import to_me
weather = on_command("疫情",rule=to_me(), priority=5)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="你想查询神马城市的疫情呀(@_@)仅限国内县城及以上哦...")
async def handle_city(bot: Bot, event: Event, state: dict):
    city = state["city"]
    city_weather = await xin(city)
    await weather.finish(city_weather)


async def xin(city: str):
    url = 'http://api.yanxi520.cn/api/virus.php?msg=' + city
    total = requests.get(url).text
    return total
