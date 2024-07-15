# Diberikan nilai-nilai
B = 0.2  # medan magnet dalam tesla (T)
I = 5    # arus listrik dalam ampere (A)
theta = 90  # sudut antara medan magnet dan arus dalam derajat

# Konversi sudut dari derajat ke radian
import math
theta_rad = math.radians(theta)

# Hitung sin(theta)
sin_theta = math.sin(theta_rad)

# Hitung gaya magnetik per satuan panjang
f = B * I * sin_theta

# Cetak hasilnya
f
