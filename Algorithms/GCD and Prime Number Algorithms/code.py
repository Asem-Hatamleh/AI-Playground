# code.py

def Min(x, y):
    return x if x < y else y

def GreatestCommonDivisor1(x, y):
    r = Min(x, y)
    largest = 1
    for j in range(1, r + 1):
        if x % j == 0 and y % j == 0:
            largest = j
    return largest

def gcd(x, y):
    while y != 0:
        t = x % y
        x = y
        y = t
    return x

def gcd_subtraction(x, y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x

def are_coprime(a, b):
    return gcd(a, b) == 1

def find_y_for_prime(x):
    if x == 2 or x == 3:
        return None
    elif x % 6 == 1 or x % 6 == 5:
        y = 1
        while True:
            if (6 * y + 1 == x) or (6 * y - 1 == x):
                return y
            y += 1
    else:
        return None

if __name__ == "__main__":
    x = int(input("Enter the value of x: "))
    y = int(input("Enter the value of y: "))
    print("GCD using first method:", GreatestCommonDivisor1(x, y))
    print("GCD using Euclidean division:", gcd(x, y))
    print("GCD using subtraction:", gcd_subtraction(x, y))
    
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    if are_coprime(num1, num2):
        print(f"{num1} and {num2} are coprime.")
    else:
        print(f"{num1} and {num2} are not coprime.")
    
    prnum = int(input("Enter the value of prime number: "))
    y_value = find_y_for_prime(prnum)
    print("y value for prime number", prnum, "is:", y_value)
