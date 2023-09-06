// 4- merge two arrays together
#include <iostream>
#include <vector>
#include <algorithm>

int main() 
{
    std::vector<int> vec1 = {9,2 ,3,4};
    std::vector<int> vec2 = {55,6,7,8};
    std::vector<int> mergedVec;

    // Ensure the destination vector has enough space to hold both vectors.
    mergedVec.resize(vec1.size() + vec2.size());

    // Use std::merge to merge the two vectors.
    // We may use insert as well
    std::merge(vec1.begin(), vec1.end(), vec2.begin(), vec2.end(), mergedVec.begin());

    std::cout << "Merged Vector: ";
    for (int num : mergedVec) 
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
