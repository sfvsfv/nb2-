from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event, Message
import requests, re
from nonebot.rule import to_me
weather = on_command("qq音乐视频", rule=to_me(),priority=5)


# weather=on_keyword({'天气'})
@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="你想看啥视频？")
async def handle_city(bot: Bot, event: Event, state: dict):
    city = state["city"]
    city_weather = await get_weather(city)
    # await bot.send(message='请稍等',event=)
    await weather.send(message=Message(city_weather))


async def get_weather(city: str):
    cityname = city
    url = 'http://xiaoapi.cn/api/dxmv.php?msg=%s&n=1' % cityname
    d = requests.get(url=url, timeout=5).text
    data = re.findall('播放链接：(.*)', d)[0]
    # tu=re.findall('图片：(.*)',d)[0]
    # print(data)
    shi = f"[CQ:video,file={data}]"
    # tu = f"[CQ:image,file={tu}]"
    return shi
