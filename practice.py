# Kodluyoruz python practice 2 :
# d = √(x₂-x₁)²+(y₂-y₁)²

# Öklid mesafesi, Öklid uzayındaki iki nokta arasındaki "sıradan" düz çizgi mesafesidir. Bu formül ile, düzlemde veya üç boyutlu uzayda iki nokta arasındaki mesafeyi bulabilirsiniz.

# Göreviniz:

# Python'da fonksiyonlar ve döngüler kavramlarını kullanarak, aşağıdaki işlemleri gerçekleştiren bir program yazmanız gerekmektedir:

# Noktaların Tanımlanması:

# ‘points’ adında bir liste oluşturun. Bu liste, 2D uzaydaki noktaları temsil eden demetler (tuple) içermelidir. Örneğin, ‘(x, y)’ noktası bir demet ‘(x, y)’ olarak temsil edilecektir.

# Öklid Mesafesi İçin Bir Fonksiyon Yazma:

# ‘euclideanDistance’ adında bir fonksiyon tanımlayın. Bu fonksiyon, iki demet (her biri bir noktayı temsil eder) almalı ve bu iki nokta arasındaki Öklid mesafesini döndürmelidir.

# Mesafelerin Hesaplanması:

# Bir döngü kullanarak, ‘points’ listesindeki her nokta çifti arasındaki Öklid mesafesini hesaplayın. Bu mesafeleri ‘distances’ adında başka bir listede saklayın.

# Minimum Mesafenin Bulunması:

# ‘distances’ listesinden minimum mesafeyi bulun ve yazdırın.


import math

# Noktaların Tanımlanması
points = [(1, 2), (4, 6), (5, 8), (9, 12), (3, 7)]

# Öklid Mesafesi İçin Bir Fonksiyon Yazma
def euclideanDistance(point1, point2):       # euclideanDistance fonksiyonu, iki nokta arasındaki Öklid mesafesini hesaplar.
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum Mesafenin Bulunması : distances listesindeki minimum mesafe bulunur ve yazdırılır.
min_distance = min(distances)
print(f"Minimum mesafe: {min_distance}")
