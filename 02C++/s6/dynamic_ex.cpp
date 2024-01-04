#include <iostream>

// Base class
class Animal {
public:
    virtual void makeSound() {
        std::cout << "Animal makes a sound" << std::endl;
    }
};

// Derived class
class Dog : public Animal {
public:
    void makeSound() override {
        std::cout << "Dog barks" << std::endl;
    }

    void fetch() {
        std::cout << "Dog fetches a ball" << std::endl;
    }
};

int main() {
    Animal* animal = new Dog();

    // Attempt a dynamic_cast to convert the base class pointer to a derived class pointer
    Dog* dog = dynamic_cast<Dog*>(animal);

    if (dog) {
        std::cout << "Successfully cast to Dog." << std::endl;
        dog->makeSound();
        dog->fetch();
    } else {
        std::cout << "Dynamic cast failed." << std::endl;
    }

    delete animal;

    return 0;
}
