# @作者 : 叶枫
# @文件 : xpath基础.py 
# @时间 : 2020/11/28 17:46 
# @版本 ：1.0
# @功能描述:
from lxml import etree
if __name__ == '__main__':
    parser = etree.HTMLParser(encoding="utf8")
    htmlelement = etree.parse("bilibli.html", parser=parser)
    r = htmlelement.xpath("//div//text()")[20]
    print(r)