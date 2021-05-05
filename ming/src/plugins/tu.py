# from nonebot.adapters.cqhttp import Message
# from nonebot import on_keyword
# from nonebot.typing import T_State
# from nonebot.adapters import Bot, Event
# import requests
# from aiocqhttp.exceptions import Error as CQHttpError
#
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
#
#
# yulu = on_keyword({'美女'})
#
#
# @yulu.handle()
# async def j(bot: Bot, event: Event, state: T_State):
#     msg = await mei()
#     print(msg)
#     try:
#         await yulu.send(Message(msg))
#
#     except CQHttpError:
#         pass
#
#
# async def mei():
#     url = 'https://api.66mz8.com/api/rand.img.php?type=美女&format=json'
#     resp = requests.get(url)
#     data = resp.json()
#     ur = data.get('pic_url')
#     tu = f"[CQ:image,file={ur}]"
#     # tu=f"[CQ:cardimage,file={ur}]"
#     return tu
#
#
# yulu = on_keyword({'涩图', '妹子'})
#
#
# @yulu.handle()
# async def j(bot: Bot, event: Event, state: T_State):
#     msg = await nv()
#     print(msg)
#     try:
#         await yulu.send(Message(msg))
#
#     except CQHttpError:
#         pass
#
#
# async def nv():
#     url = 'https://api.66mz8.com/api/rand.acg.php?type=%E7%BE%8E%E5%A5%B3&format=json'
#     resp = requests.get(url)
#     data = resp.json()
#     ur = data.get('pic_url')
#     tu = f"[CQ:image,file={ur}]"
#     return tu
