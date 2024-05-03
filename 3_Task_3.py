def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Перемістити диск з {source} на {target}: 1")
        return
    
    hanoi(n - 1, source, auxiliary, target)
    print(f"Перемістити диск з {source} на {target}: {n}")
    hanoi(n - 1, auxiliary, target, source)

def main():
    n = int(input("Введіть кількість дисків: "))
    if n <= 0:
        print("Кількість дисків повинна бути більше 0.")
        return
    
    source = 'A'
    auxiliary = 'B'
    target = 'C'

    print(f"Початковий стан: {{'A': {list(range(n, 0, -1))}, 'B': [], 'C': []}}")
    hanoi(n, source, target, auxiliary)
    print(f"Кінцевий стан: {{'A': [], 'B': [], 'C': {list(range(n, 0, -1))}}}")

if __name__ == "__main__":
    main()
