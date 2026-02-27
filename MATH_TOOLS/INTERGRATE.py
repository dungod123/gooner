import sympy as sp 
x=sp.Symbol('x')
s=input("nhap bieu thuc theo x")
nguyen_ham=sp.integrate(s,x)
print("Nguyên hàm của x^2 là:", nguyen_ham) 

tich_phan = sp.integrate(sp.sin(x), (x, 0, sp.pi))
print("Tích phân sin(x) từ 0 đến pi là:", tich_phan) 