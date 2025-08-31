#!/usr/bin/env python3
"""
Тесты для калькулятора
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import Calculator
import unittest

class TestCalculator(unittest.TestCase):
    """Тесты для класса Calculator"""
    
    def setUp(self):
        """Настройка перед каждым тестом"""
        self.calc = Calculator()
    
    def test_add(self):
        """Тест сложения"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_subtract(self):
        """Тест вычитания"""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)
    
    def test_multiply(self):
        """Тест умножения"""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
    
    def test_divide(self):
        """Тест деления"""
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(0, 5), 0)
    
    def test_divide_by_zero(self):
        """Тест деления на ноль"""
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
    
    def test_history(self):
        """Тест истории операций"""
        self.calc.add(2, 3)
        self.calc.subtract(5, 2)
        
        history = self.calc.get_history()
        self.assertEqual(len(history), 2)
        self.assertIn("2 + 3 = 5", history)
        self.assertIn("5 - 2 = 3", history)
    
    def test_clear_history(self):
        """Тест очистки истории"""
        self.calc.add(2, 3)
        self.calc.clear_history()
        
        history = self.calc.get_history()
        self.assertEqual(len(history), 0)

def run_tests():
    """Запуск тестов"""
    print("🧪 Запуск тестов калькулятора...")
    print("=" * 40)
    
    # Создаем тестовый набор
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCalculator)
    
    # Запускаем тесты
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Выводим результат
    if result.wasSuccessful():
        print("\n✅ Все тесты пройдены успешно!")
    else:
        print(f"\n❌ Тесты не пройдены: {len(result.failures)} ошибок")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    run_tests()
