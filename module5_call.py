# module5_oop.py
class NumberStore:
    def __init__(self):
        self.numbers = []

    def insert(self, number):
        self.numbers.append(number)

    def search(self, x):
        if x in self.numbers:
            return self.numbers.index(x) + 1  # Indexing starts from 1 as per the requirement
        return -1

if __name__ == "__main__":
    store = NumberStore()
    
    N = int(input("Enter the value for N (positive integer): "))
    
    for i in range(N):
        num = int(input(f"Enter number {i+1}: "))
        store.insert(num)
    
    X = int(input("Enter the value for X: "))
    result = store.search(X)
    print(result)

# module5_mod.py
class NumberStore:
    def __init__(self):
        self.numbers = []

    def insert_numbers(self, N):
        self.numbers = [int(input(f"Enter number {i+1}: ")) for i in range(N)]

    def find_index(self, X):
        return self.numbers.index(X) + 1 if X in self.numbers else -1

# module5_call.py
from module5_mod import NumberStore

if __name__ == "__main__":
    store = NumberStore()
    
    N = int(input("Enter the value for N (positive integer): "))
    store.insert_numbers(N)
    
    X = int(input("Enter the value for X: "))
    print(store.find_index(X))
