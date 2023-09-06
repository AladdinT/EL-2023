// 5-find the even and odd numbers in the array
#include <algorithm>
#include <iostream>
#include <vector>

int main() 
{
    std::vector<int> arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // Use std::partiion to separate even and odd numbers.
    auto midpoint = std::partition(arr.begin(), arr.end(), [](int x) 
    {
        return x % 2 == 0; // Predicate: even numbers
    });

    // Post Partition 
    for (auto i: arr) 
    {
        std::cout << i << " ";
    }
    
    // Print even numbers
    std::cout << "\nEven numbers: ";
    for (auto i = arr.begin(); i != midpoint; i++) 
    {
        std::cout << *i << " ";
    }
    std::cout << std::endl;

    // Print odd numbers
    std::cout << "Odd numbers: ";
    for (auto i = midpoint; i != arr.end(); i++) 
    {
        std::cout << *i << " ";
    }
    std::cout << std::endl;

    return 0;
}
