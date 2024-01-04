#include <iostream>
#include <cstdlib>

int main() {
    // Use the scrot command to take a screenshot and save it as "screenshot.png"
    // You can customize the filename and options as needed
    const char* command = "scrot screenshot.png";
    
    int result = std::system(command);
    
    if (result == 0) {
        std::cout << "Screenshot saved as screenshot.png" << std::endl;
    } else {
        std::cerr << "Failed to take a screenshot." << std::endl;
    }
    
    return 0;
}
