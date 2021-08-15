#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<algorithm>
#include<stack>

using namespace std;

int cost[300001][2];
int is_searched[300001][2];

vector<int> sales;
vector<vector<int>> links;
vector<vector<int>> teams(300001,vector<int>(0));
const int INF = 2147483647;

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

	stack<vector<int>> st,st2;
	vector<int> inp = { 0,0 }; //리더, 참석 여부
	vector<int> t;
	int leader, is_attend;
	st.push(inp);
	st2.push(inp);
	inp[1] = 1;
	st.push(inp);
	st2.push(inp);
	while (!st.empty()) {
		t = st.top();
		leader = t[0];
		is_attend = t[1];
		st.pop();

		for (int i = 0; i < teams[leader].size();i++) {
			inp[0] = teams[leader][i];
			inp[1] = 0;
			if (!is_searched[inp[0]][0]) {
				st2.push(inp);
				st.push(inp);
				is_searched[inp[0]][inp[1]] = 1;
			}

			inp[1] = 1;
			if (!is_searched[inp[0]][1]) {
				st2.push(inp);
				st.push(inp);
				is_searched[inp[0]][inp[1]] = 1;
			}

			//cout << "input " << inp[0] << "\n";
			
		}

	}
		
	
	while (!st2.empty()) {
		t = st2.top();
		leader = t[0];
		is_attend = t[1];
		st2.pop();


		int result = 0;
		if (is_attend) {
			for (int i = 0; i < teams[leader].size();i++) {
				result += Min(cost[teams[leader][i]][0], cost[teams[leader][i]][1]);
			}
			result += sales[leader];
		}
		else if (!is_attend) {
			int next_ide;
			int next_ede;
			int min_cost = INF;
			int min_node = -1;
			bool found = false;

			for (int i = 0; i < teams[leader].size();i++) {
				next_ide = cost[teams[leader][i]][1];
				next_ede = cost[teams[leader][i]][0];
				if (next_ide < next_ede) {
					result += cost[teams[leader][i]][1];
					found = 1;
				}
				else if (next_ede <= next_ide) {
					result += cost[teams[leader][i]][0];
					if (next_ide - next_ede < min_cost && !found) {
						min_cost = next_ide - next_ede;
						min_node = teams[leader][i];
					}
				}
			}
			if (!found && min_node != -1) {
				for (int i = 0; i < teams[leader].size();i++) {
					result -= cost[teams[leader][i]][0];
					result += cost[teams[leader][i]][1];
				}
			}
		}

		//cout << "leader : " << leader << " , attend : " << is_attend << " , cost : " << result << "\n";
		cost[leader][is_attend] = result;
	}
	cout << Min(cost[0][0],cost[0][1]);



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
