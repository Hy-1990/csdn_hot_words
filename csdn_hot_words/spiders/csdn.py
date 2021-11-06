#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/5 23:47
# @Author  : 至尊宝
# @Site    : 
# @File    : csdn.py

import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from csdn_hot_words.items import CsdnHotWordsItem
from csdn_hot_words.tools.analyse_sentence import get_key_word


class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    # allowed_domains = ['blog.csdn.net']
    start_urls = ['https://blog.csdn.net/rank/list']

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 使用无头谷歌浏览器模式
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome(chrome_options=chrome_options,
                                        executable_path="E:\\chromedriver_win32\\chromedriver.exe")
        self.browser.set_page_load_timeout(30)

    def parse(self, response, **kwargs):
        titles = response.xpath("//div[@class='hosetitem-title']/a/text()")
        for x in titles:
            item = CsdnHotWordsItem()
            item['words'] = get_key_word(x.get())
            yield item
