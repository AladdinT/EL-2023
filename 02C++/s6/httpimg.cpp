#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

const int PORT = 8080;

// Function to read the image file into a string
std::string readImageFile(const std::string& filename) {
    std::ifstream file(filename, std::ios::binary);
    if (!file) {
        return "";
    }

    // Read the file into a string
    std::stringstream buffer;
    buffer << file.rdbuf();
    return buffer.str();
}

int main() {
    // Create a socket
    int serverSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (serverSocket == -1) {
        perror("Error creating socket");
        return 1;
    }

    // Bind the socket to a local address and port
    sockaddr_in serverAddress{};
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_port = htons(PORT);
    serverAddress.sin_addr.s_addr = INADDR_ANY;

    if (bind(serverSocket, (struct sockaddr*)&serverAddress, sizeof(serverAddress)) == -1) {
        perror("Error binding socket");
        return 1;
    }

    // Listen for incoming connections
    if (listen(serverSocket, 5) == -1) {
        perror("Error listening on socket");
        return 1;
    }

    std::cout << "HTTP server listening on port " << PORT << std::endl;

    while (true) {
        // Accept incoming connections
        int clientSocket = accept(serverSocket, nullptr, nullptr);
        if (clientSocket == -1) {
            perror("Error accepting connection");
            continue;
        }

        // Read the HTTP request
        char buffer[1024];
        ssize_t bytesRead = recv(clientSocket, buffer, sizeof(buffer), 0);

        if (bytesRead <= 0) {
            perror("Error reading request");
            close(clientSocket);
            continue;
        }

        // Parse the request (in a real server, you'd perform more robust parsing)

        // Prepare an HTTP response with an image
        std::string imageContent = readImageFile("screenshot.png");

        if (!imageContent.empty()) {
            std::string httpResponse = "HTTP/1.1 200 OK\r\n";
            httpResponse += "Content-Type: image/jpeg\r\n";
            httpResponse += "Content-Length: " + std::to_string(imageContent.size()) + "\r\n\r\n";
            httpResponse += imageContent;

            // Send the HTTP response with the image
            send(clientSocket, httpResponse.c_str(), httpResponse.length(), 0);
        } else {
            // Error: Could not read the image file
            std::string errorResponse = "HTTP/1.1 500 Internal Server Error\r\n\r\n";
            send(clientSocket, errorResponse.c_str(), errorResponse.length(), 0);
        }

        // Close the client socket
        close(clientSocket);
    }

    // Close the server socket (unreachable in this example)
    close(serverSocket);

    return 0;
}
