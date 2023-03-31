

def extract_digits(num):
    digits = []
    while num > 0:
        digit = num % 10
        digits.append(digit)
        num //= 10
    digits.reverse()
    return digits
