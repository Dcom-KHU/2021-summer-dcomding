#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	int n, t, m, k, hour, minute;
	vector<vector<int>> table;
	cin >> n >> t >> m >> k;

	//time table 입력, 정렬
	for (int i = 0; i < k; i++)
	{
		cin >> hour >> minute;
		table.push_back({ hour, minute });
	}
	sort(table.begin(), table.end());


	vector<int> time = {9, 0};
	int idx = 0, person = 0;
	for (int i = 0; i < n; i++, time[1] += t)
	{
		person = 0; // 이번 버스에 탄 학생 수
		if (time[1] >= 60)
		{
			time[1] -= 60;
			time[0]++;
		}
		for (; person < m && idx < k && table.at(idx) <= time; person++, idx++) {}

	}

	//막차에 자리가 있다면
	if (idx < k || person < m) cout << time[0] << " " << time[1] - t;
	//막차에 자리가 없다면
	else {
		time = table.at(idx - 1);
		if (time[1] == 0) cout << time[0] - 1 << " " << 59;
		else cout << time[0] << " " << time[1] - 1;
	}
	return 0;
}