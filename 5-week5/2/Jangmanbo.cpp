#include <iostream>
#include <vector>
using namespace std;

int n, maximum = 0;
vector<int> boxes;

void func(int idx, int bottom, int total) {
	if (n == idx) {
		if (total > maximum) maximum = total;
		return;
	}
	for (int i = idx; i < n; i++)
	{
		if (boxes[i] > bottom) {
			func(i + 1, boxes[i], total + 1);
		}
	}
}

int main() {
	int num;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> num;
		boxes.push_back(num);
	}
	func(0, 0, 0);
	cout << maximum;
	return 0;
}