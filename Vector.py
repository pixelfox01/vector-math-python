from __future__ import annotations
import math


class Vector2D:

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def Dot(self, vector: Vector2D) -> float:
        return (self.x * vector.x) + (self.y * vector.y)

    def Magnitude(self) -> float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def Normalized(self) -> Vector2D:
        return Vector2D((1/self.Magnitude())*(self.x), (1/self.Magnitude())*(self.y))

    def IsOrthogonal(self, vector: Vector2D) -> bool:
        return True if self.Dot(vector) == 0 else False

    def AngleBetween(self, vector: Vector2D) -> float:
        return math.degrees(math.acos(self.Dot(vector)/(self.Magnitude()*vector.Magnitude())))

    def DisplayVector(self) -> str:
        return f'({self.x}, {self.y})'
