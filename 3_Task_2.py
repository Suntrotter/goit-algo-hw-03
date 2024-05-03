import turtle


def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)


def main():
    # Введення рівня рекурсії від користувача
    try:
        level = int(input("Введіть рівень рекурсії (ціле число більше 0): "))
        if level <= 0:
            print("Рівень рекурсії повинен бути цілим числом більше 0.")
            return
    except ValueError:
        print("Введено некоректне значення для рівня рекурсії.")
        return

    # Налаштування вікна
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    screen.title("Сніжинка Коха")

    # Налаштування черепашки
    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.speed(0)
    snowflake_turtle.color("blue")
    snowflake_turtle.penup()
    snowflake_turtle.goto(-200, 100)
    snowflake_turtle.pendown()

    for _ in range(3):
        koch_snowflake(snowflake_turtle, level, 400)
        snowflake_turtle.right(120)

    screen.mainloop()


if __name__ == "__main__":
    main()
