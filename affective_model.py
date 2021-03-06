import numpy as np
import sympy

#10个用户，5个产品和5个用户情感维度，随机生成0-10的整数
user_all = np.random.randint(0,10,size = [10,10])

user_emotion = user_all[...,:5] #截取前五列所有元素

user_rating = user_all[...,5:]

#print(user_all)
#print(user_emotion)
#print(user_rating)

def count_emtion_distance():
    #for user in np.nditer(array, flags = ["external_loop"],order = 'C'):
    #for emotion in user:
    #emotion_dis_array = []
    #采用二维数组索引情感距离
    emotion_dis_array = np.zeros([10,10],dtype = int)
    for i in range(0,9):
        ae = user_emotion[i,...]
        for j in range(i+1,9):
            be = user_emotion[j,...]
            dis0 = ae[0] - be[0]
            dis1 = ae[1] - be[1]
            dis2 = ae[2] - be[2]
            dis3 = ae[3] - be[3]
            dis4 = ae[4] - be[4]
            dis_all = abs(dis0) + abs(dis1) + abs(dis2) + abs(dis3) + abs(dis4)
            #emotion_dis_array.append(dis_all)
            emotion_dis_array[[i],[j]] = dis_all
    return emotion_dis_array
#print(count_emtion_distance())

def count_rating_distance():
    #rating_dis_array = []
    rating_dis_array = np.zeros([9,9],dtype = int)
    for i in range(0,9):
        ar = user_rating[i,...]
        for j in range(i+1,9):
            br = user_rating[j,...]
            dis0 = ar[0] - br[0]
            dis1 = ar[1] - br[1]
            dis2 = ar[2] - br[2]
            dis3 = ar[3] - br[3]
            dis4 = ar[4] - br[4]
            dis_all = abs(dis0) + abs(dis1) + abs(dis2) + abs(dis3) + abs(dis4)
            rating_dis_array[[i],[j]] = dis_all

    return rating_dis_array
print(count_rating_distance())


#使用sympy计算用户的和谐度

#用户a,b 的反馈和谐度
qa = sympy.symbols('q_A')
qb = sympy.symbols('q_B')
#用户a,b 的评分和谐度
ua = sympy.symbols('u_A')
ub = sympy.symbols('u_B')
#未知参数s
s = sympy.symbols('s')
#公式最终所求FC，用户a,b 的总体和谐度
FC = sympy.symbols('FC')
FC = 1 - sympy.sqrt(((qa-qb)**2 * (ua - ub)**2)/10**4 * s)


























