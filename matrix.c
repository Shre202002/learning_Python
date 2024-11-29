// Online C compiler to run C program online
#include <stdio.h>
#include <conio.h>



int main() {
    // Write C code here
    int i,j, a[3][3], s1=1,s2=1;
    printf("Enter Elelments in your matrix\n");
    for(i=0;i<3;i++){

        for(j=0; j<3; j++){

            printf("Enter the A[%d][%d]: ",i,j);
            scanf("%d",&a[i][j]);

            if(i==j)
             s1= s1 +a[i][j];
            else
             s2 = s2 + a[i][j];
        }
    }
    printf("Digonal Sum is: %d\n",s1);
    printf("Off Digonal Sum is: %d\n",s2);

    return 0;
}