#include <iostream>
#include <algorithm>

int main() {
    int num1, num2, num3;
    
    std::cout << "Enter three numbers: ";
    std::cin >> num1 >> num2 >> num3;
    
    int maxNum = std::max(num1, std::max(num2, num3));
    
    std::cout << "The maximum number is: " << maxNum << std::endl;
    
    return 0;
}
