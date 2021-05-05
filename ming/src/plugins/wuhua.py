from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests
from aiocqhttp.exceptions import Error as CQHttpError

# @nonebot.scheduler.scheduled_job('cron', hour='1')
yulu = on_keyword({'污话', '甜话'})


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    # bot = nonebot.get_bot()
    msg = await ji()
    try:
        await yulu.send(message=str(msg))

    except CQHttpError:
        pass


async def ji():
    url = 'https://api.66mz8.com/api/sweet.php?format=json'
    resp = requests.get(url)
    data = resp.json()
    content = data.get('sweet')
    return content


yulu = on_keyword({'骂我', '祖安'})


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    # bot = nonebot.get_bot()
    msg = await ji()
    try:
        await yulu.send(message=str(msg))

    except CQHttpError:
        pass


async def ma():
    url = 'https://nmsl.shadiao.app/api.php?level=min&lang=zh_ch'
    resp = requests.get(url)
    return resp.text


yulu = on_keyword({'夸群主', '继续夸'})


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    # bot = nonebot.get_bot()
    msg = await kua()
    try:
        await yulu.send(message=str(msg))

    except CQHttpError:
        pass


async def kua():
    url = 'https://chp.shadiao.app/api.php'
    resp = requests.get(url)
    return resp.text


yulu = on_keyword({'毒鸡汤'})


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    # bot = nonebot.get_bot()
    msg = await kua()
    try:
        await yulu.send(message=str(msg))

    except CQHttpError:
        pass


async def du():
    url = 'https://du.shadiao.app/api.php'
    resp = requests.get(url)
    return resp.text


yulu = on_keyword({'文案'})


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    # bot = nonebot.get_bot()
    msg = await peng()
    try:
        await yulu.send(message=str(msg))

    except CQHttpError:
        pass


async def peng():
    url = 'https://pyq.shadiao.app/api.php'
    resp = requests.get(url)
    return resp.text
