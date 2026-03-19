a=int(input('16진수, 10진수, 8진수, 2진수 중 몇 진수?'))
b=input('값 입력:')
if a==16:
    num=int(b,16)
if a==10:
    num=int(b,10)
if a==8:
    num=int(b,8)
if a==2:
    num=int(b,2)

print('16진수:',hex(num))
print('10진수:',int(num))
print('8진수:',oct(num))
print('2진수:',bin(num))