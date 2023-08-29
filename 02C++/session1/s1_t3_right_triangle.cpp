#include <iostream>

int main (void)
{
    int a , b , c;
    std::cout << "Enter The three sides of a triangle : ";
    std::cin >> a >> b >> c ;

    if (a <= 0 || b <= 0 || c <= 0) 
    {
        return false;  // Lengths must be positive
    }

    // Find the squares of the lengths
    int aSquared = a * a;
    int bSquared = b * b;
    int cSquared = c * c;

    // Check the Pythagorean theorem
    if ( (aSquared + bSquared == cSquared) || (aSquared + cSquared == bSquared) || (bSquared + cSquared == aSquared) )
    {
        std::cout << a << " , " << b << " , " << c << " Can form a right angle triangle" << std::endl ; 
    }
    else
    {
        std::cout << a << " , " << b << " , " << c << " Can not form a right angle triangle" << std::endl ; 
    }

    return 0;
}