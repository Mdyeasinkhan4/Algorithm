#include <stdio.h>
int main()
{
    int arr[] = {2, 4, 6, 18, 28, 40, 112};
    int item = 40;
    int left, right, middle;
    left = 0;
    right = 6;
    while (left <= right)
    {
        middle = (left + right) / 2;
        if (arr[middle] == item)
        {
            printf("Item found at index: %d\n", middle);
            return 0;
        }
        else if (arr[middle] < item)
        {
            left = middle + 1;
        }
        else
        {
            right = middle - 1;
        }
    }
    printf("Item not found!");
    return 0;
}
