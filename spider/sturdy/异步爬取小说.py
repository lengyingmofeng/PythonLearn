# @作者 : 叶枫
# @文件 : 异步爬取小说.py 
# @时间 : 2021/10/26 17:37
# @版本 ：1.0
# @功能描述:
import json
import aiofiles
import requests
import asyncio
import aiohttp

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.81 Safari/537.36",
    # 防盗链： 溯源，当前本次请求的上一级是谁
    "Referer": "https://dushu.baidu.com/pc/reader?gid=4306063500&cid=11348571"
}


async def aio_download(cid, b_id, title):   # 下载小说
    data = {
        "book_id": f"{b_id}",
        "cid": f"{b_id}|{cid}",
        "need_bookinfo": 1
    }
    data = json.dumps(data)
    url = f"https://dushu.baidu.com/api/pc/getChapterContent?data={data}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            async with aiofiles.open("西游记/" + title + ".txt", "w", encoding='utf-8') as fp:
                await fp.write(dic['data']['novel']['content'])
            print(title, "over")


async def getCatalog(url):
    resp = requests.get(url, headers=headers)
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']:
        title = item['title']
        cid = item['cid']
        # 准备异步任务
        tasks.append(aio_download(cid, b_id, title))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    b_id = "4306063500"     # 百度小说的书籍id
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + b_id + '"}'
    asyncio.get_event_loop().run_until_complete(getCatalog(url))
