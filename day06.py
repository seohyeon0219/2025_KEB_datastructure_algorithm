v0.2 day06 bit operation
def is_even(n) -> bool:
    '''
    짝수 판정 함수
    :param n: 판정할 정수
    :return: 짝수면 True, 홀수면 False
    '''
    if n%2==0:
        return True
    return False

a = 10 # 0000 1010
b = 11 # 0000 1011
# bit operation

print(a and b)
print(a % b) # 0000 1010 (둘 다 1일때만 1) -> 10 출력
print(a | b) # 11 출력
print(a ^ b) # 0001

n = int(input())
print(is_even(n))