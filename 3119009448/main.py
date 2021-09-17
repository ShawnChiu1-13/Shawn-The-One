import jieba
import re
from gensim import corpora
from gensim.similarities import Similarity
import gensim
import os
import sys
import time
#相比于上次修改更高校
#文档分句，删除符号，保留中文
def creat_sentence(file_data):
    file_sentence = []
    s = ''
    for word in file_data:
        #中文编码范围（引自网上）
        if '\u4e00'<=word<='\u9fff':
            s += word
        #逗号分句
        elif word == '，':
            file_sentence.append(s)
            s = ''
    return file_sentence


