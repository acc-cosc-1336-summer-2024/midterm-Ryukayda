from question_c import is_prime

if __name__ == "__main__":
    numbers = [4, 5, 11]
    for number in numbers:
        print(f"Is {number} prime? {is_prime(number)}")
