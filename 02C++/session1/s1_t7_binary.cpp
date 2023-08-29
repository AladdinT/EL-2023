#include <iostream>
#include <bitset>

int main (void)
{
    int deci;
     
    std::cout << "Enter a decimal value : ";
    std::cin >> deci;
    
    std::bitset<8> mybin(deci);
    std::cout << deci << " -binary-> " << mybin << std::endl;

    std::string binaryValue;

    std::cout << "Enter a binary number: ";
    std::cin >> binaryValue;

    std::bitset<32> bits(binaryValue);
    int decimalValue = bits.to_ulong();

    std::cout << binaryValue << " -decimal-> " << decimalValue << std::endl;
}