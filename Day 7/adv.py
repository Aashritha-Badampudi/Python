#Q) Using only arithmetic operations, separate a complex number into magnitude and angle (argument).
import math
z=3+5j
a=z.real
b=z.imag

magnitude=math.sqrt(a**2+b**2)
angle_radians=math.atan(b/a)
angle_degrees=math.degrees(angle_radians)

print("Real:",a,"\nImaginery:",b,"\nMagnitude:",magnitude,"\nAngle radians:",angle_radians,"\nAngle degrees:",angle_degrees)
