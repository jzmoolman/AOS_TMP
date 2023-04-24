#include <unistd.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    pid_t pid = fork();

    if (pid == 0) {
        printf("I'm the child and my pid is %d.\n", getpid());
    } else {
        printf("My child is id %d, and I'm %d\n", pid, getpid());
    }
}
