import math 

class MyComplex:
    '''
    DOC:
    This class is our implementation of complex class just to study oop
    '''
    def __init__(self, real, img):
        #constructor
        # initialze object with real/img data
        # private members
        self._real = real
        self._img = img

    def __del__(self):
        #destructor
        print("deleteing instance")
        del self

    @property
    def real(self) -> float:
        return self._real

    @real.setter
    def real(self, real):
        self._real = real

    @property
    def img(self) -> float:
        return self._img

    @img.setter
    def img(self, img):
        self._img = img
    
    def get_magnitude(self) -> float:
        # method to calculate magnitude
        return math.sqrt( self._real**2 + self._img**2 )

    def get_angle(self) -> float:
        # method to calculate magnitude
        if self._img != 0:
            return math.degrees( math.tan( self._img / self._real)  )
        else:
            return 0 if self._real > 0 else 180     

    #### dunder functions ####
    # doc
    def __str__(self):
        if self._img >= 0:
            return str(f"{self._real} + {self._img} i")
        else:
            return str(f"{self._real} - {self._img} i")

    # static method
    @staticmethod
    def get_polar_form(obj)-> list:
        print(f"{obj.get_magnitude()} ∠ {obj.get_angle()}°")
        return [ obj.get_magnitude(), obj.get_angle() ]
    
    def get_polar_form(self)-> list:
        print(f"{self.get_magnitude()} ∠ {math.degrees(self.get_angle())}°")
        return [self.get_magnitude() , self.get_angle()]
    
    # proberty
    
    #### operator overloading ####
    def __add__(self, operand):
        return MyComplex(self._real + operand.real , self._img  + operand.img)
    
    def __mul__(self):
        pass
        
    def __eq__(self, operand):
        if self._real == operand.real and self._img == operand.img:
            return True
        else:
            return False

class AcPower(MyComplex):
    def __init__(self, real, img , freq):
        super().__init__(real, img)
        if freq >= 0:
            self._freq = freq
        else:
            raise "Invalid frequency"

    @property
    def freq(self) -> float:
        return self._freq
    
    @freq.setter
    def freq(self , freq):
        if freq >= 0:
            self._freq = freq
        else:
            raise "Invalid frequency"

    def get_phase(self) -> float:
        print("Iam super " + str(super().img))
        return super().get_angle()

    def __str__(self):
        return str(f"Passive Watts : {self._real} , Active Watts {self._img} , and f={self.freq} Hz")
    
    

if __name__==  '__main__':
    a = MyComplex( 5 , 4)
    b = MyComplex( 1 , 2)

    print(a)
    print(a + b)
    print(a == b)
    print(a.get_angle())
    print(b.get_magnitude())
    
    a.real = 2
    print(a.real)
    print(a.__doc__)
    MyComplex.get_polar_form(a)
    a.get_polar_form()

    p1 = AcPower(5 , 4, 50)
    p2 = AcPower(2 , 3, 50)
    
    print(p1)
    print(p1.get_phase())
    print((p1+p2))