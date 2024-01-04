#include <iostream>
#include <cstring>

class MyString {
private:
    char* str; // Pointer to the dynamically allocated string
public:
    // Default constructor
    MyString() : str(nullptr) {}

    // Constructor that takes a C-string
    MyString(const char* s) {
        if (s != nullptr) {
            str = new char[strlen(s) + 1];
            strcpy(str, s);
        } else {
            str = nullptr;
        }
    }

    // Copy constructor
    MyString(const MyString& other) {
        if (other.str != nullptr) {
            str = new char[strlen(other.str) + 1];
            strcpy(str, other.str);
        } else {
            str = nullptr;
        }
    }

    // Move constructor
    MyString(MyString&& other) noexcept : str(other.str) {
        other.str = nullptr;
    }

    // Destructor
    ~MyString() {
        delete[] str;
    }

    // Copy assignment operator
    MyString& operator=(const MyString& other) {
        if (this != &other) { // Self-assignment check
            delete[] str; // Release existing resources
            if (other.str != nullptr) {
                str = new char[strlen(other.str) + 1];
                strcpy(str, other.str);
            } else {
                str = nullptr;
            }
        }
        return *this;
    }

    // Move assignment operator
    MyString& operator=(MyString&& other) noexcept {
        if (this != &other) { // Self-assignment check
            delete[] str; // Release existing resources
            str = other.str;
            other.str = nullptr;
        }
        return *this;
    }

    // Getter to access the string
    const char* c_str() const {
        return str;
    }
};

int main() {
    // Create and test MyString objects
    MyString str1("Hello, ");
    MyString str2("World!");

    MyString str3 = str1; // Copy constructor
    MyString str4;
    str4 = str2; // Copy assignment

    MyString str5 = std::move(str3); // Move constructor
    MyString str6;
    str6 = std::move(str4); // Move assignment

    std::cout << str5.c_str() << " " << str6.c_str() << std::endl;

    return 0;
}
