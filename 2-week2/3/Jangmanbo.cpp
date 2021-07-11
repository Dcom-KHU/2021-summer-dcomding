#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool smaller(string depart, string end) {
	if (depart.size() < end.size()) { return true; }
	else if (depart.size() > end.size()) { return false; }
	else {
		if (depart[0]<end[0])
		{
			return true;
		}
		else {
			return false;
		}
	}
}

int main() {
	int n, index;
	vector<string> depart, arrival;
	string start, end;
	cin >> n;
	
	for (int i = 0; i < n; i++)
	{
		cin >> start >> end;
		depart.push_back(start);
		arrival.push_back(end);
	}

	start = "DCOM";
	end = "ZZZZZZZZZZZ";

	cout << start << " ";

	for (int num = 0; num < n; num++)
	{
		for (int i = 0; i < depart.size(); i++)
		{
			if (depart[i] == start)
			{
				if (smaller(arrival[i], end))
				{
					end = arrival[i];
					index = i;
				}
			}
		}
		cout << end << ' ';
		depart.erase(depart.begin() + index);
		arrival.erase(arrival.begin() + index);
		start = end;
		end = "ZZZZZZZZZZZ";
	}
	return 0;
}
