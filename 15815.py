#15815: 천재 수학자 성필

"""
문제:
평행 세계의 성필은 숫자와 연산자를 만든 당대 최고의 수학자이다. 그리고 놀랍게도 이 숫자와 연산자는 현재 우리가 사용하는 것과 같다. 하지만 수식은 연산자가 피연산자 가운데 위치하는 우리와는 다르게 연산자가 피연산자 뒤에 위치한다고 한다.

우리 세계의 식을 성필의 식으로 바꾸는 방법을 간단히 설명하자면 이렇다. 우선 주어진 식을 연산자의 우선순위에 따라 괄호로 묶어준다. 그런 다음에 괄호 안의 연산자를 괄호의 오른쪽으로 옮겨주면 된다.

예를 들어 a+b*c는 (a+(b*c))의 식과 같게 된다. 그다음에 안에 있는 괄호의 연산자 *를 괄호 밖으로 꺼내게 되면 a+bc*가 된다. 마지막으로 또 +를 괄호의 오른쪽으로 고치면 abc*+가 되게 된다.

천재 수학자 성필은 자신이 만든 이런 간단한 식조차 1초 안에 계산하지 못하는 사람들을 위하여 답을 구해주는 프로그램을 개발하려고 했지만 아쉽게도 성필의 세계에는 프로그래밍 언어가 없다. 프로그래밍을 할 수 있는 우리가 성필을 위해 평행세계의 식을 계산하는 프로그램을 만들어주자.
"""

import sys

postexp = sys.stdin.readline().strip()
operand = [] #피연산자 스택

for i in postexp:
    if i.isdecimal() == True: #피연산자
        operand.append(int(i))
    else: #연산자이면
        op1 = operand.pop()
        op2 = operand.pop()
        if i == "+":
            operand.append(op1 + op2)
        elif i == "-":
            operand.append(op2 - op1)
        elif i == "*":
            operand.append(op1 * op2)
        elif i == "/":
            operand.append(op2 // op1)

print(operand.pop())