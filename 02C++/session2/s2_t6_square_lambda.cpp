// Define a lambda function to calculate the square of a number.


#include <iostream>

int main() 
{
    auto square = [](int x) -> int { return x * x; };

    int number = 5;

    std::cout << "The square of " << number << " is " << square(number) << std::endl;

    return 0;
}
