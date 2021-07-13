#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	int n, t, m, k, hour, minute;
	vector<int> table;
	cin >> n >> t >> m >> k;

	//time table �Է�, ����
	for (int i = 0; i < k; i++)
	{
		cin >> hour >> minute;
		table.push_back(hour * 60 + minute);
	}
	sort(table.begin(), table.end());

	int time = 9 * 60;
	int idx = 0, person = 0;
	for (int i = 0; i < n && time < 1440; i++, time += t)
	{
		person = 0; // �̹� ������ ź �л� ��
		for (; person < m && idx < k && table.at(idx) <= time; person++, idx++) {}
	}

	//������ �ڸ��� �ִٸ�
	if (idx < k || person < m) cout << (time - t) / 60 << " " << (time - t) % 60;
	//������ �ڸ��� ���ٸ�
	else {
		time = table.at(idx - 1);
		cout << (time - 1) / 60 << " " << (time - 1) % 60;
	}
	return 0;
}