# 문제 
'''
    <그림 참고>
    1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를
    출력하는 프로그램을 작성하시오.
'''

# 입력
'''
    컴퓨터의 수
    네트워크 상에서 직접 연결되어 있는 컴퓨터의 쌍의 수
    한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
'''

# 출력
'''
    1번 컴퓨터가 웜 바이러스에 걸렸을 때, 
    1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 
    첫째 줄에 출력한다.
'''

import sys

input = sys.stdin.readline
com = int(input())
pairs = int(input())
for _ in range(pairs):
    pair = map(int, input().split())
    
# 1번 컴퓨터가 웜 바이러스에 걸렸을 때 
# dfs를 이용해서 해결하면 될 것 같다.
'''
    경로를 저장하기 위한 2차원 리스트
    총 m개의 간선을 입력받아 경로를 변수graph에 저장한다.
    다녀간 정점을 확인하기 위한 변수
    들리지않은 정점이면 dfs()를 이용하여 다시 반복

    dfs()를 복습해보자
'''
