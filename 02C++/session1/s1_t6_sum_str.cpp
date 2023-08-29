#include <iostream>
#include <string>


int main() 
{
    std::string input;

    std::cout << "Enter a string of digits: ";
    std::cin >> input;

    int sum = 0;

    for (char digit : input) 
    {
        sum += std::stoi(std::string(1, digit)); // Convert char digit to integer
    }

    std::cout << "Sum of digits: " << sum << std::endl;

    return 0;
}
