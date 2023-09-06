// 2- create a function to search to the number in the array which number is taken from user
#include <cstddef>
#include <iostream>
#include <algorithm> // For std::find
#include <vector>

bool searchNumber(const std::vector<int>& vec, int to_find , int* index= nullptr) 
{
    
    auto found = std::find(vec.begin(), vec.end(), to_find);

    if( index != nullptr )
    {
        if(found != vec.end())
        {
            *index  = std::distance(vec.begin(), found) ;
        }
        else 
        {
            *index = -1; 
        }
    }

    // If std::find returns vec.end(), the number was not found.
    return( found != vec.end() );
}

int main() 
{
    std::vector<int> vec = {11, 22 , 33 ,44 ,55 ,66 ,77 ,88};
    int to_find;
    int index;

    std::cout << "Enter a number to search for: ";
    std::cin >> to_find;

    bool found = searchNumber(vec, to_find , &index );

    if (found) 
    {
        std::cout << "The number " << to_find << " was found in vector["<< index << "]." << std::endl;
    } 
    else 
    {
        std::cout << "The number " << to_find << " was not found in the vector." << std::endl;
    }

    return 0;
}
