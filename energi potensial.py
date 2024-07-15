import math

# Diberikan data
massa_bola = 2  # kg
percepatan_gravitasi = 9.8  # m/s^2
ketinggian = 20  # meter

# 1. Menghitung energi potensial gravitasi
energi_potensial = massa_bola * percepatan_gravitasi * ketinggian
print(f"Energi potensial gravitasi bola sebelum dijatuhkan: {energi_potensial} Joule")

# 2. Menghitung kecepatan bola tepat sebelum menyentuh tanah
# Menggunakan prinsip konservasi energi
# Energi potensial awal = Energi kinetik akhir
# EP = EK => m * g * h = 0.5 * m * v^2
# => v^2 = 2 * g * h
# => v = sqrt(2 * g * h)

kecepatan = math.sqrt(2 * percepatan_gravitasi * ketinggian)
print(f"Kecepatan bola tepat sebelum menyentuh tanah: {kecepatan} m/s")
