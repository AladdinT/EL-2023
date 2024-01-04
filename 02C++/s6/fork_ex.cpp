#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

void* thread_function(void* arg) {
    printf("Thread ID: %ld\n", (long)pthread_self());

    // Create a new process
    pid_t pid = fork();

    if (pid == 0) {
        // This code executes in the child process
        printf("Child process created. PID: %d\n", getpid());
    } else if (pid > 0) {
        // This code executes in the parent process
        printf("Parent process. Child PID: %d\n", pid);
    } else {
        // Fork failed
        perror("fork");
    }

    return NULL;
}

int main() 
{
    pthread_t thread;

    if (pthread_create(&thread, NULL, thread_function, NULL) != 0) {
        perror("pthread_create");
        return 1;
    }

    pthread_join(thread, NULL);

    return 0;
}