#!/usr/bin/env python3
"""
Простой калькулятор - пример совместного проекта
"""

class Calculator:
    """Класс для выполнения математических операций"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Сложение двух чисел"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Вычитание двух чисел"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Умножение двух чисел"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Деление двух чисел"""
        if b == 0:
            raise ValueError("Деление на ноль невозможно!")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self):
        """Получить историю операций"""
        return self.history
    
    def clear_history(self):
        """Очистить историю операций"""
        self.history = []

def main():
    """Пример использования калькулятора"""
    calc = Calculator()
    
    print("🧮 Простой калькулятор")
    print("=" * 30)
    
    # Примеры операций
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    
    print("\n📋 История операций:")
    for operation in calc.get_history():
        print(f"  {operation}")

if __name__ == "__main__":
    main()
