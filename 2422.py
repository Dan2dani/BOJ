#2422: 한윤정이 이탈리아에 가서 아이스크림을 사먹는데

"""
문제:
한윤정과 친구들은 이탈리아로 방학 여행을 갔다. 이탈리아는 덥다. 윤정이와 친구들은 아이스크림을 사먹기로 했다.
아이스크림 가게에는 N종류의 아이스크림이 있다. 모든 아이스크림은 1부터 N까지 번호가 매겨져있다.
어떤 종류의 아이스크림을 함께먹으면, 맛이 아주 형편없어진다.
따라서 윤정이는 이러한 경우를 피하면서 아이스크림을 3가지 선택하려고 한다.
이때, 선택하는 방법이 몇 가지인지 구하려고 한다.
"""
import  sys

N, M = map(int, sys.stdin.readline( ).strip().split())
C = [[False for _ in range(N)] for _ in range(N)]

for _ in range(M):
    ice1, ice2 = map(int, input().split())
    C[ice1 - 1][ice2 - 1] = True
    C[ice2 - 1][ice1 - 1] = True
cnt = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if not C[i][j] and not C[i][k] and not C[j][k]:
                cnt += 1

print(cnt)