#include <stdio.h>
#include <string.h>
struct student
{
    int id, age;
    char name[20];
    float per;
} s[100];
int main()
{
    int i, j, n;
    printf("Enter Number of students you want to enter: ");
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        printf("Enter your ID: ");
        scanf("%d", &s[i].id);
        printf("Enter a Name: ");
        scanf("%s", s[i].name);
        printf("Enter age: ");
        scanf("%d", &s[i].age);
        printf("Enter percentage: ");
        scanf("%f", &s[i].per);
        printf("Your Data is Added..!;\n\n");
    }

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n-i-1 ; j++)
        {
            if (s[j].per > s[j + 1].per)
            {
                struct student r;
                r = s[j];
                s[j] = s[j + 1];
                s[j + 1] = r;
            }
        }
    }
    printf("\tID\t|\tNAME\t|\tAGE\t|\tPERCENTAGE\t|\n");

    for (i = 0; i < n; i++)
    {
        printf("\t%d\t|\t%s\t|\t%d\t|\t%f\t\n", s[i].id, s[i].name, s[i].age, s[i].per);
    }
}
