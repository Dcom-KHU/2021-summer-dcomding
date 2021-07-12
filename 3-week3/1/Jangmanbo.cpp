#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int n, k, before, total = 1;
	cin >> n >> k;
	int* books = new int[n];
	for (int i = 0; i < n; i++)
	{
		cin >> books[i];
	}
	sort(books, books + n);

	before = books[0];
	for (int i = 1; i < n; i++)
	{
		if (before != books[i])
		{
			total++;
			before = books[i];
			if (total == k) break;
		}
	}
	cout << total;
	return 0;
}