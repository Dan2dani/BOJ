#2776: 암기왕
#파이썬 이진탐색 모듈(?)) 공부하기!
"""
문제:
연종이는 엄청난 기억력을 가지고 있다.
그래서 하루 동안 본 정수들을 모두 기억 할 수 있다.
하지만 이를 믿을 수 없는 동규는 그의 기억력을 시험해 보기로 한다.
동규는 연종을 따라 다니며, 연종이 하루 동안 본 정수들을 모두 ‘수첩1’에 적어 놓았다.
그것을 바탕으로 그가 진짜 암기왕인지 알아보기 위해, 동규는 연종에게 M개의 질문을 던졌다. 질문의 내용은 “X라는 정수를 오늘 본 적이 있는가?” 이다.
연종은 막힘없이 모두 대답을 했고, 동규는 연종이 봤다고 주장하는 수 들을 ‘수첩2’에 적어 두었다.
집에 돌아온 동규는 답이 맞는지 확인하려 하지만, 연종을 따라다니느라 너무 힘들어서 여러분에게 도움을 요청했다.
동규를 도와주기 위해 ‘수첩2’에 적혀있는 순서대로, 각각의 수에 대하여, ‘수첩1’에 있으면 1을, 없으면 0을 출력하는 프로그램을 작성해보자.
"""
import sys

def binary_search(left, right, i, Mlist):
    while left <= right:
        mid = (left + right) // 2
        if Nlist[mid] == i:
            return 1
            break
        elif Nlist[mid] > i:
            right = mid - 1
        else:
            left = mid + 1
    return 0

T = int(sys.stdin.readline( ))

for _ in range(T):
    N = int(sys.stdin.readline( ))
    Nlist = sorted(list(map(int, sys.stdin.readline().strip().split())))
    M = int(sys.stdin.readline( ))
    Mlist = list(map(int, sys.stdin.readline().strip().split()))

    left = 0
    right = N - 1
    for i in Mlist:
        print(binary_search(left, right, i, Mlist))