#include <iostream>
#include <signal.h>

void signal_callback_handler(int signum) {
   std::cout << " Caught signal " << signum << std::endl;
   // Terminate program
   exit(signum);
}

int main (void)
{
    /*TASK3: Handle a hotkey*/
    std::cout << "\n************\n";
    //Register signal and signal handler
    signal(SIGINT, signal_callback_handler);

    while(true){
        std::cout << "Program processing..." << std::endl;
        sleep(1);
    }


    return EXIT_SUCCESS;

    return 0;
}