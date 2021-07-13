#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	int n, t, m, k, hour, minute;
	vector<int> table;
	cin >> n >> t >> m >> k;

	//time table 입력, 정렬
	for (int i = 0; i < k; i++)
	{
		cin >> hour >> minute;
		table.push_back(hour * 60 + minute);
	}
	sort(table.begin(), table.end());

	int time = 9 * 60;
	int idx = 0, person = 0, bus = 0;
	for (; bus < n && time < 1440; bus++, time += t)
	{
		person = 0; // 이번 버스에 탄 학생 수
		for (; person < m && idx < k && table.at(idx) <= time; person++, idx++) {}
	}

	if (bus==n)
	{
		if (person==m)
		{
			time = table.at(idx - 1);
			cout << (time - 1) / 60 << " " << (time - 1) % 60;
		}
		else {
			cout << (time - t) / 60 << " " << (time - t) % 60;
		}
	}
	else {
		time = 540 + (n - 1) * t;
	}
	return 0;
}