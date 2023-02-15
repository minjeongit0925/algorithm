# 문제
'''
    계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.
    1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
    2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
    3. 마지막 도착 계단은 반드시 밟아야 한다.
'''

# 입력
'''
    첫째 줄에 계단의 개수가 주어진다.
    둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로
    각 계단에 쓰여 있는 점수가 주어진다.
'''

# 출력
'''
    첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 출력한다.
'''

import sys
input = sys.stdin.readline
score = []
result = 0

num = int(input())
for _ in range(num):
    score.append(int(input()))

result += score[-1] # 마지막 계단은 꼭 밟아야한다.
