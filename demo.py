# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import ch
# 避免 windows 下中文乱码
ch.utf8writer_register()

from gensim.models import word2vec
from gensim import models
import logging

def main():
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	
	# model = models.Word2Vec.load_word2vec_format('wiki.zh.model.bin',binary=True)
	model = word2vec.Word2Vec.load('wiki.zh.model')

	print("提供 3 种测试模式")
	print("输入一个词，则去寻找前二十个该词的相似词")
	print("输入两个词，则去计算两个词的余弦相似度")
	print("输入三个词，进行类比推理")

	while True:
		query = raw_input("请输入: ")
		query = query #.decode('utf-8')
		q_list = query.split()
		try:
			if len(q_list) == 1:
				print("相似词前 20 排序")
				res = model.most_similar(q_list[0], topn = 20)
				for item in res:
					print(item[0]+","+str(item[1]))

			elif len(q_list) == 2:
				print("计算 Cosine 相似度")
				res = model.similarity(q_list[0], q_list[1])
				print(res)
				
			else:
				print("%s之于%s，如%s之于" % (q_list[0], q_list[2], q_list[1]))
				res = model.most_similar([q_list[0], q_list[1]], [q_list[2]], topn = 20)
				for item in res:
					print(item[0]+","+str(item[1]))
					
			print("----------------------------")
		except Exception as e:
			print(repr(e))
		
		
if __name__ == "__main__":
	main()
