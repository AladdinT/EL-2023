import math 

class MyComplex:
    '''
    DOC:
    '''  
    # Arrtibutes
    real = 0
    img = 0
    __mag = 0  # private att.
    angle = 0
    ### constructor    # def __init__(self, real, img):
    def __init__(self, in_real, in_img):
        # Attributes
        # print("Constructor")
        self.real = in_real
        self.img  = in_img
        self.__angle = 0
        
        
    
    ### destructor     # def __del__(self):
    def __del__(self):
        # print("destructor")
        del self

    # Methods         # def calc_angle(self) -> float
    def calc_magnitude(self):
        return math.sqrt( self.real**2 + self.img**2 )
    
    # def mag_setter(self, mag):
    #     self.__mag = mag
    #     self.real

    # def mag_getter(self):
    #     return self.__mag
    
    ## @property
    @property
    def magnitude(self):
        print("getter")
        return self.__mag
    
    @magnitude.setter
    def magnitude(self, value):
        self.__mag = value
    
    
    #### dunder functions    #def __str__(self):
    def __str__(self) -> str:
        if self.img >= 0:
            return str(f"{self.real} + {self.img}  i")
        else:
            return str(f"{self.real} - {self.img * -1}  i")
    
    def __len__(self):
        pass
    
    # @staticmethod          #def get_polar_form(obj)-> list:
    @staticmethod
    def clac_mag(real , imag):
        return math.sqrt( real**2 + imag**2 )
    
    #### operator overloading     #def __add__(self, operand):
    def __add__(self, other):
       res_real = self.real + other.real
       res_img = self.img + other.img
       return MyComplex(res_real , res_img)
       
    
    def __eq__(self, other) -> bool:
        if self.real == other.real and self.img == other.img:
            return True
        else:
            return False

# Inheritance
# AcPower is MyComplex
class AcPower(MyComplex):
    _freq = 0
    def __init__(self, real, img , freq):
        super().__init__(real, img)
        self._freq = freq
        

    def __del__(self):
        super().__del__()
        del self
    
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
        return super().angle


    def __str__(self): # Polymorphism
        return str(f"Passive Watts : {self.real} , Active Watts {self.img} , and f={self.freq} Hz")
    

# encapsulation
# Abstraction
# Inheritance
# Polymorphism -> Poly , morphism