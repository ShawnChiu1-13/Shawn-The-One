import jieba     #导入jieba库，用于中文句子分词
import gensim    #导入gensim，用于计算文本相似度
import re        #使Python拥有全部的正则表达式的功能

# 获取指定路径的文件内容
def get_file_contents(path):
    string = ''
    f = open(path, 'r', encoding='UTF-8')
    line = f.readline()                  #该方法每次读出一行内容，所以，读取时占用内存小，比较适合大文件，该方法返回一个字符串对象。
    while line:
        string = string + line
        line = f.readline()
    f.close()
    return string                       #关闭文件，不能再进行读写操作

def filter(string):
    content = re.compile(u"[^a-zA-Z0-9\u4e00-\u9fa5]") #先将读取内容的标点符号、转义符号等去掉，
