#1758: 알바생 강호

"""
문제:
손님들은 입구에 들어갈 때, 강호에게 팁을 준다. 손님들은 자기가 커피를 몇 번째 받는지에 따라 팁을 다른 액수로 강호에게 준다.
각 손님은 강호에게 원래 주려고 생각했던 돈 - (받은 등수 - 1) 만큼의 팁을 강호에게 준다.
만약, 위의 식으로 나온 값이 음수라면, 강호는 팁을 받을 수 없다.
예를 들어, 민호는 팁을 3원 주려고 했고, 재필이는 팁을 2원, 주현이가 팁을 1원 주려고 한 경우를 생각해보자.
민호, 재필, 주현이 순서대로 줄을 서있다면, 민호는 강호에게 3-(1-1) = 3원, 재필이는 2-(2-1) = 1원, 주현이는 1-(3-1) = -1원을 팁으로 주게 된다.
주현이는 음수이기 때문에, 강호에게 팁을 주지 않는다. 따라서, 강호는 팁을 3+1+0=4원을 받게 된다.
스타박스 앞에 있는 사람의 수 N과, 각 사람이 주려고 생각하는 팁이 주어질 때, 손님의 순서를 적절히 바꿨을 때,
강호가 받을 수 잇는 팁의 최댓값을 구하는 프로그램을 작성하시오.
"""
N = int(input())
tips = []
maxtip = 0

for _ in range(N):
    tips.append(int(input()))

tips.sort(reverse=True)

for i in range(len(tips)):
    if tips[i] - i > 0:
        maxtip += (tips[i] - i)
    else:
        break

print(maxtip)