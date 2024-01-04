#include <iostream>
#include <algorithm>

class MyVector {
private:
    int* data;      // Pointer to dynamically allocated array
    size_t size;    // Number of elements in the array

public:
    // Default constructor
    MyVector() : data(nullptr), size(0) {}

    // Constructor with size
    MyVector(size_t sz) : data(new int[sz]), size(sz) 
    {
        std::fill(data, data + size, 0);
    }

    // Destructor (Rule 1)
    ~MyVector() {
        delete[] data;
    }

    // Copy constructor (Rule 2)
    MyVector(const MyVector& other) : data(new int[other.size]), size(other.size) {
        std::copy(other.data, other.data + other.size, data);
    }

    // Copy assignment operator (Rule 3)
    MyVector& operator=(const MyVector& other) {
        if (this != &other) { // Self-assignment check
            // Deallocate existing resources
            delete[] data;

            // Allocate new resources
            size = other.size;
            data = new int[size];

            // Copy data from other object
            std::copy(other.data, other.data + other.size, data);
        }
        return *this;
    }

    // Move constructor (Rule 4)
    MyVector(MyVector&& other) noexcept : data(nullptr), size(0) {
        // Steal the resources from 'other'
        swap(*this, other);
    }

    // Move assignment operator (Rule 5)
    MyVector& operator=(MyVector&& other) noexcept {
        // Swap resources with 'other'
        swap(*this, other);
        return *this;
    }

    // Member function to swap resources between two objects
    friend void swap(MyVector& first, MyVector& second) noexcept {
        std::swap(first.data, second.data);
        std::swap(first.size, second.size);
    }

    // Other member functions as needed...
};

int main() {
    MyVector vec1(5); // Create a MyVector with 5 elements
    MyVector vec2(vec1); // Copy constructor

    MyVector vec3;
    vec3 = vec2; // Copy assignment operator

    MyVector vec4(std::move(vec3)); // Move constructor
    MyVector vec5;
    vec5 = std::move(vec4); // Move assignment operator

    // Note: vec3 and vec4 are in a valid but unspecified state after moving

    return 0;
}
