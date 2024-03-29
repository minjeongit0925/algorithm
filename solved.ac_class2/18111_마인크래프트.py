# 문제
'''
    땅 고르기 작업을 해야 한다.
    세로 N, 가로 M 크기의 접터를 골랐다.
    집터 맨 왼쪽 위의 좌표는 (0, 0)이다.
    
    1. 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
    2. 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.

    1번 작업은 2초, 2번 작업은 1초

    '땅 고르기' 작업에 걸리는 최소 시간과 그 경우 땅의 높이를 출력하시오.
    B개의 블록이 들어 있다.
'''

# 입력
'''
    N, M, B가 주어진다.
    N개의 줄에 각각 M개의 정수로 땅의 높이가 주어진다.
'''

# 출력
'''
    첫째 줄에 땅을 고르는데 걸리는 시간과 땅의 높이를 출력하시오.
    답이 여러 개 있다면 그 중에서 땅의 높이가 가장 높은 것을 출력하시오.
'''
# 브루트포스 알고리즘
# pypy3로 채점함.

# 도움
'''
    https://thflgg133.tistory.com/88
'''

import sys
from math import inf

N, M, B = map(int, sys.stdin.readline().split())
lands = [0 for _ in range(N)]

for i in range(N):
    lands[i] = list(map(int, sys.stdin.readline().split()))

# 2차원배열 요소들의 평균을 구한다.
height = 0
result = inf

for i in range(257):
    max = 0
    min = 0
    for j in range(N):
        for k in range(M):
            if lands[j][k] < i:
                min += i - lands[j][k]
            else:
                max += lands[j][k] - i
    inventroy = max + B

    if inventroy < min:
        continue
    time = 2 * max + min

    if time <= result:
        result = time
        height = i
print(result, height)