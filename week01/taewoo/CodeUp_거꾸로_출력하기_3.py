# CodeUp 1402 - 거꾸로 출력하기 3
# n개 정수를 입력받아 스택에 넣었다가 pop 하며 역순으로 출력


def main():
    n = int(input())
    nums = list(map(int, input().split()))

    stack = []
    for x in nums:
        stack.append(x)

    out = []
    while stack:
        out.append(str(stack.pop()))

    print(" ".join(out))


if __name__ == "__main__":
    main()
