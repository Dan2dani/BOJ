#★★★10825: 국영수

"""
문제:
도현이네 반 학생 N명의 이름과 국어, 영어, 수학 점수가 주어진다. 이때, 다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성하시오.
국어 점수가 감소하는 순서로
국어 점수가 같으면 영어 점수가 증가하는 순서로
국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)
국어 내림차순, 영어 오름차순, 수학 내림차순, 사전순
"""

N = int(input())
mems = []

for _ in range(N):
    mems.append(list(map(str,input("").split())))

mems.sort(key = lambda x:str(x[0]))
mems.sort(key = lambda x:int(x[3]), reverse=True)
mems.sort(key = lambda x:int(x[2]))
mems.sort(key = lambda x:int(x[1]), reverse=True)

for i in mems:
    print(i[0])