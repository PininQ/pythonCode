# -*- coding: utf-8 -*-
__author__ = 'QB'
import urllib.request
import re
'''
获取贴吧某一个帖子下的所有图片，并保存在 images 目录下。
'''

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header(
        'User-Agent',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)'
    )
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    return html


def get_img(html):
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)'
    imglist = re.findall(p, html)
    # for each in imglist:
    #     print(each)
    for each in imglist:
        filename = "images/%s" % each.split("/")[-1]
        urllib.request.urlretrieve(each, filename)


if __name__ == '__main__':
    url = 'https://tieba.baidu.com/p/5797176027'
    get_img(open_url(url))
