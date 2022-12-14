# 문제
'''
    재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.
    재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다. 재민이를 도와주자!
'''

# 입력
'''
    정수 K
    K개의 줄에 정수 1개씩 주어짐.
    정수가 "0"일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
'''

# 출력
'''
    재민이가 최종적으로 적어 낸 수의 합 출력
'''

import sys

K = int(sys.stdin.readline())
nums = []
sum = 0

for _ in range(K):
    num = int(sys.stdin.readline())
    if num != 0:
        nums.append(num) # 배열에 넣기
    else:
        nums.pop() # 배열의 맨 마지막 요소 빼기


for num in nums:
    sum += num

print(sum)
