# -*- coding: utf-8 -*-
import string

__author__ = 'wu'

import urllib2
import urllib
import re
import threading
import os
import time

from digg.models import Book

class Analyse_Url(threading.Thread):
    def __init__(self, page):
        threading.Thread.__init__(self)
        self.page = page

    def run(self):
        self.all_url = self.get_url(self.page)

        for tmpurl in self.all_url:
            content = urllib.urlopen(tmpurl).read().decode('utf-8')
            #content = urllib.urlopen("http://book.douban.com/subject/1230413/").read().decode('utf-8')

            self.author = ""
            self.translator = ""

            self.get_author(content)
            self.get_translator(content)
            self.pagenum = self.get_simple_info(content, "页数".decode('utf-8'))
            self.isbn = self.get_simple_info(content, "ISBN".decode('utf-8'))
            self.price = self.get_simple_info(content, "定价".decode('utf-8'))
            self.publisher = self.get_simple_info(content, "出版社".decode('utf-8'))
            self.publish_time = self.get_simple_info(content, "出版年".decode('utf-8'))
            self.zhuangzhen = self.get_simple_info(content, "装帧".decode('utf-8'))
            self.title = self.get_title(content)
            self.intro = self.get_intro(content)
            self.score = '0'

            self.pic = self.get_pic(content)
            self.pic_name_small = os.path.dirname(os.path.dirname(__file__)) + r"/digg/static/digg/mpic/" + self.isbn + r".jpg"
            self.pic_name_big = ""
            urllib.urlretrieve(self.pic, self.pic_name_small)

            p = Book(
                isbn= self.isbn,
                title=self.title,
                author=self.author,
                translator=self.translator,
                price=self.price,
                publisher=self.publisher,
                publish_time=self.publish_time,
                page_num=self.pagenum,
                zhuangzhen=self.zhuangzhen,
                introduct=self.intro,
                pic_name_big='',
                pic_name_small=r"/home/digg/static/digg/mpic/" + self.isbn + r".jpg",
                score=self.score
            )

            p.save()



    def get_url(self, page):
        #page = '40'
        top_url = "http://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start=page_num&type=T"
        top_url = re.sub('(page_num)', page, top_url)
        content = urllib.urlopen(top_url).read()
        many_url = re.compile(r'class="nbg" href="(.+)"')
        result = many_url.findall(content)
        return result


    def get_author(self, content):
        str1 = re.compile(ur'<span class="pl">([ ]?)作者([\s\S]+?)</span><br/>')
        tmp = str1.findall(content)

        str2 = re.compile(ur'<a([\s\S]+?)>([\s\S]+?)</a>')

        result = str2.findall(tmp[0][1])

        i = 0

        for tmp in result:
            self.author += tmp[1]
            i += 1
            if i >= len(result):
                break
            self.author += "/"



    def get_translator(self, content):
        str1 = re.compile(ur'<span class="pl">([ ]?)译者([\s\S]+?)</span><br/>')
        tmp = str1.findall(content)

        if not tmp:
            return ""

        str2 = re.compile(ur'<a([\s\S]+?)>([\s\S]+?)</a>')

        result = str2.findall(tmp[0][1])

        i = 0

        for tmp in result:
            self.translator += tmp[1]
            i += 1
            if i >= len(result):
                break
            self.translator += "/"


    def get_simple_info(self, content, arg):
        str1 = re.compile(ur'<span class="pl">([ ]?)%s([\s\S]+?)</span>([ ]?)([\s\S]+?)<br/>' % arg)
        tmp = str1.findall(content)
        if not tmp:
            return ""

        return str1.findall(content)[0][3]


    def get_title(self, content):
        str1 = re.compile(ur'<span property="v:itemreviewed">([\s\S]+?)</span>')
        return str1.findall(content)[0]


    def get_intro(self, content):
        str1 = re.compile(ur'<div class="intro">([\s\S]+?)</div>')
        tmp = str1.findall(content)

        if tmp[0].find("展开全部".decode('utf-8')) != -1 :
            tmp[1] = re.sub(r'(\n)', '', tmp[1])
            tmp[1] = re.sub(r'(<p>)', '  ', tmp[1])
            tmp[1] = re.sub(r'(</p>)', '\n', tmp[1])
            return tmp[1]
        else:
            tmp[0] = re.sub(r'(\n)', '', tmp[0])
            tmp[0] = re.sub(r'(<p>)', '  ', tmp[0])
            tmp[0] = re.sub(r'(</p>)', '\n', tmp[0])
            return tmp[0]


    def get_pic(self, content):
        str1 = re.compile(ur'<img src="([\s\S]+?)" title="点击看大图')
        return str1.findall(content)[0]

"""
    def run(self):
        author = re.compile('<span class="pl">([ ]?)作者([\s\S]+)<\/a>([\s\S]+)<span class="pl">([\s\S]?)出版社')
"""