def isPalindrome(n: int) -> bool:
    rev = 0
    i = n
    while i > 0:
        rev = rev * 10 + i % 10
        i //= 10
    return (n == rev)
def countPal(minn: int, maxx: int):
    for i in range(minn, maxx + 1):
        if isPalindrome(i):
            print(i, end = " ")
if __name__ == "__main__":
    a=int(input("first number:"))
    b=int(input("second number:"))
    countPal(a, b)
