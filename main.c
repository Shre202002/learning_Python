// write a c program to find the square by n numbers using calloc() function
#include <stdio.h>
#include <stdlib.h>
int main()
{
    int a,b;
    a= 20;
    b =  20;
    printf("Before swapping: a = %d, b = %d\n", a, b);
    swapping(&a, &b);
    printf("After swapping: a = %d, b = %d\n", a, b);
    return 0;
}
 void swapping(int *a, int *b){
     int *temp = *a;
        *a = *b;
        *b = temp;
 }
