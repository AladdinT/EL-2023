#include <iostream>


class abc
{
 public:
  int x=10;
  int* ptr; //->int
  abc(){}
  
  abc(const abc& other) //copy constructor
  {
                                    //      Address inside ptr          whats inside the address (*ptr)
    int other_int = *(other.ptr);   //ptr = 0x1234                  -> 5
    this->ptr = new int(other_int); //ptr = 0x4321                  -> 5

   	this->ptr = new int(*other.ptr); 
  }




  abc(abc* other) //pass by ref
  {
   	this->ptr = new int; 
  }

//   abc(abc other)
//   {
//    	this->ptr = new int(*(other).ptr); 
//   }

    void operator+( abc& other)
    {
        other.x = 11;
    }

    abc& operator=(const abc& other)
    {
        this->ptr = new int(*other.ptr);
        this->x = other.x; 
        return *this;
    } 

    abc* operator=(const abc* other)
    {
        this->ptr = new int(*(*other).ptr);
        this->x = (*other).x; 
        return this;
    }


    static int & func(abc *  other)
    {
        return (*other).x;
    }
    

  
};


int main ()
{
    abc obj;
    abc obj1;
    //    abc& operator=(const abc& other)

    std::cout << &(obj)  << std::endl;
    // tempobj = *obj (*this)
    abc obj3; 
    obj3 = obj = obj1;
    // obj3 = obj.operator=(obj1)
    // obj3 = (obj)
    // obj3.operator=(obj)
    // (obj3)

    // int x = 5;
    std::cout << &(obj = obj1) << std::endl;
    // std::cout << &obj3  << std::endl;
    // std::cout << *(abc::func(&obj)) << std::endl;


    return 0;
}

