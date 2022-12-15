# 문제
'''
    a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼
    사람들을 데려와 살아야 한다.

    비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정하자.
    주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라.
'''

# 입력
'''
    테스트 케이스 T
    케이스마다 정수 첫번째 줄 정수 k, 두번째 줄 정수 n
'''

# 출력
'''
    k층 n호의 거주민 수
'''

'''
    0층 1호 ~ : 1명 ~
    1층 1호 ~ : 1명, 1+2명, 1+2+3명, 1+2+3+4명 ~
    2층 1호 ~ : 1명, 1+1+2명, 1+1+2+1+2+3명, 1+1+2+1+2+3+1+2+3+4명, ~
    ...
'''

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())


