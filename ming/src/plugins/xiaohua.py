from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event
import requests
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot.rule import to_me
weather = on_command("新闻",rule=to_me(), priority=5)
# weather=on_keyword({'天气'})
from nonebot.adapters.cqhttp import Bot, Message


@weather.handle()
async def j(bot: Bot, event: Event):
    msg = await xin()
    print(msg)
    try:
        await weather.send(Message(msg))
    except CQHttpError:
        pass


async def xin():
    url = 'http://v.juhe.cn/toutiao/index?type=top&key=8e7ff44d3a5b8c13ebc1c8ce8a06a30f'
    d = requests.get(url=url).json()
    # print(d)
    b = "标题：" + d['result']['data'][0]['title']
    u = "网址：" + d['result']['data'][0]['url']
    b1 = "标题：" + d['result']['data'][1]['title']
    u1 = "网址：" + d['result']['data'][1]['url']
    b2 = "标题：" + d['result']['data'][2]['title']
    u2 = "网址：" + d['result']['data'][2]['url']
    b3 = "标题：" + d['result']['data'][3]['title']
    u3 = "网址：" + d['result']['data'][3]['url']
    return str(b + '\n' + u + '\n\n' + b1 + '\n' + u1 + '\n\n' + b2 + '\n' + u2 + '\n\n' + b3 + '\n' + u3)
