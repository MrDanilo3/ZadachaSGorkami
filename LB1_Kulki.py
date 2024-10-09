import numpy as np
import matplotlib.pyplot as plt

# Розрахунок часу руху кульки по прямій лінії
def calculate_straight_slide_time(g):
    return 2 / np.sqrt(g)

# Розрахунок часу руху кульки по параболі
def calculate_parabolic_slide_time(g):
    return calculate_integral(0, 1, 500, g)

# Розрахунок інтегралу для параболи
def calculate_integral(x0, x1, N, g):
    sum_ = 0
    subinterval_width = (x1 - x0) / N

    for i in range(N):
        x = x0 + i * subinterval_width
        derivative_of_function = 2 * x  
        integral_curve = np.sqrt(1 + derivative_of_function ** 2) 
        sum_ += integral_curve

    integral_result = subinterval_width * sum_
    return integral_result / np.sqrt(2 * g)  # Повертаємо час

# Функція для побудови графіків
def plot_trajectories():
    # Параметри
    g = 9.81  # Прискорення вільного падіння
    h = 1.0   # Висота 1 метр
    d = 2.0   # Довжина траєкторії (горизонтальна відстань)

    # Пряма траєкторія
    x_straight = np.linspace(0, d, 100)
    y_straight = h - (h / d) * x_straight  # Лінійна залежність для прямої

    # Параболічна траєкторія
    x_parabolic = np.linspace(0, d, 100)
    y_parabolic = (4 * h / d**2) * (x_parabolic - d / 2)**2  # Ввігнута парабола

    # Створення графіка
    plt.figure(figsize=(8, 6))
    plt.plot(x_straight, y_straight, label="Пряма траєкторія", color="blue", linewidth=2)
    plt.plot(x_parabolic, y_parabolic, label="Параболічна траєкторія", color="red", linestyle="--", linewidth=2)

    # Додаткові налаштування
    plt.title("Траєкторії руху кульок", fontsize=14)
    plt.xlabel("Горизонтальна відстань (м)", fontsize=12)
    plt.ylabel("Вертикальна висота (м)", fontsize=12)
    plt.legend(loc="upper right")
    plt.grid(True)

    # Відображення графіка
    plt.show()

# Приклад використання
g = 9.81  # Прискорення вільного падіння

# Розрахунок часу
straight_time = calculate_straight_slide_time(g)
parabolic_time = calculate_parabolic_slide_time(g)

print(f"Час руху по прямій лінії: {straight_time:.4f} секунд")
print(f"Час руху по параболі: {parabolic_time:.4f} секунд")

# Виводимо графіки
plot_trajectories()
