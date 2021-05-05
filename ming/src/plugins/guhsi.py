from nonebot.adapters.cqhttp import Message
from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests
from nonebot.rule import to_me

twqh = on_command('诗词', rule=to_me(), priority=6)


@twqh.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    lovelive_send = await get_lovelive()
    await twqh.send(Message(lovelive_send))
    # await twqh.reject()

async def get_lovelive():
    url = 'http://xiaoapi.cn/api/tzgsc.php?id=1828222534&msg='
    hua = requests.get(url=url).text
    return hua


@twqh.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.get_message()).strip()
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@twqh.got("city", prompt="选择正确的答案序号哦！")
async def handle_city(bot: Bot, event: Event, state: dict):
    city = state["city"]
    city_weather = await gu(city)
    if city == "结束":
        await weather.finish('下次再来吧！嘿嘿！！')

    await twqh.send(city_weather)
    await twqh.send('如果不想玩了记得说”结束“哦！')
    await twqh.reject()  # 重复选


async def gu(city: str):
    ci = city
    url = 'http://xiaoapi.cn/api/tzgsc.php?id=1828222534&msg=' + ci
    re = requests.get(url=url).text
    return re
