from nonebot.adapters.cqhttp import Message
from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests
from aiocqhttp.exceptions import Error as CQHttpError

yulu = on_keyword({'掏心语'})


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    # bot = nonebot.get_bot()
    msg = await ji()
    try:
        await yulu.send(Message(str(msg)))

    except CQHttpError:
        pass


async def ji():
    url = 'https://api.66mz8.com/api/quotation.php?format=json'
    resp = requests.get(url)
    data = resp.json()
    content = data.get('quotation')
    return content


she = on_keyword({'社会'})


@she.handle()
async def s(bot: Bot, event: Event, state: T_State):
    mag = await hui()
    try:
        await she.send(Message(str(mag)))
    except CQHttpError:
        pass


async def hui():
    url = 'https://api.66mz8.com/api/social.php?format=json'
    r = requests.post(url)
    data = r.json()
    content = data.get('social')
    return content


she = on_keyword({'随机一言'})


@she.handle()
async def s(bot: Bot, event: Event, state: T_State):
    mag = await sui()
    try:
        await she.send(Message(str(mag)))
    except CQHttpError:
        pass


async def sui():
    url = 'http://api.ymong.top/api/yiyan.php'
    r = requests.post(url)
    return r.text


she = on_keyword({'舔狗日记'})


@she.handle()
async def s(bot: Bot, event: Event, state: T_State):
    mag = await tian()
    try:
        await she.send(Message(str(mag)))
    except CQHttpError:
        pass


async def tian():
    url = 'http://api.ymong.top/api/tiangou.php'
    r = requests.post(url)
    return r.text


she = on_keyword({'调侃'})


@she.handle()
async def s(bot: Bot, event: Event, state: T_State):
    mag = await kou()
    try:
        await she.send(Message(str(mag)))
    except CQHttpError:
        pass


async def kou():
    url = 'http://api.ymong.top/api/tiangou.php'
    r = requests.post(url)
    return r.text


she = on_keyword({'骚话'})


@she.handle()
async def s(bot: Bot, event: Event, state: T_State):
    mag = await sao()
    try:
        await she.send(Message(str(mag)))
    except CQHttpError:
        pass


async def sao():
    url = 'http://api.ymong.top/api/qinghua.php'
    r = requests.post(url)
    return r.text


twqh = on_keyword({'土味情话', '再来一句'})


@twqh.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    lovelive_send = await get_lovelive()
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await twqh.send(Message(lovelive_send))


async def get_lovelive():
    url = 'https://api.lovelive.tools/api/SweetNothings'
    hua = requests.get(url=url).text
    return hua


twqh = on_keyword({'谜语'})


@twqh.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    lovelive_send = await mi()
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await twqh.send(Message(lovelive_send))


async def mi():
    url = 'http://xiaoapi.cn/api/miyu.php'
    hua = requests.get(url=url).text
    return hua


twqh = on_keyword({'郭德纲'})


@twqh.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    lovelive_send = await de()
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await twqh.send(Message(lovelive_send))


async def de():
    url = 'http://api.clousx7.cn/api/gdg.php'
    hua = requests.get(url=url).text
    return hua


twqh = on_keyword({'笑话'})


@twqh.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    lovelive_send = await xi()
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await twqh.send(Message(lovelive_send))


async def xi():
    url = 'https://api.muxiaoguo.cn/api/xiaohua'
    hua = requests.get(url=url).json()
    # print(hua)
    data = hua["data"]["content"]
    # print(data)
    return data


twqh = on_keyword({'网易云'})


@twqh.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    lovelive_send = await yi()
    # at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await twqh.send(Message(lovelive_send))


async def yi():
    url = 'https://api.muxiaoguo.cn/api/163reping'
    hua = requests.get(url=url).json()
    # print(hua)
    data = hua["data"]["content"]
    # print(data)
    return data
