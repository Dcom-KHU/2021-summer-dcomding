#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int n;

bool DFS(string start, vector<vector<string>> tickets, vector<int> stop, int consume, vector<string>& print) {
	if (consume == n) { return true; }

	int size = tickets.size();
	vector<string> buf;

	for (int i = 0; i < size; i++)
	{
		if (tickets[i][0] == start && !stop[i]) {
			buf = tickets[i];
			print.push_back(buf[1]);
			stop[i] = 1;
			if (DFS(buf[1], tickets, stop, consume + 1, print)) {
				return true;
			}
			print.pop_back();
			stop[i] = 0;
		}
	}

	return false;
}

bool compare(vector<string> start, vector<string> end) {
	return start[1].size() < end[1].size();
}


int main() {
	cin >> n;
	vector<vector<string>> tickets;
	vector<int> stop(n, 0);
	string depart, arrive;
	for (int i = 0; i < n; i++)
	{
		cin >> depart >> arrive;
		tickets.push_back({ depart, arrive });
	}
	sort(tickets.begin(), tickets.end(), compare);

	vector<string> print = { "DCOM" };
	DFS("DCOM", tickets, stop, 0, print);
	for (int i = 0; i < n + 1; i++)
	{
		cout << print[i] << " ";
	}
	return 0;
}