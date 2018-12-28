import numpy as np
import argparse
import random
import jieba
import qsresouce



#词向量字典模型建模

def read_vectors(path, topn, vectors):  # read top n word vectors
    lines_num =  0
    with open(path, encoding='utf-8', errors='ignore') as f:
        first_line = True
        for line in f:
            if first_line:
                first_line = False
                continue
            lines_num += 1
            tokens = line.rstrip().split(' ')
            vectors[tokens[0]] = np.asarray([float(x) for x in tokens[1:]])
            if topn != 0 and lines_num >= topn:
                break
    return 


#print('数据读取完成')

#将句子转化为向量
def sentence_vector(s,vectors):#该函数用于计算句子向量
        words = jieba.lcut(s.replace("能不能",""))
        v = np.zeros(300)
        for word in words:
            if word in ["告诉","你" , "请问" , "我" , "什么" , "是" ,"呀", "，","？","?",".","。",
            "可不可以","的","该","如何","进行","吗",
            "会","怎么办","到底","应该",
            "怎么","做","应该","这",
            "才能","达到","呢",
            "用来","可以","干","啥"]:
                 continue
            if word in vectors.keys():#如果表中有则加入
                v += vectors[word]
            else:
                for tmp in word:#如果表中没有则分成单个字后加入
                    if tmp in vectors.keys():
                        v+=vectors[tmp]
       # v /= len(words)，不需要，计算向量角度和向量的长度无关
        return v



#用于计算句子相似度，即输入两个句子计算其cos
def vector_similarity(s1, s2,vectors):
    v1, v2 = sentence_vector(s1,vectors), sentence_vector(s2,vectors)
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))





def similarityCheck(s,vectors,queList,ansList):
    finalsimiar=0 
    flag=0
    for index in range(len(queList)):
        tmpsimilar=vector_similarity(s,queList[index],vectors)
        if tmpsimilar>finalsimiar:
            finalsimiar=tmpsimilar
            flag=index
            answer=ansList[flag]
    if finalsimiar>0.7:
        return answer

