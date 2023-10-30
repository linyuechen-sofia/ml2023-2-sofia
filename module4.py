N = int(input("Enter N (positive integer): "))
numbers = [int(input()) for _ in range(N)]
X = int(input("Enter X (integer): "))

if X in numbers:
    print(numbers.index(X) + 1)
else:
    print(-1)
