# 문제
'''
    숫자 카드는 정수 하나가 적혀져 있는 카드이다. 
    상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
'''

# 입력
'''
    첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 
    둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 
    숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

    셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 
    넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 
    이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
'''

# 출력
'''
    첫째 줄에 입력으로 주어진 M개의 수에 대해서, 
    각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.
'''

# 첫번째 시도 -> 시간 초과
"""
    import sys

    N = int(sys.stdin.readline())
    cardNums = list(map(int, sys.stdin.readline().split()))

    M = int(sys.stdin.readline())
    findNums = list(map(int, sys.stdin.readline().split()))

    count = 0
    countList = []

    for findNum in findNums:
        for cardNum in cardNums:
            if cardNum == findNum:
                count += 1
        countList.append(count)
        count = 0
                

    for answer in countList:
        print(answer, end=' ')
"""

# 두번째 시도 -> 내장 모듈 counter 이용

from collections import Counter
import sys

N = int(sys.stdin.readline())
cardNums = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
findNums = list(map(int, sys.stdin.readline().split()))

count = Counter(cardNums) # Counter({10: 3, 3: 2, -10: 2, 6: 1, 2: 1, 7: 1})
# 각 항목별로 몇 개 있는지 셈.

for findNum in findNums:
    if findNum in count:
        print(count[findNum], end=' ')
    else:
        print(0, end=' ')