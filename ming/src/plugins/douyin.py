from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event, Message
import requests, re
from nonebot.rule import to_me
weather = on_command("抖音",rule=to_me(), priority=7)
# def get(share_url) -> dict:
#     """
#     author, title, audioName, audios, videoName, videos
#     """
#     data = {}
#     headers = {
#         'accept': 'application/json',
#         'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
#     }
#     api = "https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={item_id}"
#
#     rep = requests.get(share_url, headers=headers, timeout=10)
#     if rep.ok:
#         # item_id
#         item_id = re.findall(r'video/(\d+)', rep.url)
#         if item_id:
#             item_id = item_id[0]
#             # video info
#             rep = requests.get(api.format(item_id=item_id), headers=headers, timeout=10)
#             if rep.ok and rep.json()["status_code"] == 0:
#                 info = rep.json()["item_list"][0]
#
#                 data["author"] = info["author"]["nickname"]
#                 data["title"] = data["videoName"] = info["desc"]
#                 if info.get('music'):
#                     data["audioName"] = info["music"]["title"]
#                     data["audios"] = [info["music"]["play_url"]["uri"]]
#                 # data["imgs"] = [info["video"]["origin_cover"]["url_list"][0]]
#
#                 # playwm_url -> play_url
#                 play_url = info["video"]["play_addr"]["url_list"][0].replace('playwm', 'play')
#                 data["videos"] = play_url
#                 return data
#     return {'msg': '获取失败'}


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.get_message()).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="请发送抖音链接，小可爱！")
async def handle_city(bot: Bot, event: Event, state: dict):
    city = state["city"]
    city_weather = await get_weather(city)
    await weather.send(Message(city_weather))


async def get_weather(city: str):
    urls = re.findall(
        r"https?://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]\.[-A-Za-z]+[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]",
        city)
    # 这是第三方的抖音视频api
    url = 'https://tenapi.cn/douyin/?url=' + str(urls[0])
    print(url)
    d = requests.get(url=url).json()
    shi = d['url']
    co=d['cover']
    print(shi)
    pin = f"[CQ:video,file={shi},cover={co}]"
    return pin
