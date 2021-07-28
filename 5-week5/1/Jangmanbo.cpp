#include <iostream>
#include <vector>
using namespace std;


int main() {
	vector<int> vec;
	string str;
	cin >> str;
	int size = str.size();
	for (int i = 0; i < size; i++)
		vec.push_back(str[i] - '0');

	int num = 1;
	int bef = vec[0];
	for (int i = 1; i < size; i++)
	{
		if (vec[i] != bef) {
			num++;
			bef = vec[i];
		}
	}
	cout << num / 2;
	return 0;
}