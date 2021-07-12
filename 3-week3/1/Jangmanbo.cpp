#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n, k;
	cin >> n >> k;
	int* books = new int[n];
	for (int i = 0; i < n; i++)
	{
		cin >> books[i];
	}
	sort(books, books + n);

	int total = n;
	for (int i = 1; i < n; i++)
	{
		if (books[i - 1] == books[i]) total--;
	}
	cout << min(total, k);
	return 0;
}