def is_even(n) -> bool:
    '''
    짝수 판정 함수
    :param n: 판정할 정수
    :return: 짝수면 True, 홀수면 False
    '''


    return not n & 1
    # 비트 연산(홀수는 무조건 마지막 비트가 1로 끝남)으로 짝수 판정 가능, 11을 입력하면 1011 & 0001
    # if n % 2==0:
    #     return True
    # return False


n = int(input())
print(is_even(n))


