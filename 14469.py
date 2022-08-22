#14469: 소가 길을 건나간 이유 3

"""
문제:
이웃 농장의 소가 길을 마구잡이로 건너는 것에 진절머리가 난 존은 극단의 결정을 내린다. 농장 둘레에 매우 큰 울타리를 짓는 것이다. 이렇게 하면 근처 농장 출신의 소가 들어올 일이 거의 없다. 이 일로 주변 소들이 분개하였다. 친구네 집에 놀러 갈 수 없을 뿐만 아니라, 매년 참가하던 국제 젖 짜기 올림피아드에도 올해는 참가할 수 없게 되었기 때문이다.
이웃 농장의 소 중 존의 농장에 방문할 수 있는 소가 조금 있긴 하지만, 그들도 안심할 수 있는 건 아니다. 존의 농장에 들어가는 문은 하나밖에 없고, 그 문을 통과하려면 감시관의 길고 긴 검문을 받아야 한다. 여러 마리의 소가 한 번에 들어가려고 하면 줄이 그 만큼 길어진다.
N마리의 소가 이 농장에 방문하러 왔다. 소가 도착한 시간과 검문받는 데 걸리는 시간은 소마다 다르다. (물론 같을 수도 있다.) 두 소가 동시에 검문을 받을 수는 없다. 예를 들어, 한 소가 5초에 도착했고 7초 동안 검문을 받으면, 8초에 도착한 그 다음 소는 12초까지 줄을 서야 검문을 받을 수 있다.
모든 소가 농장에 입장하려면 얼마나 걸리는 지 구해보자.
"""

N = int(input())
cow = []

for _ in range(N):
    arrive_time, check_time = map(int, input().split())
    cow.append((arrive_time, check_time))
cow.sort()

time = cow[0][0]
for i in range(N):
    if time <= cow[i][0]:
        time = cow[i][0] + cow[i][1]
    else:
        time += cow[i][1]

print(time)
