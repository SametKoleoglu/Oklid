import math

# Noktaların tanımlanması
points = [(10, 20), (30, 40), (50, 60), (70, 80), (90, 100)]

# Öklid mesafesi hesaplama fonksiyonu


def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = min(distances)
print(f"Minimum mesafe: {min_distance}")
