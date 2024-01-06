class RandomGenerator:
    def __init__(self, a, b, n, seed):
        # Инициализация параметров генератора
        self.a = a
        self.b = b
        self.n = n
        self.state = seed

    def middle_square(self):
        # Метод середины квадрата
        self.state = int(str(self.state ** 2).zfill(8)[2:6])
        return self.state / 10000

    def linear_congruential_generator(self):
        # Линейный конгруэнтный генератор
        self.state = (self.a * self.state + self.b) % self.n
        return self.state / self.n

    def fibonacci_generator(self, x0, x1):
        # Генератор Фибоначчи
        next_value = (x0 + x1) % self.n
        x0, x1 = x1, next_value
        return next_value / self.n

    def inverse_congruential_generator(self):
        # Инверсный конгруэнтный генератор
        try:
            modular_inverse = pow(self.state, -1, self.n)
        except ValueError:
            print("Error: Modular inverse does not exist for the current state and modulus.")
            return None

        self.state = (self.a * modular_inverse + self.b) % self.n
        return self.state / self.n

    def shift_register(self, feedback_mask):
        # Регистр сдвига с линейной обратной связью
        feedback = sum(int(bit) for bit in bin(self.state & feedback_mask)[2:])
        self.state = ((self.state << 1) | feedback) % self.n
        return self.state / self.n

    def quadratic_residual(self, p, q):
        # Генератор с квадратичным остатком (BBS)
        self.state = pow(self.state, 2, p * q)
        return self.state / (p * q)

# Пример использования:
seed_value = 1234
generator = RandomGenerator(a=1664525, b=1013904223, n=2**32, seed=seed_value)

print("Middle Square Method:")  # Вывод заголовка метода середины квадрата
for _ in range(5):
    print(generator.middle_square())  # Вывод результатов метода середины квадрата

print("\nLinear Congruential Generator:")  # Вывод заголовка линейного конгруэнтного генератора
for _ in range(5):
    print(generator.linear_congruential_generator())  # Вывод результатов линейного конгруэнтного генератора

print("\nFibonacci Generator:")  # Вывод заголовка генератора Фибоначчи
x0, x1 = seed_value, seed_value + 1
for _ in range(5):
    print(generator.fibonacci_generator(x0, x1))  # Вывод результатов генератора Фибоначчи

print("\nInverse Congruential Generator:")  # Вывод заголовка инверсного конгруэнтного генератора
for _ in range(5):
    result = generator.inverse_congruential_generator()
    if result is not None:
        print(result)  # Вывод результатов инверсного конгруэнтного генератора

print("\nShift Register:")  # Вывод заголовка регистра сдвига
feedback_mask = 0b10101
for _ in range(5):
    print(generator.shift_register(feedback_mask))  # Вывод результатов регистра сдвига

print("\nQuadratic Residual (BBS):")  # Вывод заголовка генератора с квадратичным остатком (BBS)
p, q = 11, 17  # Выбор простых чисел
for _ in range(5):
    print(generator.quadratic_residual(p, q))  # Вывод результатов генератора с квадратичным остатком (BBS)
