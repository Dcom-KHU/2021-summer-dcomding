#include <iostream>
#include <vector>
using namespace std;

struct Map
{
	int height;
	bool ladder = false;
};

int main()
{
	int N, L;
	cin >> N >> L;

	vector<vector<Map>> map;
	for (int i = 0; i < N; i++) {
		vector<Map> innermap;
		for (int j = 0; j < N; j++) {
			Map temp;
			cin >> temp.height;
			innermap.push_back(temp);
		}
		map.push_back(innermap);
	}

	for (int i = 0; i < N; i++) {
		vector<Map> innermap;
		for (int j = 0; j < N; j++) {
			innermap.push_back(map[j][i]);
		}
		map.push_back(innermap);
	}

	int count = 0;
	int pre, now;
	bool way;
	for (int i = 0; i < (N * 2); i++) {
		pre = map[i][0].height;
		way = true;
		for (int j = 0; j < N; j++) {
			now = map[i][j].height;
			if (now != pre) {
				if (abs(now - pre) > 1) {
					way = false;
					break;
				}
				else if (now < pre) {
					for (int k = j + 1; k < (j + L); k++) {
						if ((k == N) || (now != map[i][k].height)) {
							way = false;
							break;
						}
						else map[i][k].ladder = true;
					}
					map[i][j].ladder = true;
				}
				else {
					for (int k = j - L; k < j; k++) {
						if (((k < 0) || map[i][k].ladder == true) || (pre != map[i][k].height)) {
							way = false;
							break;
						}
					}
				}
			}
			if (way == false) break;
			pre = map[i][j].height;
		}
		if (way == true) count++;
	}

	cout << count << endl;

	return 0;
}