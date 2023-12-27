import requests
import os, time
from lxml import etree
from multiprocessing.dummy import Pool
from uuid import uuid4

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63",
}
# 爬到的每个链接
htmls = []


def Parsing_html(url):
    res = requests.get(url=url, headers=headers)
    parsing_tree = etree.HTML(res.text)
    html_list = parsing_tree.xpath('//*[@id="main-content"]/div[1]/div[2]/article/h2/a/@href')
    for html in html_list:
        htmls.append(html)


# 最后的url
imgs = []


def Parsing_imgurl(imgurl):
    res = requests.get(url=imgurl, headers=headers)
    parsing_tree = etree.HTML(res.text)
    img_list = parsing_tree.xpath('//*[@id="the-post"]/div/div[2]/p/img/@src')
    # name_list = parsing_tree.xpath('//*[@id="the-post"]/div/div[2]/p/text()')
    # 遍历列表
    for img in img_list:
        imgs.append(img)


def Parsing_data(uurl):
    print('图片{}正在下载...'.format(uuid4()))
    data = requests.get(url=uurl, headers=headers).content
    try:
        # 下载位置
        root = 'E://acg17图库//'
        # 创建文件夹
        if not os.path.exists(root):
            os.mkdir(root)
        with open('{}{}.jpg'.format(root, uuid4()), 'wb') as f:
            f.write(data)
            print('图片{}下载成功'.format(uuid4()))
    except:
        pass


if __name__ == '__main__':
    # 要爬取的网址
    for page in range(1, 3):
        acg_urls = ['http://acg17.com/category/meitu/pixiv-painter/page/{}/'.format(page),
                    'http://acg17.com/category/meitu/pixiv-wallpaper/page/{}/'.format(page), ]
        print(acg_urls)
        # 创建进程池
        pool = Pool(8)
        # 第一次爬取到每个页面链接
        pool.map(Parsing_html, acg_urls)
        # 第二次爬取到每个图片链接
        pool.map(Parsing_imgurl, htmls)
        # 去重
        imglists = list(set(imgs))
        imglists.remove('https://tva2.sinaimg.cn/large/8a1c233bgw1fb6l0gxjk0j20cs077dgj.jpg')
        # 第三次保存图片
        start = time.time()
        pool.map(Parsing_data, imglists)
        end = time.time() - start
        print('消耗时间为:', end)
        # 关闭进程池
        pool.close()
        # 等待所有子进程执行完成。
        pool.join()
