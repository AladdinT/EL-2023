#include <functional>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <stdexcept>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <fstream>
#include <unistd.h>
#include <sstream>

// Function to read the image file into a string
std::string readImageFile(const std::string& filename) 
{
    std::ifstream file(filename, std::ios::binary);
    if (!file) 
    {
        return "";
    }

    // Read the file into a string
    std::stringstream buffer;
    buffer << file.rdbuf();
    return buffer.str();
}

int main() {
    int serverSocket, clientSocket;
    struct sockaddr_in serverAddr, clientAddr;
    socklen_t clientAddrLen = sizeof(clientAddr);

    // Create socket
    serverSocket = socket(AF_INET, SOCK_STREAM, 0);
    // socket descriptor (like a file-handle) = 
    // domain: 
    //      AF_ LOCAL : for communication on the same host. 
    //      AF_INET   : for different hosts connected by IPV4.
    //      AF_I NET 6 : for processes connected by IPV6.
    // type: communication type
    //      SOCK_STREAM: TCP(reliable, connection oriented)
    //      SOCK_DGRAM: UDP(unreliable, connectionless)
    // protocol: Protocol value for Internet Protocol(IP), which is 0.
    
    if (serverSocket == -1) {
        // perror("Error creating socket");
        // exit(EXIT_FAILURE);
    }

    // Bind socket to a port
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(8080);
    serverAddr.sin_addr.s_addr = INADDR_ANY; //localhost
    
    if (bind(serverSocket, (struct sockaddr*)&serverAddr, sizeof(serverAddr)) == -1) 
    {
        throw std::runtime_error("Error binding socket\n");
    }

    // Listen for incoming connections
    if (listen(serverSocket, 5) == -1) 
    {
        throw std::runtime_error("Error listening\n");
    }

    std::cout << "Server listening on port " << ntohs(serverAddr.sin_port) << std::endl;
    
    // Accept incoming connection
    clientSocket = accept(serverSocket, (struct sockaddr*)&clientAddr, &clientAddrLen);
    if (clientSocket == -1) 
    {
        throw std::runtime_error("Error accepting connection\n");
    }
    else
    {
        std::cout << " Client connection accepted \n " 
        << "client: " << clientSocket << '\n'
        << "Address: " << clientAddr.sin_addr.s_addr << '\n'
        << std::endl;
    }

    // Send a message to the client
    // std::string httpResponse = "HTTP/1.1 200 OK\r\n  \
    //                             Content-Type: text/html\r\n";

    // httpResponse += "Content-Length: " + std::to_string(strlen("<html><body><h1>Hello, World!</h1></body></html>")) + "\r\n\r\n";
    // httpResponse += "<html><body><h1>Hello, World!</h1> </body></html>";
    // Prepare an HTTP response with an image
    
    std::string imageContent = readImageFile("screenshot.ppm");

    if (!imageContent.empty()) 
    {
        std::string httpResponse = "HTTP/1.1 200 OK\r\n";
        httpResponse += "Content-Type: image/jpeg\r\n";
        httpResponse += "Content-Length: " + std::to_string(imageContent.size()) + "\r\n\r\n";
        httpResponse += imageContent;

        // Send the HTTP response with the image
        const char* message = httpResponse.c_str();
        send(clientSocket, message , strlen(message) , 0);
   
    }
    // const char* message = httpResponse.c_str();

    // send(clientSocket, message , strlen(message) , 0);
    // send(clientSocket, message, strlen(message), 0);

    // Receive data from the client
    char buffer[1024];
    while(1)
    {    
        // ssize_t bytesRead = recv(clientSocket, buffer, sizeof(buffer), 0);

        // if (bytesRead <= 0) {
        //     perror("Error receiving data\n");
        //     break;
        // } else {
        //     buffer[bytesRead] = '\0';
        //     std::cout << "Received from client: " << buffer << std::endl;
        // }
    }
    // Close sockets
    close(clientSocket);
    close(serverSocket);

    return 0;
}
