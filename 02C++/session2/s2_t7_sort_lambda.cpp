// Sort with Lambda: Use lambda functions to sort an array of integers in ascending and descending order.

#include <iostream>
#include <vector>
#include <algorithm>

int main() 
{
    std::vector<int> arr = {5, 2, 9, 1, 5, 6, 3, 8, 4, 7};

    auto ascending = [](int a, int b) -> bool { return a < b; };
    auto descending = [](int a, int b) -> bool { return a > b; };

    // Ascending order
    std::sort(arr.begin(), arr.end(), ascending );

    std::cout << "Ascending order: ";
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // Descinding
    std::sort(arr.begin(), arr.end(), descending);

    std::cout << "Descending order: ";
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
