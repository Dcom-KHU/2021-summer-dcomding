#include <iostream>
using namespace std;

void insertionSort(int arr[], int size) {
    int i, j, key;

    for (i = 1; i < size; i++) {
        key = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

int main() {
    int n, k, start, end, sum = 0;
	cin >> n >> k;
	int* num = new int[n];
	for (int i = 0; i < n; i++)
	{
		cin >> num[i];
	}
    insertionSort(num, n);
    start = (k - 1) / 2 + 1;
    end = start + (n - k);
    for (int i = start; i < end; i++)
    {
        sum += num[i];
    }
    cout << sum;
    return 0;
}