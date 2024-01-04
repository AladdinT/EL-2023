#include <iostream>
#include <unistd.h>
// main process
int main() 
{
    // execv("./calc"); // same pid 

    
    // new process
    // system("ls"); // new
    int child_pid = fork(); // copy of the same code
    
    // pid = 995
    // main thread // new thread // thread 2

    int x = 10;
    if (child_pid == 0) 
    {
        // x = 20;
        std::cout << "Printed from child of PID : " << getpid()  << "\n x =  " << x << std::endl;
    } 
    else 
    {
        x = 30;  
        std::cout << "Printed from Parent of PID: " << getpid() << "\n x =  " << x<< "\n\t child PID: " << child_pid << std::endl;
    }

    return 0;
}
