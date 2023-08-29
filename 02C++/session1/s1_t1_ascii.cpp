#include <iostream>
#include <iomanip>

int main() {
    std::cout << "ASCII Table" << std::endl;
    std::cout << "-----------" << std::endl;
    
    // Print header
    std::cout << "\tChar\t|\tASCII" << std::endl;
    std::cout << "------------------------------" << std::endl;

    // Print ASCII table
    for (int i = 0; i <= 127; ++i) {
        // std::cout << "\t" << static_cast<char>(i) << "\t|\t" << (i) << std::endl;
        printf("\t %c \t | \t %d\n",i,i);
    }

    return 0;
}
