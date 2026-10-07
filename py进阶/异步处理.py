import asyncio
import aiohttp # 支持异步网络请求
import re

PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')

# 声明协程函数：拥有暂停（挂起）和恢复执行的能力，并且改变它的调用规则（调用但不执行）
# 调用时返回协程对象，只有事件循环接手调度，才会真正执行
async def fetch_page(session, url):
    # with 确保请求结束后，网络连接会自动释放，不会导致资源泄露
    # async 声明异步：如果连接池已满，暂停（挂起），交还 CPU
    async with session.get(url, ssl = False) as resp:
        return await resp.text() # await 暂停（挂起），交还 CPU，等服务器发送完成 HTML 后，再恢复执行，返回网页文本

async def show_title(session, url):
    html = await fetch_page(session, url)
    print(PATTERN.search(html).group('title'))

async def main():
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    
    async with aiohttp.ClientSession() as session:
        '''
        ClientSession() 拥有 
        连接池（Connection Pool）：维持着多条 TCP 连接，随用随取
        + 记忆功能：自动帮你记住和发送 Cookie
        + 并发能力：并发处理多个 session.get()
        '''
        tasks = [show_title(session, url) for url in urls]
        # tasks 里面装的不是执行结果，而是 5 个未运行的协程对象。此时程序没有任何网络请求发出！
        await asyncio.gather(*tasks) # 接收协程对象，并提交给事件循环
        # await 指主协程（main）在这里暂停（挂起），直到这 5 个任务全部彻底完成，才会继续执行。
        # *tasks 解包
if __name__ == '__main__':
    asyncio.run(main()) # 启动事件循环    

'''
asyncio 的事件循环（Event Loop）本质上就是一个任务调度队列。
内部维护着就绪队列和等待队列。
当一个协程遇到 await 时，它就被扔进等待队列，而 CPU 则去就绪队列中找下一个任务跑
'''
    
    