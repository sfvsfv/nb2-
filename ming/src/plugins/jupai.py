from nonebot.adapters.cqhttp import Message
from nonebot import on_keyword, on_command
from nonebot.adapters import Bot, Event
import requests
from nonebot.rule import to_me
ipname = on_command("举牌", rule=to_me(),priority=5)


@ipname.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.get_message()).strip()
    if args:
        state["ipname"] = args


@ipname.got("ipname", prompt="你想举牌神马内容呀...")
async def handle_city(bot: Bot, event: Event, state: dict):
    ipinfo = state["ipname"]
    ip_info = await get_ipinfo(ipinfo)
    await ipname.send(Message(ip_info))

async def get_ipinfo(ipinfo: str):
    ip = ipinfo
    url = 'http://www.crys.top/api/acard.php?msg=' + ip
    re = requests.get(url).text
    tu = f"[CQ:image,file={re}]"
    return tu
