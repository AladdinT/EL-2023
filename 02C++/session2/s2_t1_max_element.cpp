// 1- create a function to find the maximum number of array

#include <iostream>
#include <algorithm> // std::max_element
#include <vector>    

int getMax( int arr[], int size) 
{
    
    if (size <= 0) 
    {
        throw std::invalid_argument("Array is empty or invalid.");
    }

    int* maxElementPtr = std::max_element(arr, arr + size);

    return *maxElementPtr;
}


int getMax(std::vector<int> & vec) 
{
    if (vec.empty()) 
    {
        throw std::invalid_argument("Vector is empty.");
    }
    
    auto maxElement = std::max_element(vec.begin(), vec.end());

    return  *maxElement;
}

int main() 
{
    int arr[] = {6, 0 , 8 , 12 ,55 ,3 , 99 ,1 ,2 };
    int size = sizeof(arr) / sizeof(arr[0]);

    int max1 = getMax(arr, size);
    std::cout << "The maximum number in the array is: " << max1 << std::endl;

    // Using Vectors
    std::vector<int> vec = {6, 0 , 8 , 12 ,55 ,3 , 99 ,1 ,2 };
    int max2 = getMax( vec);
    std::cout << "The maximum number in the vector is: " << max2 << std::endl;

    return 0;
}
