import unittest
import test_function  # 引用一下计算程序
from BeautifulReport import BeautifulReport

class TestForAllTextTfIdf(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("开始单元测试……")
    @classmethod
    def tearDown(self):
        print("已结束测试")

    def test_self_tfidf(self):
        print("正在载入orig.txt")
        test_function.solve(r'C:\Users\zmj\Desktop\测试文本2\orig.txt', r'C:\Users\zmj\Desktop\测试文本2\orig.txt', r'C:\Users\zmj\Desktop\z.txt')

    def test_add_tfidf(self):
        print("正在载入orig_0.8_add.txt")
        test_function.solve(r'C:\Users\zmj\Desktop\测试文本2\orig.txt',r'C:\Users\zmj\Desktop\测试文本2\orig_0.8_add.txt','C:\Users\zmj\Desktop\z.txt')

    def test_del_tfidf(self):
        print("正在载入orig_0.8_del.txt")
        test_function.solve(r'C:\Users\zmj\Desktop\测试文本2\orig.txt', r'C:\Users\zmj\Desktop\测试文本2\orig_0.8_del.txt', 'C:\Users\zmj\Desktop\z.txt')

    def test_dis_1_tfidf(self):
        print("正在载入orig_0.8_dis_1.txt")
        test_function.solve(r'C:\Users\zmj\Desktop\测试文本2\orig.txt', r'C:\Users\zmj\Desktop\测试文本2\orig_0.8_dis_1.txt', 'C:\Users\zmj\Desktop\z.txt')


    def test_dis_10_tfidf(self):
        print("正在载入orig_0.8_dis_10.txt")
        test_function.solve(r'C:\Users\zmj\Desktop\测试文本2\orig.txt', r'C:\Users\zmj\Desktop\测试文本2\orig_0.8_dis_10.txt', 'C:\Users\zmj\Desktop\z.txt')

    def test_dis_15_tfidf(self):
        print("正在载入orig_0.8_dis_15.txt")
        test_function.solve(r'C:\Users\zmj\Desktop\测试文本2\orig.txt', r'sim_0.8\orig_0.8_dis_15.txt', 'C:\Users\zmj\Desktop\z.txt')



if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestForAllTextTfIdf('test_self_tfidf'))
    suite.addTest(TestForAllTextTfIdf('test_add_tfidf'))
    suite.addTest(TestForAllTextTfIdf('test_del_tfidf'))
    suite.addTest(TestForAllTextTfIdf('test_dis_1_tfidf'))
    suite.addTest(TestForAllTextTfIdf('test_dis_10_tfidf'))
    suite.addTest(TestForAllTextTfIdf('test_dis_15_tfidf'))
    runner = BeautifulReport(suite)
    runner.report(
        description='论文查重测试报告',  # => 报告描述
        filename='nlp_TFIDF.html',  # => 生成的报告文件名
        log_path='.'  # => 报告路径
    )
