#include <stdio.h>

int main()
{
    int width, length;

    printf("Enter rectangle width: ");
    scanf("%d", &width);

    printf("Enter rectangle length: ");
    scanf("%d", &length);

    int area = width * length;
    int perimeter = (width + length) * 2;

    printf("Area = %d\n", area);
    printf("Perimeter = %d\n", perimeter);

    return 0;
} 

// gcc rectangle.c -o rect