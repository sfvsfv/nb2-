from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event, Message
import requests, re, json

weather = on_command("快手",rule=to_me(), priority=5)


def get(url: str) -> dict:
    """
    title、imgs、videos
    """
    data = {}
    failed = {'msg': 'failed...'}
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25",
        "Cookie": "did=web_68e0268146694843a92700d2de49a0a6;"
    }
    # rewrite desktop url
    temp = re.findall(r'live\.kuaishou\.com/u/\w+/(\w+)', url)
    if temp:
        url = 'https://c.kuaishou.com/fw/photo/{}'.format(temp[0])

    rep = requests.get(url, headers=headers, timeout=10)
    if rep.status_code != 200:
        return failed

    page_data = re.findall(r'<script type="text/javascript">window\.pageData= (\{.*?\})</script>', rep.text)
    if not page_data:
        return failed

    try:
        page_data = json.loads(page_data[0])
    except Exception:
        print('kuaishou loads json failed')
        return failed

    video_info = page_data['video']
    data['title'] = video_info['caption']
    # 获取视频
    try:  # 如果出错，则可能是长图视频
        data['videos'] = [video_info['srcNoMark']]
    except Exception:
        pass
    else:
        data['videoName'] = data['title']
        data['msg'] = '如果快手视频下载出错请尝试更换网络'
    # 获取图片
    try:  # 如果出错，则可能是普通视频；
        images = video_info['images']
        imageCDN: str = video_info['imageCDN']
        # 如果是长图视频，则这几项一定存在
        assert images is not None
        assert imageCDN is not None
    except Exception:
        pass
    else:
        if not imageCDN.startswith('http'):
            imageCDN = 'http://' + imageCDN
        data['imgs'] = [imageCDN + i['path'] for i in images]
    return data

@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="请发送你要看的http://格式快手链接！")
async def handle_city(bot: Bot, event: Event, state: dict):
    city = state["city"]
    city_weather = await get_weather(city)
    await weather.send(Message(city_weather))


async def get_weather(city: str):
    urls = re.findall(
        r"https?://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]\.[-A-Za-z]+[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]",
        city)
    d = get(str(urls[0]))
    print(d)
    shi = d['videos'][0]
    pin = f"[CQ:video,file={shi}]"
    return pin
