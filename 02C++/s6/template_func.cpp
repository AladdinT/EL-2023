#include <iostream>

// Define a template function that finds the maximum of two values of any data type.
template <typename T>
T max(T a, T b) 
{
    return (a > b) ? a : b;
}

template <class T1, class T2>
T1 min(T1 a, T2 b) 
{
    std::cout<<__PRETTY_FUNCTION__ << " : ";
    return (a < b) ? a : b;
}

// template <>
char min(char a, char b) 
{
    std::cout<< "SPECIALIZED" << " : ";
    return (a < b) ? a : b;
}


int main() 
{
    int x = 5, y = 10;
    double a = 3.14, b = 2.71;

    // Use the max function with different data types
    std::cout << "Max of integers: " << max<int>(x, y) << std::endl;
    std::cout << "Max of doubles: " << max<double>(a, b) << std::endl;
    std::cout << "Max of char: " << max('a', 'z') << std::endl;
    // Use the min function with different data types
    std::cout <<  min(5, 10) << std::endl;
    std::cout <<  min(3.14, 5) << std::endl;
    std::cout <<  min('a', 66) << std::endl;
    std::cout <<  min<char,char>('a', 'z') << std::endl;
    std::cout <<  min('a', 'z') << std::endl;

    return 0;
}
