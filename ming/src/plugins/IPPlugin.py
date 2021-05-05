from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event
import requests
from nonebot.rule import to_me
ipname = on_command("ip", rule=to_me(),priority=5)


@ipname.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.get_message()).strip()
    if args:
        state["ipname"] = args


@ipname.got("ipname", prompt="你想查神马...")
async def handle_city(bot: Bot, event: Event, state: dict):
    ipinfo = state["ipname"]
    ip_info = await get_ipinfo(ipinfo)
    await ipname.finish(ip_info)


async def get_ipinfo(ipinfo: str):
    ip = ipinfo
    url = 'http://ip-api.com/json/' + ip
    response = requests.get(url)
    strpp = {}
    strpp = response.json()
    try:
        return f'IP : ' + strpp['query'] + '\nContry : ' + strpp['country'] + '\nProvince : ' + strpp[
            'regionName'] + '\nCity : ' + strpp['city'] + '\nLongitude : ' + str(strpp['lon']) + '\nLatitude : ' + str(
            strpp['lat']) + '\nISP : ' + strpp['isp'] + '\nORG : ' + strpp['org']
    except Exception as e:
        return f"你的IP地址输入有误：{e}"
