def Pythagorean():
  ab = float(input("Enter the length of AB: "))
  ac = float(input("Enter the length of AC: "))
  bc = (ab**2 + ac**2)**0.5
  print(f"The length of BC (the hypotenuse) is {bc}")
Pythagorean()