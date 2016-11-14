#!/usr/bin/env python
# encoding: utf-8

"""
@author: comwrg
@license: MIT
@file: qqMusicToKwl.py
@time: 2016/11/14 22:32
@desc: 将qq音乐歌单转换成酷我音乐的kwl格式,网易导入地址:http://music.163.com/#/import/kuwo
"""

import re
import urllib.request
from html import unescape


def getQQMusicList(url):
    '''
    获取QQMusic歌单信息
    :param url: https://y.qq.com/portal/playlist/3363492195.html#&dirid=201
    :return:[(歌名, 歌手, 专辑), ...]
    '''
    with urllib.request.urlopen(url) as r:
        html = r.read().decode('utf-8')
        # 反转义
        html = unescape(html)
        pattern = '<a href="javascript:;" title=".*">(.*)</a></span>\
[\s\S]*?<a href="javascript:;" title=".*" class="singer_name">(.*)</a>\
[\s\S]*?<a href="javascript:;" title=".*">(.*)</a>'
        mc = re.findall(pattern, html)
        #print(mc)
        return mc


def list2kwl(list):
    '''

    :param list:歌单信息,[(歌名, 歌手, 专辑), ...]
    :return:返回kwl格式文本,转换文件需要 gb2312 编码!!!
    '''
    kwl = ''
    for item in list:
        kwl += '    <so name="%s" artist="%s" album="%s"></so>\r\n' % (item[0], item[1], item[2])
    kwl = '<so>\r\n%s</so>' % kwl
    return kwl

l = getQQMusicList('https://y.qq.com/portal/playlist/3363492195.html#&dirid=201')
k = list2kwl(l)
print(k)

# 下面的errors='ignore'浪费了我至少半个小时,没有这个,转换会报错
with open('aaa.kwl', 'w', encoding='gb2312', errors='ignore') as f:
    f.write(k)
