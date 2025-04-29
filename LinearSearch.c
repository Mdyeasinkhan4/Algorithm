#include <stdio.h>
int main()
{
    int a[] = {12, 5, 188, -3, 10, 6};
    int SearchItem = 188;
    int i;
    for (i = 0; i < 6; i++)
    {
        if (a[i] == SearchItem)
        {
            printf("Item found at index: %d\n", i);
            return;
        }
    }
    printf("Item not found!");
    return 0;
}