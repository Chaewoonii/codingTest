num = int(input())

#1, 69, 8, 0
# f(1) : 0, 1, 8
# f(2)=4: 11, 69, 88, 96
# f(3): f(2)*f(1)+f(2) = 16: 101, 111, 181, 609, 619, 689, 808, 818, 888, 906, 916, 986
# f(4): f(2)*f(2)+f(3)+f(2) = 36: 1001, 1691, 1881, 1961,
# f(5): f(2)*f(3) 120: 10001...
# f(6): f(2)*f(4)

def flipOver(num):
    if num == 0:
        return [""]
    elif num == 1:
        return ["0", "1", "8"]




print(flipOver(num))