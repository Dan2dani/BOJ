#10815: 숫자카드

#문제: 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.
#이진탐색

N = int(input(""))
N_list = list(map(int, input().split()))
M = int(input(""))
M_list = list(map(int, input().split()))
N_list.sort()

for i in M_list:
    flag = 0
    left = 0
    right = N - 1
    while right >= left:
        mid = (left + right) // 2
        if N_list[mid] == i:
            flag = 1
            break
        elif N_list[mid] < i:
            left = mid + 1
        else:
            right = mid - 1
    if flag == 1:
        print("1", end=" ")
    else:
        print("0", end=" ")
    
________________________________________________________________________________________________________________    
#bisect 라이브러리 사용
#bisect_left(a,x): 정렬된 순서를 유지하면서 리스트 a 에서 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
#bisect_rigth(a,x): 정렬된 순서를 유지하면서 리스트  a 에서 데이터 x를 삽입할 가장 오론쪽 인덱스를 찾는 메서드

from bisect import bisect_right, bisect_left

N = int(input(""))
N_list = list(map(int, input().split()))
M = int(input(""))
M_list = list(map(int, input().split()))
N_list.sort()

for i in M_list:
    left = bisect_left(N_list, i)
    right = bisect_right(N_list, i)
    if left == right:
        print("0", end = " ")
    else:
        print("1", end = " ")
