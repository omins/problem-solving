infix = input()
prefix = ''
stack = []

for ch in infix:  # 중위표기식의 각 원소에 대해
    if ch.isalpha():  # 알파벳이면 prefix에 곧바로 추가
        prefix += ch
    else:
        if ch == '(':
            stack.append(ch)
        elif ch in ('+', '-'):  # 가장 우선순위가 낮은 연산자
            while stack and stack[-1] != '(':  # 여는 괄호를 만나면 멈추고
                prefix += stack.pop()  # 그렇지 않으면 stack 원소를 prefix에 추가
            stack.append(ch)
        elif ch in ('/', '*'):
            # 동일 우선순위 연산자는 먼저 나오는 연산자가 우선
            while stack and stack[-1] in ('/', '*'):
                prefix += stack.pop()
            stack.append(ch)
        elif ch == ')':  # 닫는 괄호를 만나면
            while stack and stack[-1] != '(':  # 괄호 내 모든 연산자를 prefix에 추가
                prefix += stack.pop()
            stack.pop()

# 알고리즘이 끝나고 스택에 원소가 있으면 모두 prefix에 추가
while stack:
    prefix += stack.pop()

print(prefix)
