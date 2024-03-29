# 문제
'''
    N명의 사람들이 줄을 서있다.
    1번부터 N번까지
    i번 사람이 돈을 인출하는데 걸리는 시간은 Pi분이다.

    각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램.
'''

# 입력
'''
    사람의 수 N
    각 사람이 돈을 인출하는데 걸리는 시간 Pi
'''

# 출력
'''
    첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.
'''

import sys

ans = 0

N = int(sys.stdin.readline())
Pi = list(map(int, sys.stdin.readline().split()))

# 인출 시간이 적은 순으로 정렬
Pi.sort()

for i in range(1, N+1):
    ans += sum(Pi[0:i]) # 0부터 i까지의 합
print(ans)