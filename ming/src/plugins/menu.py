from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters import Event
from nonebot.adapters.cqhttp import Bot, Message

menu = on_keyword({'菜单'})

@menu.handle()
async def h_r(bot: Bot, event: Event, state: T_State):
    msg = """
                娱乐功能
    1.今日人品， 成语接龙，新闻,星座运势,黄历，知乎日报，历史今天，每日一句，绕口令
    2.涩图,色图，头像，美女，美腿，cos，动漫,校花，举牌
    3.掏心语，社会语录，污话,骂我，祖安，随机一言,舔狗日记，骚话.土味情话，夸群主，调侃,郭德纲语录,诗歌,笑话,网易云，谜语
    4.随机音乐,铃声,点歌,听歌,王者（英雄相关问题）,今日哔哩排行,哔哩热搜，微博热搜
    6.语音(1,2,3,4,5,6 六种模式哦，试试吧！) 
    7.喵喵视频，明星视频，网红视频，抖音，快手
    8.搜狗百科,ip查询
            实用功能
    1.填体温   2.翻译  3.天气      4.分类（垃圾哈，也可以问非垃圾hh）
    5.疫情     6.身份证查询
            群管功能
    1.返回成员撤回的消息  
    2.欢迎信任进群，恭送退群 
    3.检测文件上传
    4.匿名禁言          
    5.全员禁言（取消禁言）    
    6.获取群文件信息  
    7.不良语言广告撤回并禁言
                问答系统
    添加格式：（模糊/全局）问xx答yy,最好在前面加一下模糊更好
    删除格式：删除词条xx
    加入后就会保存，下次自动回答相关问题
    
    """

    id = str(event.get_user_id())
    # yuyin=f"[CQ:record,file=http://baidu.com/1.mp3]"
    # biaoqing=f"[CQ:face,id=123]"#表情包使用
    at_ = f"[CQ:at,qq={id}]"  # 艾特好友使用
    await menu.send(Message(at_ + msg))  # 发送消息使用
