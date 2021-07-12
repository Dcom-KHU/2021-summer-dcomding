#include <iostream>
#include <vector>
using namespace std;

void DFS(vector<vector<int>>& table, int index, int total, int& max) {
	int size = table.size();
	for (int i = index; i < size; i++)
	{
		if (i + table[i][0] <= size)
		{
			total += table[i][1];
			DFS(table, i + table[i][0], total, max);
			total -= table[i][1];
		}
	}
	if (total > max) max = total;
}

int main() {
	int n, t, p, total = 0, max = 0;
	vector<vector<int>> table;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> t >> p;
		table.push_back({ t, p });
	}
	DFS(table, 0, 0, max);
	cout << max;
	return 0;
}