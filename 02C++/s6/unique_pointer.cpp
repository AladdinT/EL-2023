#include <iostream>
#include <memory>

namespace 
{
    int x=10;
    namespace  
    {
        int x=20;
        int y=20;
        void display()
        {
            std::cout << ::x << std::endl; 
        }
    }
}
class Foo
{
    int x;
    public :
    explicit Foo(int x) : x(x)
    {

    }
    int getX ()
    {
        return x;
    }
    ~Foo() 
    {
        std::cout << __PRETTY_FUNCTION__ << '\n';
    }
};

int main ()
{
    std::cout << "Hello world" << std::endl;
    Foo * raw = new Foo(11);
    std::shared_ptr<Foo> ptr (raw);
    std::shared_ptr<Foo> ptr2 (ptr);
    // ptr.reset();

    std::cout << ptr2.use_count()<< '\n';
    std::cout << ptr2->getX() << '\n';
    
    std::cout << "\n*********\n";
    
    std::cout << ::x << "\n*********\n";
    ::x = 55;
    ::x=11;
    display();

    return 0;
}


