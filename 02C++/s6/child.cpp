#include <iostream>
#include <unistd.h>
// child process
int main() 
{
    if (child_pid == -1) 
    {
        std::cout << "Fork failed." << std::endl;
        return 1;
    }

    if (child_pid == 0) 
    {
        // This code is executed in the child process
        std::cout << "Printed from child of PID : " << getpid() << std::endl;
    } 
    else 
    {
        std::cout << "Printed from Parent of PID: " << getpid() << "\n\t child PID: " << child_pid << std::endl;
    }

    return 0;
}
