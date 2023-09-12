#include <iostream>
#include <algorithm>
#include <array>

int main() 
{
    std::array<int, 5> arr = {2, 4, 3, 8, 10}; 

    // std::all_of : Checks if unary predicate p returns true for all elements in the range [first, last).

    bool allEven = std::all_of(arr.begin(), arr.end(), [](int num) {
        return num % 2 == 0;
    });

    if (allEven) 
    {
        std::cout << "All elements in the array are even." << std::endl;
    } 
    else 
    {
        std::cout << "Not all elements in the array are even." << std::endl;
    }

    return 0;
}
