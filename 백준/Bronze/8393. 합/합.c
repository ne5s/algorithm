#include <stdio.h>

int main(){
    int a,x,y=0;
    scanf("%d", &x);
    for(a=1;a<=x;a++)
        y=y+a;
    
    printf("%d", y);
    
    return 0;
}