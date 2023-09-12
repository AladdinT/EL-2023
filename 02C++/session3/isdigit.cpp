#include <iostream>
#include <cctype> 

int main() 
{
    char character;

    std::cout << "Enter a character: ";
    std::cin >> character;

    if (std::isdigit(character)) 
    {
        std::cout << "The character is a digit." << std::endl;
    } 
    else 
    {
        std::cout << "The character is not a digit." << std::endl;
    }

    return 0;
}
