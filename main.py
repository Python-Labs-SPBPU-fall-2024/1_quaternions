import math


def is_quat(other):
    """Функция, проверяющая тип переменной и при необходимости преобразующая в объект класса Quaternion"""
    if isinstance(other, Quaternion):
        return other
    else:
        return Quaternion(other)


class Quaternion:
    """
    Класс кватернионов
    """
    def __init__(self, w=0.0, i=0.0, j=0.0, k=0.0):
        self.w = w  # Скалярная часть
        self.i = i  # Векторная часть (i)
        self.j = j  # Векторная часть (j)
        self.k = k  # Векторная часть (k)

    def sum(self, other):
        """Метод, возвращающий сумму кватернионы"""
        return Quaternion(self.w + other.w, self.i + other.i, self.j + other.j, self.k + other.k)

    def sub(self, other):
        """Метод, возвращающий разность кватернионов"""
        return Quaternion(self.w - other.w, self.i - other.i, self.j - other.j, self.k - other.k)

    def __add__(self, other):
        """Сумма кватерниона с другой переменной

        На основе переменной создаем элемент класса и передаем в метод sum"""
        other_q = is_quat(other)
        return self.sum(other_q)

    def __radd__(self, other):
        """Сумма переменной с кватернионом

        На основе переменной создаем элемент класса и передаем в метод sum"""
        other_q = is_quat(other)
        return other_q.sum(self)

    def __sub__(self, other):
        """Разность кватерниона с другой переменной

        На основе переменной создаем элемент класса и передаем в метод sub"""
        other_q = is_quat(other)
        return self.sub(other_q)

    def __rsub__(self, other):
        """Разность переменной с кватернионом

        На основе переменной создаем элемент класса и передаем в метод sum"""
        other_q = is_quat(other)
        return other_q.sub(self)

    def __eq__(self, other):
        """Метод сравнения катернионов =="""
        other_q = is_quat(other)
        return (self.w == other_q.w and
                self.i == other_q.i and
                self.j == other_q.j and
                self.k == other_q.k)

    def __ne__(self, other):
        """Метод сравнения катернионов !="""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Метод сравнения катернионов <"""
        other_q = is_quat(other)
        return self.norm() < other_q.norm()

    def __le__(self, other):
        """Метод сравнения катернионов <="""
        other_q = is_quat(other)
        return self.norm() <= other_q.norm()

    def __gt__(self, other):
        """Метод сравнения катернионов >"""
        return not self.__lt__(other)

    def __ge__(self, other):
        """Метод сравнения катернионов >="""
        return not self.__le__(other)

    def __repr__(self):
        """Вывод квтерниона"""
        return f"({self.w} + {self.i}i + {self.j}j + {self.k}k)"

    def mate(self):
        """Метод, возвращающий сопряженный катернион"""
        return Quaternion(self.w, -self.i, -self.j, -self.k)

    def norm(self):
        """Метод, возвращающий норму катерниона"""
        return math.sqrt(self.w ** 2 + self.i ** 2 + self.j ** 2 + self.k ** 2)

    def normalization(self):
        """Метод, нормализующий катернион"""
        norm_quat = self.norm()
        if (norm_quat != 0):
            return Quaternion(self.w / norm_quat, self.i / norm_quat,
                              self.j / norm_quat, self.k / norm_quat)
        else:
            print("Cannot normalize")


def test_arithmetic():

    q0 = Quaternion()
    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(0.5, 3.2, 77, 0)
    q3 = q2 - q1
    q4 = Quaternion(4)
    q5 = q0 + q1 - q2 + q3 + q4
    print(q0, q1, q2, q3, q4)
    print(q5)
    print(123 + q1)
    print(q0 + 1000.11)
    print(q4 + (Quaternion(3, 5)))

def test_comprasion():
    q0 = Quaternion()
    print(q0 == 0)
    print(q0 >= 0)
    print(q0 <= 0)

    print(1000 == q0)
    print(1000 != q0)

    q1 = Quaternion(1, 2, 3, 4)
    q2 = Quaternion(3, 6, 3, 9)
    q3 = Quaternion(800)
    print(q1 > q2)
    print(q1 < q2)
    print(q2 > q3)
    print(q3 > q2)
    print(q1 > q3)
    print(q1 < q3)
    print(q1 >= q3)
    print(q1 <= q3)

def test_operation():
    q0 = Quaternion()
    print(q0.mate())
    print(q0.norm())
    print(q0.normalization())
    print(q0.reverse())

    q1 = Quaternion(1, 2, 3, 4)
    print(q1.mate())
    print(q1.norm())
    print(q1.normalization())
    print(q1.reverse())



if __name__ == '__main__':
    #test_arithmetic()
    #test_comprasion()
    test_operation()
