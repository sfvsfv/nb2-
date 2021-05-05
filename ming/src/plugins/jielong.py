from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event
import requests
from nonebot.rule import to_me
weather = on_command("成语接龙",rule=to_me(), priority=10)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="你先说成语，我来接，我很强的哦！！")
async def handle_city(bot: Bot, event: Event, state: dict):
    city = state["city"]
    city_weather = await get_weather(city)
    if city=="结束":
        await weather.finish('下次再来吧！嘿嘿！！')

    await weather.send(city_weather)
    await weather.send('如果不想玩了记得说”结束“哦！')
    await weather.reject()#重复选

async def get_weather(city: str):
    cityname = city
    url = 'http://apis.juhe.cn/idiomJie/query?key=a5883a782089d34b233de5c772bf800a&wd=%s&size=5&is_rand=1' % str(cityname)
    d = requests.get(url=url, timeout=5).json()
    data = d['result']['data'][0]
    return str(data)
