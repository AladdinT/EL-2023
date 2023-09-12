#include <iostream>
#include <array>
#include <numeric>

int main (void)
{
    /*TASK1: Initialize an array with numbers from 10 to 10000*/
    std::array<int, 9991/*10000-10+1*/ > a;
    std::iota(a.begin(), a.end(), 10);

    for(int i: a )
    {
        //std::cout << i << ",";
    }
    std::cout << std::endl;


    return 0;
}