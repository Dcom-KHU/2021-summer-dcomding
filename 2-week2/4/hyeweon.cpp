#include <iostream>
#include <string>
using namespace std;

int main()
{
	int n;
	cin >> n;

	string* items = new string[n];
	string* types = new string[n];
	int* count = new int[n];
	int types_index = 0;
	bool newtype = true;

	int start = 0;
	int end = 0;
	int min_start = 0;
	int min_end = n;
	bool zerotype = false;

	for (int i = 0; i < n; i++) {
		cin >> items[i];
		for (int j = 0; j < types_index; j++) {
			if (items[i] == types[j]) {
				newtype = false;
				break;
			}
		}
		if (newtype == true) {
			types[types_index] = items[i];
			count[types_index] = 0;
			types_index++;
		}
		newtype = true;
	}

	for (; end < n; end++) {
		for (int j = 0; j < types_index; j++) {
			if (items[end] == types[j]) {
				count[j]++;
				if (zerotype == true)
					break;
			}
			else if (count[j] == 0) {
				zerotype = true;
			}
		}

		if (zerotype == false) {
			for (int j = 0; j < types_index;) {
				if (items[start] == types[j]) {
					if (count[j] > 1) {
						count[j]--;
						start++;
						j = 0;
					}
					else
						break;
				}
				else
					j++;
			}

			if (min_end - min_start > end - start) {
				min_start = start;
				min_end = end;
			}
		}
		zerotype = false;
	}

	cout << min_start + 1 << endl;
	cout << min_end + 1 << endl;
}