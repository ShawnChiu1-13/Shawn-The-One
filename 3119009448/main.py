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

#求相似度列表
    sim_value = []
    for i in range(0,len(sim_items)):
        sim_vec = dictionary.doc2bow(sim_items[i])
        sim = index[tf[sim_vec]]
    #取相似度最大的值
        sim_max = max(sim)
        sim_value.append(sim_max)
    return sim_value

#求每段话在文章中的权重
def get_weight(file_data,file_sentence):
    #权重列表
    weight = []
    #计算文章总字词长度
    file_len = 0
    #quanzhong用来留存每句话的权重
    quanzhong = 0
    for word in file_data:
        if '\u4e00'<=word<='\u9fff':
            file_len +=1
    for sentence in file_sentence:
        for word in sentence:
            if '\u4e00' <= word <= '\u9fff':
                quanzhong += 1
        weight.append(quanzhong/file_len)
        quanzhong = 0
    return weight

if __name__ == '__main__':
    #开始计时
    time_start = time.time()
    #打开原始文档
    path1 = sys.argv[1]    #原始文本路径
    path2 = sys.argv[2]    #相似文本路径
    path3 = sys.argv[3]    #存放答案文本路径
    orig_file = open(path1,'r', encoding='UTF-8')
    #打开相似文档
    similiar_file = open(path2,'r',encoding='utf-8')
    #原始文档写入
    orig_data = orig_file.read()
    #相似文档写入
    similiar_data = similiar_file.read()
    #关闭原始文档和相似文档
    orig_file.close()
    similiar_file.close()

    #对原始文档进行分句分词
    orig_sentence =creat_sentence(orig_data)
    orig_word = [[word for word in jieba.lcut(sentence)] for sentence in orig_sentence]
    #对相似文档进行分句分词
    similiar_sentence = creat_sentence(similiar_data)
    similiar_word = [[word for word in jieba.lcut(sentence)] for sentence in similiar_sentence]
    #获取相似文档的权重列表
    weight = get_weight(similiar_data,similiar_sentence)
    #获取相似文档相似度列表
    similiar_value = tfidf_model(orig_word,similiar_word)
    #total_similiarities用于存放最后总相似度，为每句权重和相似度的积
    total_similiarities = 0
    for i in range(len(weight)):
        total_similiarities += weight[i]*similiar_value[i]
    total_similiarities = (str("%.2f") % total_similiarities)
    print(total_similiarities)
    #将结果输出至指定文档
    file = open(path3,'w', encoding='UTF-8')
    file.write(total_similiarities)
    file.close()

    time_end = time.time()
    #得出耗时
    time = time_end-time_start
    print("time = ",time)
