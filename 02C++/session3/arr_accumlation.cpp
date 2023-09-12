#include <iostream>
#include <array>
#include <numeric>


int main (void)
{
    int arr[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
    int n = 7, sum = 0;

    sum = std::accumulate(arr, arr+n, sum);

    std::cout << "arr = {" ;
    for(int i: arr )
    {
        std::cout << i << ",";
    }
    std::cout<<"}\nThe array sum is "<<sum << std::endl;

    
    return 0;
}