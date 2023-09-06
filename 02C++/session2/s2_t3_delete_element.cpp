// 3- delete number in array
#include <iostream>
#include <algorithm>
#include <vector>

int main() 
{
    std::vector<int> vec = {1, 2,3,4,5,5,5,7 };
    int numberToDelete = 5;

    std::cout << "Before : \n";
    for (int num : vec) 
    {
        std::cout << num << " ";
    }
    
    // Use std::remove to move elements to be deleted to the end.
    auto newEnd = std::remove(vec.begin(), vec.end(), numberToDelete);
    
    // Use std::erase to remove the elements from the vector.
    vec.erase(newEnd, vec.end());

    std::cout << "\nAfter erasing " << numberToDelete << ":\n";
    for (int num : vec) 
    {
        std::cout << num << " ";
    }

    std::cout << std::endl;
    return 0;
}
