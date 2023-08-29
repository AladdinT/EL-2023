#include <iostream>
#include <string>

int main() {

    std::string vowels = "aeiouAEIOU";
    char input;
    
    std::cout << "Enter a character: ";
    std::cin >> input;
    
    if ( vowels.find(input) != std::string::npos ) {
        std::cout << "The entered character is a vowel." << std::endl;
    } else {
        std::cout << "The entered character is not a vowel." << std::endl;
    }
    
    return 0;
}
