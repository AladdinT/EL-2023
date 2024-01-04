#include <iostream>
#include <stdexcept>

// A function that is marked as noexcept
void myFunction(int x) noexcept {
    std::cout << 1/x << "This function does not throw exceptions." << std::endl;
}

// Another function that throws an exception
void mightThrowException() {
    throw std::runtime_error("This function might throw an exception.");
}

int main() {
    try {
        myFunction(2); // No exception is expected here
        mightThrowException(); // This function might throw an exception
    } catch (const std::exception& e) {
        std::cerr << "Caught an exception: " << e.what() << std::endl;
    }

    return 0;
}
