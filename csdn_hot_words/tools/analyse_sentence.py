#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/5 23:47
# @Author  : 至尊宝
# @Site    : 
# @File    : analyse_sentence.py

import jieba.analyse


def get_key_word(sentence):
    result_dic = {}
    words_lis = jieba.analyse.extract_tags(
        sentence, topK=3, withWeight=True, allowPOS=())
    for word, flag in words_lis:
        if word in result_dic:
            result_dic[word] += 1
        else:
            result_dic[word] = 1
    return result_dic
