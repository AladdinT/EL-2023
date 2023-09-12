#include <iostream>
#include <string>
// #include <functional>


#define  TRACE_ENTER  BackTrace::enter_func(__PRETTY_FUNCTION__)
#define  TRACE_EXIT    BackTrace::exit_func(__PRETTY_FUNCTION__)

class BackTrace
{
public:
    BackTrace(std::string name) :  name(name) 
    {
        depth ++;
        std::cout << depth << ": Called : " << name << std::endl;
    }
    ~BackTrace()
    {

    }

    static void enter_func(std::string name)
    {
        depth ++;
        std::cout << depth << ": Called : " << name << std::endl;
    }

    static void exit_func(std::string name)
    {
        std::cout << depth << ": Exited : " << name << std::endl;
        depth--;
    }

private:
    static int depth;
    // const static int depth2;
    
    std::string name;

};

int BackTrace::depth = -1;
// const int BackTrace::depth2 = 4;

void fun()
{
    BackTrace::enter_func(__PRETTY_FUNCTION__);
    BackTrace::exit_func(__PRETTY_FUNCTION__);

}
void fun1()
{
    TRACE_ENTER;
    fun();
    TRACE_EXIT;

}

int main ()
{   
    fun();
    fun1();
    fun();

    return 0;
}