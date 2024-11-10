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

    def __add__(self, other):
        """Сумма кватерниона с другим кватернионом"""

        other_q = is_quat(other)
        return Quaternion(self.w + other_q.w, self.i + other_q.i, self.j + other_q.j, self.k + other_q.k)

    def __radd__(self, other):
        """Сумма кватернионов, изменяемый объект справа"""
        other_q = is_quat(other)
        return other_q + self

    def __sub__(self, other):
        """Разность кватерниона с другим кватернионом"""
        other_q = is_quat(other)
        return Quaternion(self.w - other_q.w, self.i - other_q.i, self.j - other_q.j, self.k - other_q.k)

    def __rsub__(self, other):
        """Разность кватернионов, изменяемый объект справа"""
        other_q = is_quat(other)
        return other_q - self

    def __eq__(self, other):
        """Метод сравнения кватернионов =="""
        other_q = is_quat(other)
        return (math.isclose(self.w,other_q.w, abs_tol = 1e-3) and
                math.isclose(self.i, other_q.i, abs_tol = 1e-3) and
                math.isclose(self.j, other_q.j, abs_tol = 1e-3) and
                math.isclose(self.k, other_q.k, abs_tol = 1e-3))

    def __ne__(self, other):
        """Метод сравнения кватернионов !="""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Метод сравнения кватернионов <"""
        other_q = is_quat(other)
        return self.norm() < other_q.norm()

    def __le__(self, other):
        """Метод сравнения кватернионов <="""
        other_q = is_quat(other)
        return self.norm() <= other_q.norm()

    def __gt__(self, other):
        """Метод сравнения кватернионов >"""
        return not self.__lt__(other)

    def __ge__(self, other):
        """Метод сравнения кватернионов >="""
        return not self.__le__(other)

    def __repr__(self):
        """Вывод квтерниона"""
        return f"({self.w} + {self.i}i + {self.j}j + {self.k}k)"

    def mate(self):
        """Метод, возвращающий сопряженный катернион"""
        return Quaternion(self.w, -self.i, -self.j, -self.k)

    def norm(self):
        """Метод, возвращающий норму катерниона"""
        return (self.w ** 2 + self.i ** 2 + self.j ** 2 + self.k ** 2) ** 0.5

    def normalization(self):
        """Метод, нормализующий катернион"""
        norm_quat = self.norm()
        if (norm_quat != 0):
            return Quaternion(self.w / norm_quat, self.i / norm_quat,
                              self.j / norm_quat, self.k / norm_quat)
        else:
            print("Cannot normalize")

    def __mul__(self, other):
        """Умножение кватерниона на другой кватернион"""
        other_q = is_quat(other) #на всякий случай переводим объект other в кватернион
        return Quaternion(
            self.w * other_q.w - self.i * other_q.i - self.j * other_q.j - self.k * other_q.k,  #w
            self.w * other_q.i + self.i * other_q.w + self.j * other_q.k - self.k * other_q.j,  #i
            self.w * other_q.j - self.i * other_q.k + self.j * other_q.w + self.k * other_q.i, #j
            self.w * other_q.k + self.i * other_q.j - self.j * other_q.i + self.k * other_q.w  #k
        )
    def __rmul__(self, other):
        """Умножение кватернионов, изменяемый объект справа"""
        other_q = is_quat(other)
        return other_q * self
    
    def inverse(self):
        """Обратный по умножению кватернион"""
        norm_squared = self.norm() ** 2
        if norm_squared != 0:
            return Quaternion(
                self.w / norm_squared, 
                -self.i / norm_squared, 
                -self.j / norm_squared, 
                -self.k / norm_squared
            )
        else:
            raise ZeroDivisionError("Cannot invert a quaternion with zero norm")


    def __truediv__(self, other):
        """Деление кватерниона на другой кватернион"""
        other_q = is_quat(other)
        return self * other_q.inverse()

    def __rtruediv__(self, other):
        """Деление кватернионов, изменяемый объект справа"""
        other_q = is_quat(other)
        return  self * other_q.inverse()

    def __pow__(self, power):
        """Возведение кватерниона в целую степень"""
        if not isinstance(power, int):
            raise ValueError("Power must be an integer")
        else:
            if power == 0:
                return Quaternion(1, 0, 0, 0)
            elif power == 1:
                return self
            elif power > 1:
                result = self
                for _ in range(power - 1):
                    result *= self
                return result
            else:
                return self.inverse() ** (-power)


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
    #test_operation()

    q = Quaternion(1, 2, 3, 4)
    print(q * 5, 5 * q)

