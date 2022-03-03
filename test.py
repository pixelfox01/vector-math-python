from Vector2D import Vector2D

v1 = Vector2D(1, 0)
v2 = Vector2D(0, 1)

print(v1.Dot(v2))
print(v1.IsOrthogonal(v2))
print(v1.Magnitude())
print(v1.Normalized().DisplayVector())
print(v1.AngleBetween(v2))
