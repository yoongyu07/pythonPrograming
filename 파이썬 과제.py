print("1. 입력한 수식 계산  2. 두 수 사이의 합계 : ", end="")
choice = int(input())

# 1번 선택: 수식 계산
if choice == 1:
    print("*** 수식을 입력하세요 : ", end="")
    expr = input()
    
    result = eval(expr)  # 입력한 수식 계산
    print(f"{expr} 결과는 {result}입니다.")

# 2번 선택: 두 수 사이 합계
elif choice == 2:
    print("*** 첫 번째 숫자를 입력하세요 : ", end="")
    num1 = int(input())
    
    print("*** 두 번째 숫자를 입력하세요 : ", end="")
    num2 = int(input())
    
    total = 0
    for i in range(num1, num2 + 1):
        total += i
    
    print(f"{num1}+...+{num2}는 {total}입니다.")