import random
import time
from collections import Counter
start=time.time()

holy_num=list(range(1,46))

#기존 숫자별 가중치
# weight=[17883,25967,25123,26088,26365,30368,20443,32463,30563
# ,49863,35766,43850,43006,43971,44248,48251,38326,50346,48446,57947,43850
# ,51934,51090,52055,52332,56335,46410,58430,56530,57103,43006,51090,50246
# ,51211,51488,55491,45566,57586,55686,58068,43971,52055,51211,52176,52453]

#최대치에서 각 값 빼준 뒤 그 차이를 줄이는 방식(나누기 5000)
weight=[58422,58424,58423,58424,58424,58424,58422,58425,58424,58428,58425,58427
,58427,58427,58427,58428,58426,58428,58428,58430,58427,58429,58429,58429,58429
,58430,58428,58430,58430,58430,58427,58429,58428,58429,58429,58429,58427,58430
,58429,58430,58427,58429,58429,58429,58429]

def get_count(x):
    gc_list={}
    for i in x:
        try: gc_list[i]+=1
        except: gc_list[i]=1
    return gc_list

count=0
while True:
    c=0
    winner=[]

    while c<=5:
        new_list={}
        num=0
        while num<1000:
            a1=sorted(random.choices(holy_num,weight,k=6))
            for i in a1:
                try: new_list[i]+=1
                except: new_list[i]=1
            num+=1
            #print(a1)

        result=dict(sorted(new_list.items(), key=lambda x : x[1], reverse=True))

        aa = []
        for key in result:
            aa.append(key)
        winner.append(aa[0:6])
        c+=1

    a1 = sorted(winner[0])
    a2 = sorted(winner[1])
    a3 = sorted(winner[2])
    a4 = sorted(winner[3])
    a5 = sorted(winner[4])

    num = a1 + a2 + a3 + a4 + a5
    d1 = get_count(num)

    a = [0] * 10
    for key, value in d1.items():
        if value > 1:
            a[value] += 1
    print(a)
    count+=1
    if a[2] == 3 and a[3] <= 0 and a[4] == 0 and a[5]==0:
        break

#중복 번호 리스트
overlap=[]
for key,value in d1.items():
    if value>=2:
        overlap.append(key)

a1_overlap=len(list(set(a1).intersection(overlap)))
a2_overlap=len(list(set(a2).intersection(overlap)))
a3_overlap=len(list(set(a3).intersection(overlap)))
a4_overlap=len(list(set(a4).intersection(overlap)))
a5_overlap=len(list(set(a5).intersection(overlap)))


print('-'*30)
print(f'돌린 횟수: {count}')
print(f'걸린 시간: {round(time.time()-start,3)}초')
print('-'*30)
b = [0] * 5
for i in range(5):
    if a[i] != 0:
        b[i] += a[i]
        print(f'{i}번 나온 숫자가 총 {a[i]}개')
print('-'*30)
print(f'중복 숫자: {overlap}')
print('-'*30)
print('가중치 모델')
print('-'*30)
print(f'#1 {a1},{a1_overlap}',f'#2 {a2},{a2_overlap}',f'#3 {a3},{a3_overlap}' \
      ,f'#4 {a4},{a4_overlap}',f'#5 {a5},{a5_overlap}',sep='\n')
