from nonebot.adapters.cqhttp import Message
from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests, re
from aiocqhttp.exceptions import Error as CQHttpError
import httpx
from nonebot.log import logger
da = on_keyword({'二次元'})

@da.handle()
async def j(bot: Bot, event: Event, state: T_State):
    msg = await ji()
    try:
        await da.send(Message(msg))
    except CQHttpError:
        pass


async def ji():
    url = 'http://api.ymong.top/api/acg.php'
    da = requests.get(url).text
    tu = f"[CQ:image,file={da}]"
    return tu


da = on_keyword({'美腿'})


@da.handle()
async def j(bot: Bot, event: Event, state: T_State):
    msg = await tui()
    try:
        await da.send(Message(msg))

    except CQHttpError:
        pass


async def tui():
    url = 'http://api.ymong.top/api/meitui.php'
    da = requests.get(url).text
    tu = f"[CQ:image,file={da}]"
    return tu


da = on_keyword({'cos'})


@da.handle()
async def j(bot: Bot, event: Event, state: T_State):
    msg = await co()
    try:
        await da.send(Message(msg))
    except CQHttpError:
        pass


async def co():
    url = 'http://api.ymong.top/api/cos.php'
    da = requests.get(url).text
    tu = f"[CQ:image,file={da}]"
    return tu


da = on_keyword({'星期'})


@da.handle()
async def j(bot: Bot, event: Event, state: T_State):
    msg = await xing()
    try:
        await da.send(Message(msg))

    except CQHttpError:
        pass


async def xing():
    url = 'http://api.ymong.top/api/dongshijie.php'
    # t=requests.get(url=url)
    tu = f"[CQ:image,file={url}]"
    return tu


da = on_keyword({'动漫'})


@da.handle()
async def j(bot: Bot, event: Event, state: T_State):
    # id = str(event.get_user_id())
    # xin = '帅哥，您要的动漫小姐姐马上就好了，希望你喜欢哦'
    # biaoqing = f"[CQ:face,id=6]"  # 表情包使用
    # await da.send(MessageSegment.at(id) + biaoqing + xin)
    msg = await d()
    try:
        await da.send(Message(msg))

    except CQHttpError:
        pass


async def d():
    url = 'http://api.ymong.top/api/wallpa.php?msg=2'
    resp = requests.get(url).text
    bo = re.findall('img=(.*)±', resp)[0]
    tu = f"[CQ:image,file={bo}]"
    return tu


da = on_keyword({'色图'})


@da.handle()
async def j(bot: Bot, event: Event, state: T_State):
    msg = await f()
    try:
        await da.send(Message(msg))

    except CQHttpError:
        pass


async def f():
    url = "https://api.lolicon.app/setu/?apikey=0961535560170e964e4689&r18=2&size1200=true"
    response = requests.get(url=url).json()
    print(response)
    url = response['data'][0]['url']
    print(url)
    tu = f"[CQ:image,file={url}]"
    return tu


setu = on_keyword({'壁纸'})

@setu.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    # at_ = "[CQ:at,qq={}]".format(event.get_user_id())
    async with httpx.AsyncClient() as client:
        resp = await client.get('https://api.mtyqx.cn/api/random.php?return=json')
        logger.debug(resp.json())
        imgurl = resp.json()['imgurl']
        cqimg = f"[CQ:image,file=1.{imgurl.split('.')[1]},url={imgurl}]"
        await setu.send(Message(cqimg))


da = on_keyword({'明星照'})


@da.handle()
async def j(bot: Bot, event: Event, state: T_State):
    try:
        await da.send(Message(msg))
    except CQHttpError:
        pass


async def m():
    url = 'http://api.ymong.top/api/wallpa.php?msg=9'
    resp = requests.get(url).text
    bo = re.findall('img=(.*)±', resp)[0]
    tu = f"[CQ:image,file={bo}]"
    return tu


da = on_keyword({'校花'})


@da.handle()
async def j(bot: Bot, event: Event, state: T_State):
    msg = await x()
    try:
        await da.send(Message(msg))

    except CQHttpError:
        pass


async def x():
    url = 'http://xiaoapi.cn/api/meinvtu.php?m=0'
    resp = requests.get(url).text
    bo = re.findall('img=(.*)±', resp)[0]
    tu = f"[CQ:image,file={bo}]"
    return tu


# yulu = on_keyword({'涩图'})
#
#
# @yulu.handle()
# async def j(bot: Bot, event: Event, state: T_State):
#     msg = await qian()
#     print(msg)
#     try:
#         await yulu.send(Message(msg))
#
#     except CQHttpError:
#         pass
#
#
# async def qian():
#     url = 'https://api.66mz8.com/api/rand.tbimg.php?format=json'
#     resp = requests.get(url)
#     data = resp.json()
#     ur = data.get('pic_url')
#     tu = f"[CQ:image,file={ur}]"
#     return tu


yulu = on_keyword({'美女'})
@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    msg = await mei()
    print(msg)
    try:
        await yulu.send(Message(msg))

    except CQHttpError:
        pass


async def mei():
    url = 'https://api.66mz8.com/api/rand.img.php?type=美女&format=json'
    resp = requests.get(url)
    data = resp.json()
    ur = data.get('pic_url')
    tu = f"[CQ:image,file={ur}]"
    # tu=f"[CQ:cardimage,file={ur}]"
    return tu


yulu = on_keyword({'涩图'})
@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    msg = await nv()
    # ms1=await z()
    # msg2=await qian()
    # print(msg)
    try:
        await yulu.send(Message(msg))
        # await yulu.send(Message(ms1))
        # await yulu.send(Message(msg2))
    except CQHttpError:
        pass


async def nv():
    url = 'https://api.66mz8.com/api/rand.acg.php?type=%E7%BE%8E%E5%A5%B3&format=json'
    resp = requests.get(url)
    data = resp.json()
    ur = data.get('pic_url')
    tu = f"[CQ:image,file={ur}]"
    return tu

# async def z():
#     url = "https://api.lolicon.app/setu/?apikey=0961535560170e964e4689&r18=2&size1200=true"
#     response = requests.get(url=url).json()
#     # print(response)
#     url = response['data'][0]['url']
#     print(url)
#     tu = f"[CQ:image,file={url}]"
#     return tu


# async def qian():
#     url = 'https://api.66mz8.com/api/rand.tbimg.php?format=json'
#     resp = requests.get(url)
#     data = resp.json()
#     ur = data.get('pic_url')
#     tu = f"[CQ:image,file={ur}]"
#     return tu