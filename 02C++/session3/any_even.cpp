#include <iostream>
#include <algorithm>
#include <array>

int main() 
{
    std::array<int, 5> arr = {1, 3, 5, 7, 8}; 

    // std::any_of to check if any element is even
    bool anyEven = std::any_of(arr.begin(), arr.end(), [](int num) {
        return num % 2 == 0;
    });

    if (anyEven) 
    {
        std::cout << "There is at least one even value in the array." << std::endl;
    }
    else 
    {
        std::cout << "There are no even values in the array." << std::endl;
    }

    return 0;
}
