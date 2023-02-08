#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d",&n);
    int c=0;
    int arr[n];
    for (int i=0;i<n;i++){
        
        scanf("%d",&arr[i]);
    }
   for (int i=0;i<n;i++){
        
       if (arr[i]%2==0){
           c++;
       }
   
    }
   
    printf("%d",c);

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
