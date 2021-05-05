from nonebot import on_command,on_keyword
from nonebot.adapters.cqhttp import Bot, Event,Message
import requests
menu = on_keyword({'测试'})
@menu.handle()
async def h_r(bot: Bot, event: Event):
    msg = """
        机器人菜单 
       菜单：功能介绍
       1.今日人品：看看今天人品如何？
       2.涩图,壁纸，头像，美女，美腿，cos图，动漫,风景照,校花，二次元
       4.掏心语，社会语录，污话,骂我，祖安，随机一言,舔狗日记，骚话.土味情话，夸群主，调侃
       5.随机音乐,/铃声,/点歌,/酷狗点歌
       6./成语接龙，/新闻,/星座运势,/黄历，知乎日报，历史今天，每日一句
       7./天气（全国县级城市）
       8.语音(1,2,3,4,5,6 六种模式哦，试试吧！) 格式：/语音1
       9.(明星，网红，游戏，动物，风景)视频,/qq音乐视频
       10.翻译（支持14个国家语言） 格式：/翻译
       11.返回成员撤回的消息，欢迎信任进群，恭送退群，检测文件上传,匿名禁言,全员禁言（取消禁言），戳一戳送礼物等
       12.智能聊天，实现AI 格式：憨憨+你想说的话
       13./垃圾分类
       14./王者（所有英雄相关问题）
       16.诗词（题目），郭德纲语录,/诗歌（唐诗宋词啥都可）,笑话,网易云，谜语
       17./抖音 （查看任何抖音视频）
       18./搜狗百科，/百度百科
       19.填体温，全国疫情数据查询，/ip查询,/身份证查询
    
       """
    url='http://api.52guleng.cn/api/wzztp/api.php?s=325&ss=00A8FF&nr='+msg
    png=requests.get(url=url).text
    tu=f"[CQ:image,file={png}]"
    await menu.send(Message(tu))