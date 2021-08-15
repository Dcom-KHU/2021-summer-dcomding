#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<algorithm>

using namespace std;

int cost[300001][2];
vector<int> sales;
vector<vector<int>> links;
vector<vector<int>> teams(300001,vector<int>(0));
const int INF = 2147483647;

int getCost(int leader, int is_attend);
int setInfo();
int Min(int a, int b);
int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n = setInfo();
	//T.print();

	for (int i = 0; i < 300001;i++) {
		cost[i][1] = -1;
		cost[i][0] = -1;
	}
	int res = Min(getCost(0, 0),getCost(0,1));
	cout << res;



}

int Min(int a, int b) {
	if (a < b) return a;
	else return b;
}
int setInfo() {
	int n, input;
	vector<int>inputvec(2);
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> input;
		sales.push_back(input);
	}
	for (int i = 0; i < n - 1; i++) {
		cin >> inputvec[0] >> inputvec[1];
		links.push_back(inputvec);
		teams[inputvec[0]].push_back(inputvec[1]);
	}

	return 0;
}

int getCost(int leader, int is_attend){ //is_attend는 leader가 참여하는지 여부
	//cout << "cost[" << leader << "][" << is_attend << "] 구하는중 : ";
	int result = 0;
	int cur_result;
	if (cost[leader][is_attend] != -1) {
		return cost[leader][is_attend];
	}
	if (is_attend) {
		for (int i = 0; i < teams[leader].size();i++) {
			result += Min(getCost(teams[leader][i], 0), getCost(teams[leader][i], 1));
		}
		result += sales[leader];
	}
	else if (!is_attend) {
		int next_ide;
		int next_ede;
		int min_cost=INF;
		int min_node = -1;
		bool found = false;

		for (int i = 0; i < teams[leader].size();i++) {
			next_ide = getCost(teams[leader][i], 1);
			next_ede = getCost(teams[leader][i], 0);
			if (next_ide < next_ede) {
				result += getCost(teams[leader][i],1);
				found = 1;
			}
			else if (!found && next_ede <= next_ide) {
				if (next_ide-next_ede < min_cost) {
					min_cost = next_ide-next_ede;
					min_node = teams[leader][i];
				}
			}
		}
		if (!found&& min_node != -1) {
			for (int i = 0; i < teams[leader].size();i++) {
				if (teams[leader][i] == min_node) {
					result += getCost(teams[leader][i], 1);
				}
				else {
					result += getCost(teams[leader][i], 0);
				}
			}
		}	
	}


	cost[leader][is_attend] = result;
	
	//cout << "cost["<<leader<<"]["<<is_attend<<"] result : " << result << "\n";
	return result;
}