from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event, Message,MessageSegment
import requests
from aiocqhttp.exceptions import Error as CQHttpError
weather = on_command("搜图", priority=5)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="搜什么图呢？")
async def handle_city(bot: Bot, event: Event, state: dict):
    city = state["city"]
    cityname = city
    url = 'http://api.yanxi520.cn/api/baich.php?msg=' + cityname
    d = requests.get(url=url).text
    try:
        await weather.send(MessageSegment.image(d))
    except CQHttpError:
        await weather.send('加载失败')

