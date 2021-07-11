#include<iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

map<string, int> itemloc;
vector<string> items;
vector<int> res;
int n, s = 0, e = 0;

int main() {
	
	cin >> n;
	string input;
	for (int i = 0; i < n; i++) {
		cin >> input;
		items.push_back(input);
	}

	for (int i = 0; i < items.size();i++) {
		itemloc[items[i]] = 0;
	}

	int total_items = itemloc.size();
	int cur_items = 0;
	int tmp_s, tmp_e;
	int len = 100001;
	while (true) {
		if (cur_items == total_items) {
			if (e - s < len) {
				tmp_s = s;
				tmp_e = e;
				len = e - s;
			}

			if (itemloc[items[s]] > 1) {
				itemloc[items[s]]--;
				s++;
			}
			else {
				itemloc[items[s]]--;
				s++;
				cur_items--;
			}

		}
		else {
			if (e == items.size()) break;
			if (!itemloc[items[e]]) cur_items++;
			itemloc[items[e]]++;
			e++;
		}
	}

	cout << tmp_s+1 << "\n" << tmp_e;
}