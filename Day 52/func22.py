def is_armstrong(num):
    original = num
    total = 0

    while num > 0:
        digit = num % 10
        total += digit ** 3
        num = num // 10

    return total == original

print(is_armstrong(153))
