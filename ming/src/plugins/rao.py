from nonebot.adapters.cqhttp import Message
from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests
from aiocqhttp.exceptions import Error as CQHttpError

rao = on_keyword({'绕口令'})
@rao.handle()
async def j(bot: Bot, event: Event, state: T_State):
    msg = await ji()
    try:
        await rao.send(message=Message(msg))

    except CQHttpError:
        pass


async def ji():
    url = 'http://ai.kenaisq.top/API/rkl.php'
    resp = requests.get(url).json()
    da=resp['text']
    return da