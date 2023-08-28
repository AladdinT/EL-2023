from w2_skeleton_oop import MyComplex
from w2_skeleton_oop import AcPower

a = MyComplex( 1 , -2)
b = MyComplex( 2 , -2) 

# print( a == b )

p1 = AcPower(1 , 2 , 50)

print( p1.get_phase()  ) # Created new method 
print( p1.calc_magnitude()) # Called parent method
print(p1) # overwritten a parent method

p1.freq = 70 