from nonebot import on_command
from nonebot . adapters .cqhttp import Bot,Message,Event
from selenium import webdriver
import random
from nonebot.permission import *
from selenium.webdriver.chrome.options import Options
from nonebot.rule import to_me
from aiocqhttp.exceptions import Error as CQHttpError

t=on_command('填体温',rule=to_me(),permission=SUPERUSER,priority=99)
@t.handle()
async def tiantiwen(bot: Bot, event: Event):
    msg = await Y()
    msg1=await D()
    msg2=await L()
    try:
        await t.send(message=Message(str(msg)))
        await t.send(message=Message(str(msg1)))
        await t.send(message=Message(str(msg2)))
    except CQHttpError:
        pass

async def Y():
    result = str(random.uniform(36, 37))[0:4]
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    brower = webdriver.Chrome(executable_path=r'C:\Users\hp\Downloads\chromedriver.exe',
                              chrome_options=chrome_options)
    # 1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
    # 第一步：模拟网站登录
    # 打开浏览器
    # brower = webdriver.Chrome()
    brower.get(
        'https://web-vpn.sues.edu.cn/https/77726476706e69737468656265737421f3f652d234256d43300d8db9d6562d/cas/login?service=https%3A%2F%2Fweb-vpn.sues.edu.cn%2Flogin%3Fcas_login%3Dtrue')
    # ****** 替换成自己账号
    brower.find_element_by_id('username').send_keys('051719220')
    # ****** 替换成自己密码
    brower.find_element_by_id('password').send_keys('Zxcvbnm123')
    # 模拟登录
    brower.find_element_by_id('passbutton').click()
    # 第二步：模拟程序自动录入体温提交
    # 发送网络请求
    brower.get(
        'https://web-vpn.sues.edu.cn/https/77726476706e69737468656265737421e7f85397213c6747301b9ca98b1b26312700d3d1/default/work/shgcd/jkxxcj/jkxxcj.jsp')
    # 模拟鼠标滚动到页面底部
    brower.execute_script("var action=document.documentElement.scrollTop=2000")
    # 首先定位到input,清空输入框信息
    brower.find_element_by_xpath('//input[@placeholder="范围35.0-45.0"]').clear()
    # 将程序每次随机生成的体温，模拟输入到文本框
    brower.find_element_by_xpath('//input[@placeholder="范围35.0-45.0"]').send_keys(result)
    # 程序模拟点击提交
    brower.find_element_by_id('post').click()
    brower.find_element_by_xpath('//a[@class="layui-layer-btn0"]').click()
    print('Y 填报完毕')
    # 1秒之后关闭窗口
    brower.quit()
    # await t.send(Message('Y主人，体温填报完毕'))
    return '一号填报完成'
async def D():
    result1 = str(random.uniform(36, 37))[0:4]
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    brower = webdriver.Chrome(executable_path=r'C:\Users\hp\Downloads\chromedriver.exe',
                              chrome_options=chrome_options)
    # 1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
    # 第一步：模拟网站登录
    # 打开浏览器
    # brower = webdriver.Chrome()
    brower.get(
        'https://web-vpn.sues.edu.cn/https/77726476706e69737468656265737421f3f652d234256d43300d8db9d6562d/cas/login?service=https%3A%2F%2Fweb-vpn.sues.edu.cn%2Flogin%3Fcas_login%3Dtrue')
    # ****** 替换成自己账号
    brower.find_element_by_id('username').send_keys('151119102')
    # ****** 替换成自己密码
    brower.find_element_by_id('password').send_keys('Drt@3926')
    # 模拟登录
    brower.find_element_by_id('passbutton').click()
    # 第二步：模拟程序自动录入体温提交
    # 发送网络请求
    brower.get(
        'https://web-vpn.sues.edu.cn/https/77726476706e69737468656265737421e7f85397213c6747301b9ca98b1b26312700d3d1/default/work/shgcd/jkxxcj/jkxxcj.jsp')
    # 模拟鼠标滚动到页面底部
    brower.execute_script("var action=document.documentElement.scrollTop=2000")
    # 首先定位到input,清空输入框信息
    brower.find_element_by_xpath('//input[@placeholder="范围35.0-45.0"]').clear()
    # 将程序每次随机生成的体温，模拟输入到文本框
    brower.find_element_by_xpath('//input[@placeholder="范围35.0-45.0"]').send_keys(result1)
    # 程序模拟点击提交
    brower.find_element_by_id('post').click()
    brower.find_element_by_xpath('//a[@class="layui-layer-btn0"]').click()
    print('小邓  填报完毕')
    # 1秒之后关闭窗口
    # time.sleep(1)
    brower.quit()
    # await t.send(Message('D主人，体温填报完毕'))
    return '二号填报完成'
async def L():
    result2 = str(random.uniform(36, 37))[0:4]
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    brower = webdriver.Chrome(executable_path=r'C:\Users\hp\Downloads\chromedriver.exe',
                              chrome_options=chrome_options)
    # 1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
    # 第一步：模拟网站登录
    # 打开浏览器
    # brower = webdriver.Chrome()
    brower.get(
        'https://web-vpn.sues.edu.cn/https/77726476706e69737468656265737421f3f652d234256d43300d8db9d6562d/cas/login?service=https%3A%2F%2Fweb-vpn.sues.edu.cn%2Flogin%3Fcas_login%3Dtrue')
    # ****** 替换成自己账号
    brower.find_element_by_id('username').send_keys('151219121')
    # ****** 替换成自己密码
    brower.find_element_by_id('password').send_keys('W23Ch5a67H253R6')
    # 模拟登录
    brower.find_element_by_id('passbutton').click()
    # 第二步：模拟程序自动录入体温提交
    # 发送网络请求
    brower.get(
        'https://web-vpn.sues.edu.cn/https/77726476706e69737468656265737421e7f85397213c6747301b9ca98b1b26312700d3d1/default/work/shgcd/jkxxcj/jkxxcj.jsp')
    # 模拟鼠标滚动到页面底部
    brower.execute_script("var action=document.documentElement.scrollTop=2000")
    # 首先定位到input,清空输入框信息
    brower.find_element_by_xpath('//input[@placeholder="范围35.0-45.0"]').clear()
    # 将程序每次随机生成的体温，模拟输入到文本框
    brower.find_element_by_xpath('//input[@placeholder="范围35.0-45.0"]').send_keys(result2)
    # 程序模拟点击提交
    brower.find_element_by_id('post').click()
    brower.find_element_by_xpath('//a[@class="layui-layer-btn0"]').click()
    print('小刘  填报完毕')
    # 1秒之后关闭窗口
    brower.quit()
    # await t.send('L主人体温填报完毕')
    return '三号填报完成'