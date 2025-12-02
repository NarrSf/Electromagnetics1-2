#از آنجا که مقاله مورد بحث ماهیت اثباتی و نظری داشت و امکان کدنویسی مستقیم برای خود اثبات وجود نداشت، این کدها
#صرفاً به منظور بصری‌سازی و کمک به درک بهتر مفاهیم مرتبط (مانند میدان‌ها و برهم‌کنش‌ها) ارائه گردیدند. لازم به ذکر است که 
# برای سادگی در فهم مراحل، توضیحات هر بخش از کد به عنوان کامنت، مستقیماً در کنار کدها قرار داده شده است


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# مثال 1: بصری‌سازی میدان الکتریکی ناشی از یک بار نقطه‌ای

def electric_field_point_charge(charge_pos, charge_q, X, Y, Z):
 
    # بردار از موقعیت بار تا هر نقطه در شبکه
    Rx = X - charge_pos[0]
    Ry = Y - charge_pos[1]
    Rz = Z - charge_pos[2]
    R_mag = np.sqrt(Rx**2 + Ry**2 + Rz**2)

    # برای جلوگیری از تقسیم بر صفر در محل بار، قدر مطلق فاصله را بی‌نهایت می‌کنیم
    R_mag[R_mag == 0] = np.inf

    # اندازه میدان الکتریکی E = k * q / r^2 (برای سادگی k=1 در نظر گرفته شده است)
    E_mag = charge_q / R_mag**2

    # مؤلفه‌های میدان الکتریکی 
    Ex = E_mag * (Rx / R_mag)
    Ey = E_mag * (Ry / R_mag)
    Ez = E_mag * (Rz / R_mag)

    return Ex, Ey, Ez

# تنظیمات و اجرای بصری‌سازی میدان الکتریکی 
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# ایجاد شبکه نقاط در فضای سه‌بعدی
x = np.linspace(-2, 2, 8) # نقطه در هر بعد
y = np.linspace(-2, 2, 8)
z = np.linspace(-2, 2, 8)
X, Y, Z = np.meshgrid(x, y, z)

# تعریف مشخصات بار نقطه‌ای
charge_pos = np.array([0, 0, 0]) # بار در مبدأ مختصات
charge_q = 1.0  # بار مثبت

# محاسبه مؤلفه‌های میدان الکتریکی
Ex, Ey, Ez = electric_field_point_charge(charge_pos, charge_q, X, Y, Z)

# رسم بردارهای میدان
ax.quiver(X, Y, Z, Ex, Ey, Ez, length=0.5, normalize=True, color='blue', arrow_length_ratio=0.3)

# رسم موقعیت بار
ax.scatter(charge_pos[0], charge_pos[1], charge_pos[2], color='black', s=100, label='Electric charge')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Electric field due to an electric charge')
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.legend()
plt.show() 

# مثال 2: بصری‌سازی میدان مغناطیسی ناشی از یک دوقطبی مغناطیسی 

def magnetic_field_dipole(dipole_moment, X, Y, Z):
   
    mu0_over_4pi = 1.0 

    Rx = X
    Ry = Y
    Rz = Z
    R_mag_sq = Rx**2 + Ry**2 + Rz**2
    R_mag = np.sqrt(R_mag_sq)

    # برای جلوگیری از تقسیم بر صفر در محل دوقطبی
    R_mag[R_mag == 0] = np.inf
    R_mag_cubed = R_mag**3
    R_mag_fifth = R_mag**5

    # مؤلفه‌های گشتاور دوقطبی
    mx, my, mz = dipole_moment

    m_dot_r = (mx*Rx + my*Ry + mz*Rz)

    # محاسبه مؤلفه‌های میدان مغناطیسی
    Bx = mu0_over_4pi * (3 * m_dot_r * Rx / R_mag_fifth - mx / R_mag_cubed)
    By = mu0_over_4pi * (3 * m_dot_r * Ry / R_mag_fifth - my / R_mag_cubed)
    Bz = mu0_over_4pi * (3 * m_dot_r * Rz / R_mag_fifth - mz / R_mag_cubed)

    return Bx, By, Bz

# تنظیمات و اجرای بصری‌سازی میدان مغناطیسی 
fig2 = plt.figure(figsize=(10, 8))
ax2 = fig2.add_subplot(111, projection='3d')

# ایجاد شبکه نقاط
x = np.linspace(-2, 2, 8)
y = np.linspace(-2, 2, 8)
z = np.linspace(-2, 2, 8)
X, Y, Z = np.meshgrid(x, y, z)

# تعریف گشتاور دوقطبی مغناطیسی 
dipole_moment = np.array([0.0, 0.0, 1.0])

# محاسبه مؤلفه‌های میدان مغناطیسی
Bx, By, Bz = magnetic_field_dipole(dipole_moment, X, Y, Z)

# رسم بردارهای میدان
ax2.quiver(X, Y, Z, Bx, By, Bz, length=0.5, normalize=True, color='purple', arrow_length_ratio=0.3)

# رسم موقعیت دوقطبی (مبدأ)
ax2.scatter(0, 0, 0, color='black', s=100, label='Magnetic dipole')

ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('Magnetic field due to a dipole')
ax2.set_xlim([-2, 2])
ax2.set_ylim([-2, 2])
ax2.set_zlim([-2, 2])
ax2.legend()
plt.show() 
