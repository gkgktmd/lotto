#1회부터
import random
import time
start=time.time()

hr22=[43,27,34,17,1,4,13,12,33,39,20,10,40,38,18,26,14,2,31,3,11,37] #상위 22개
lr23=[24,21,19,16,45,8,7,15,36,6,5,42,44,30,35,25,28,32,41,23,29,22,9] #하위 23개

hr38=[43,27,34,17,1,4,13,12,33,39,20,10,40,38,18,26,14,2,31,3,11,37
      ,24,21,19,16,45,8,7,15,36,6,5,42,44,30,35,25] #상위 22개
lr7=[28,32,41,23,29,22,9] #하위 7개

def get_count(x):
    new_list={}
    for i in x:
        try: new_list[i]+=1
        except: new_list[i]=1
    return new_list

count=0
while True:
    # 1번 모델 중복 제거
    while True:
        a1 = sorted(random.sample(hr38, 4) + random.sample(lr7, 2))
        a11 = get_count(a1)
        a = [0] * 10
        for key, value in a11.items():
            if value > 1:
                a[value] += 1
        if a[2] <= 0 and a[3] <= 0 and a[4] == 0 and a[5] == 0:
            break

    # 2번 모델 중복 제거
    while True:
        a2 = sorted(random.sample(hr38, 5) + random.sample(lr7, 1))
        a22 = get_count(a2)
        a = [0] * 10
        for key, value in a22.items():
            if value > 1:
                a[value] += 1
        if a[2] <= 0 and a[3] <= 0 and a[4] == 0 and a[5] == 0:
            break

    # 3번 모델 중복 제거
    while True:
        a3 = sorted(random.sample(hr22, 4) + random.sample(lr23, 2))
        a33 = get_count(a3)
        a = [0] * 10
        for key, value in a33.items():
            if value > 1:
                a[value] += 1
        if a[2] <= 0 and a[3] <= 0 and a[4] == 0 and a[5] == 0:
            break

    # 4번 모델 중복 제거
    while True:
        a4 = sorted(random.sample(hr22, 2) + random.sample(lr23, 4))
        a44 = get_count(a4)
        a = [0] * 10
        for key, value in a44.items():
            if value > 1:
                a[value] += 1
        if a[2] <= 0 and a[3] <= 0 and a[4] == 0 and a[5] == 0:
            break

    # 5번 모델 중복 제거
    while True:
        a5 = sorted(random.sample(hr22, 3) + random.sample(lr23, 3))
        a55 = get_count(a5)
        a = [0] * 10
        for key, value in a55.items():
            if value > 1:
                a[value] += 1
        if a[2] <= 0 and a[3] <= 0 and a[4] == 0 and a[5] == 0:
            break

    # 쓰까 모델 추출
    num = a1 + a2 + a3 + a4 + a5
    d1 = get_count(num)

    a = [0] * 10
    for key, value in d1.items():
        if value > 1:
            a[value] += 1
    print(a)
    count+=1
    if a[2] == 2 and a[3] <= 0 and a[4] == 0 and a[5]==0:
        break

print('-'*30)
print(f'1-1: {len(hr22)}개 1-2: {len(lr23)}개')

a22=sorted(hr22+lr23)

if a22==list(range(1,46)):
    print('대상 True')

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
print('1회 모델')
print('-'*30)
print(f'#1 {a1},{a1_overlap}',f'#2 {a2},{a2_overlap}',f'#3 {a3},{a3_overlap}' \
      ,f'#4 {a4},{a4_overlap}',f'#5 {a5},{a5_overlap}',sep='\n')