#include <iostream>
using namespace std;

void quickSort(int i, int j, int arr[])
{
    if (i >= j) return;
    int pivot = arr[(i + j) / 2];
    int left = i;
    int right = j;

    while (left <= right)
    {
        while (arr[left] < pivot) left++;
        while (arr[right] > pivot) right--;
        if (left <= right)
        {
            swap(arr[left], arr[right]);
            left++; right--;
        }
    }
    quickSort(i, right, arr);
    quickSort(left, j, arr);
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
    int n, k, start, end, sum = 0;
    cin >> n >> k;
    int* num = new int[n];
    for (int i = 0; i < n; i++)
    {
        cin >> num[i];
    }
    quickSort(0, n - 1, num);
    start = (k - 1) / 2 + 1;
    end = start + (n - k);
    for (int i = start; i < end; i++)
    {
        sum += num[i];
    }
    cout << sum;
    return 0;
}