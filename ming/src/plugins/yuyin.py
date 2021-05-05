from nonebot.adapters.cqhttp import Message
from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests
from nonebot.rule import to_me
test = on_command('语音1',rule=to_me(),priority=5)


@test.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    # id = str(event.get_user_id())
    ms = await hui()
    chuo = f"[CQ:tts,text={ms}]"
    await test.send(Message(chuo))


async def hui():
    url = 'https://api.66mz8.com/api/social.php?format=json'
    r = requests.post(url)
    data = r.json()
    content = data.get('social')
    return content


test = on_command('语音2',rule=to_me(),priority=5)


@test.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    # id = str(event.get_user_id())
    ms = await kou()
    chuo = f"[CQ:tts,text={ms}]"
    await test.send(Message(chuo))


async def kou():
    url = 'http://api.ymong.top/api/tiangou.php'
    r = requests.post(url)
    return r.text


test = on_command('语音3',rule=to_me(),priority=5)


@test.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    # id = str(event.get_user_id())
    ms = await tian()
    chuo = f"[CQ:tts,text={ms}]"
    await test.send(Message(chuo))


async def tian():
    url = 'http://api.ymong.top/api/tiangou.php'
    r = requests.post(url)
    return r.text


test = on_command('语音4',rule=to_me(),priority=5)


@test.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    # id = str(event.get_user_id())
    ms = await kua()
    chuo = f"[CQ:tts,text={ms}]"
    await test.send(Message(chuo))


async def kua():
    url = 'https://chp.shadiao.app/api.php'
    resp = requests.get(url)
    return resp.text


test = on_command('语音5',rule=to_me(),priority=5)


@test.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    # id = str(event.get_user_id())
    ms = await kua()
    chuo = f"[CQ:tts,text={ms}]"
    await test.send(Message(chuo))


test = on_command('语音6',rule=to_me(),priority=5)


@test.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    # id = str(event.get_user_id())
    ms = await ma()
    chuo = f"[CQ:tts,text={ms}]"
    await test.send(Message(chuo))


async def ma():
    url = 'https://nmsl.shadiao.app/api.php?level=min&lang=zh_ch'
    resp = requests.get(url)
    return resp.text
