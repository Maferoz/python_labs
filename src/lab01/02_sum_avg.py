a = (input("a:"))
b = (input("b:"))
a = float(a.replace(",","."))
b = float(b.replace(",","."))
summ = a + b
avg = summ/2
print(f"sum:{summ:.2f}; avg = {avg:.2f}")