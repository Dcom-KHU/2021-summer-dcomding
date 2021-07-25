#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n, start, end;
	vector<pair<int, int>> vec;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> start >> end;
		vec.push_back(make_pair(end, start));
	}
	sort(vec.begin(), vec.end());
	int size = vec.size(), time = 0, team = 0;
	for (int i = 0; i < size; i++)
	{
		if (time <= vec[i].second) {
			team++;
			time = vec[i].first;
		}
	}
	cout << team;

	return 0;
}