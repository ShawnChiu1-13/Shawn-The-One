import jieba
import re
from gensim import corpora
from gensim.similarities import Similarity
import gensim
import os
import sys
import time

#相比于上次修改更高效
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

def tfidf_model(items,sim_items):
    #生成词典
    dictionary = corpora.Dictionary(items)
    #生成稀疏向量库
    corpus = [dictionary.doc2bow(text) for text in items]
    #利用TFIDF模型建模
    tf = models.TfidfModel(corpus)
    #通过token2id得到特征数（字典里面的键的个数）
    num_features = len(dictionary.token2id.keys())
    #建立索引
    index = similarities.MatrixSimilarity(tf[corpus],num_features=num_features)
    #索引持久性
    index.save('index.txt')


