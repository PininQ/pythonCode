# -*- coding: utf-8 -*-
__author__ = 'QB'
import json
from multiprocessing.pool import Pool
from requests.exceptions import RequestException
import re
import urllib.request
'''
爬取猫眼电影 T100 的电影信息
'''

# 获取页面
def get_one_page(url):
    try:
        req = urllib.request.Request(url)
        req.add_header(
            'User-Agent',
            'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)'
        )
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        # response = requests.get(url, data={
        #     'User-Agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)'})
        if html is not None:
            return html
        return None
    except RequestException:
        return None


# 解析页面
def parse_on_page(html):
    pattern = re.compile(
        r'<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a' +
        '.*?">(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>' +
        '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


# 写入文件
def write_to_file(content):

    with open('result_new.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


# 配置启动函数
def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_on_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    # 多线程
    pool = Pool()
    pool.map(main, [i * 10 for i in range(10)])  # 前10页
