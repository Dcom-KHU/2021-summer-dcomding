#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int n, k;
	cin >> n >> k;

	int* books = new int[n];
	vector<int> booktypes;

	for (int i = 0; i < n; i++) {
		cin >> books[i];
		if (find(booktypes.begin(), booktypes.end(), books[i]) == booktypes.end())
			booktypes.push_back(books[i]);
	}
	
	int type = booktypes.size();
	if (k > type)
		cout << type << endl;
	else
		cout << k << endl;

	return 0;
}