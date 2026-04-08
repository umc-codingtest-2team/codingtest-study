n = int(input())

arr = [] # 입력 수열
stack = [] # 진짜 스택
output = [] # +, - 저장

current = 1 

for _ in range(n):
    arr.append(int(input()))

for x in arr:
    while current <= x:
        stack.append(current)
        output.append('+')
        current += 1
    
    if stack and stack[-1] == x:
        stack.pop()
        output.append('-')
    else:
        print("NO")
        exit()
        
print('\n'.join(output))