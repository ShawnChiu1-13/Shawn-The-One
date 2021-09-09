题目：论文查重

描述如下：

设计一个论文查重算法，给出一个原文文件和一个在这份原文上经过了增删改的抄袭版论文的文件，在答案文件中输出其重复率。

原文示例：今天是星期天，天气晴，今天晚上我要去看电影。
抄袭版示例：今天是周天，天气晴朗，我晚上要去看电影。
要求输入输出采用文件输入输出，规范如下：

从命令行参数给出：论文原文的文件的绝对路径。
从命令行参数给出：抄袭版论文的文件的绝对路径。
从命令行参数给出：输出的答案文件的绝对路径。
我们提供一份样例，课堂上下发，上传到班级群，使用方法是：orig.txt是原文，其他orig_add.txt等均为抄袭版论文。

注意：答案文件中输出的答案为浮点型，精确到小数点后两位

补充一下第一次尝试的过程
我先是在CSDN上查阅了一些判定相似度的算法资料

1.
defi compare(file1,file2):

lines1= readLines(file1) lines2 readlines(file2)

count =0.

for line in lines1:

if lines2.count line)>0

count +=1

return count / max(len(lines1)，len(lines2))

这样的结果是查重率高得离谱，果断放弃。

2.
然后网上资料显示，Python有自带的查重函数difflib

import difflib

def string similar(s1,s2):

return difflib.sequenceMatcher(None，s1,s2).quick_ratio() 
for i in range(len(data4_message)):

s1 data4 message[i]

s2= data4 answer[i]

print(string_similar(s1，s2))

