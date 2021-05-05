from nonebot.adapters.cqhttp import Message
from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests, re
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot.rule import to_me
yulu = on_keyword({'网红视频'})


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    msg = await shi()
    try:
        await yulu.send(Message(msg))

    except CQHttpError:
        await yulu.send('视频加载失败')


async def shi():
    url = 'http://api.ymong.top/api/video.php?n=%E7%BD%91%E7%BA%A2'
    resp = requests.get(url).text
    bo = re.findall('播放链接：(.*)', resp)[0]
    co = re.findall('img=(.*)±', resp)[0]
    # print(bo)
    # print(co)
    shi = f"[CQ:video,file={bo},cover={co}]"
    return shi


yulu = on_keyword({'明星视频'})


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    # bot = nonebot.get_bot()
    await yulu.send('请稍等，正在努力寻找视频中，请稍等...')
    msg = await ming()
    try:
        await yulu.send(Message(msg))

    except CQHttpError:
        await yulu.send('视频加载失败')


async def ming():
    url = 'http://api.ymong.top/api/video.php?n=%E6%98%8E%E6%98%9F'
    resp = requests.get(url).text
    bo = re.findall('播放链接：(.*)', resp)[0]
    co = re.findall('img=(.*)±类型', resp)[0]
    # print(bo)
    # print(co)
    shi = f"[CQ:video,file={bo},cover={co}]"
    return shi




yulu = on_keyword({'喵喵视频'})


@yulu.handle()
async def j(bot: Bot, event: Event, state: T_State):
    await yulu.send('请稍等，正在努力寻找视频中，请稍等...')
    msg = await d()
    try:
        await yulu.send(Message(msg))

    except CQHttpError:
        await yulu.send('视频加载失败')

async def d():
    url = 'http://api.ymong.top/api/video.php?n=%E5%8A%A8%E7%89%A9'
    resp = requests.get(url).text
    bo = re.findall('播放链接：(.*)', resp)[0]
    co=re.findall('img=(.*)±',resp)[0]
    # print(bo)
    # print(co)
    shi = f"[CQ:video,file={bo},cover={co}]"
    return shi


ipname = on_command("腾讯视频",rule=to_me(), priority=5)


@ipname.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.get_message()).strip()
    if args:
        state["ipname"] = args


@ipname.got("ipname", prompt="你想查神马视频...")
async def handle_city(bot: Bot, event: Event, state: dict):
    ipinfo = state["ipname"]
    ip_info = await get_ipinfo(ipinfo)
    await ipname.send(Message(ip_info))


async def get_ipinfo(ipinfo: str):
    ip = ipinfo
    url = 'http://api.yanxi520.cn/api/txss.php?msg=' + ip
    response = requests.get(url).text
    ur = re.findall('地址:(.*)', response)[0]
    co=re.findall('图片:(.*)地址',response)[0]
    print(ur)
    # print(co)
    shi = f"[CQ:video,file={ur},cover={co}]"
    return shi
