def Energy():
  C =  299792458
  mass = float(input("Enter the mass in Kg: "))
  Energy = mass*C**2
  print(f"The energy in Joules is {Energy}")
Energy()