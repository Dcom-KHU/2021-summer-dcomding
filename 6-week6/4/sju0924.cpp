#include <string>
#include <vector>
#include<iostream>
#include<stack>
using namespace std;
vector<long long int> node;
vector<vector<int>> edge;
vector<int> visit;

stack<int> nt;
long long int totalCount = 0;

struct Node {
	int idx;
	int childidx;

	Node(int i, int c) {
		idx = i;
		childidx = c;
	}
	Node() {
		idx = -1;
		childidx = -1;
	}
	void setNode(int i, int c) {
		idx = i;
		childidx = c;
	}
};

stack<Node> st;

long long int Abs(long long int n) {
	if (n > 0) return n;
	else return -n;
}
long long int searchCount(int n) {
	visit[n] = 1;

	long long int sub = 0;
	for (int i = 0; i < edge[n].size();i++) {
		if (visit[edge[n][i]]) continue;
		sub = searchCount(edge[n][i]);

		node[n] += sub;
		node[edge[n][i]] -= sub;
		totalCount += Abs(sub);
	}


	return node[n];
}
void PushStack(int n, char kind) {
	Node newnode;
	if (kind == 'n') {
		visit[n] = 1;
		for (int i = 0; i < edge[n].size();i++) {
			if (!visit[edge[n][i]]) {
				nt.push(edge[n][i]);
				newnode.setNode(n, edge[n][i]);
				st.push(newnode);
			}
			
		}
	}

}
long long int solution() {
	long long int answer = -2;
	long long int res;

	int t;
	Node Top;
	long long int sub = 0;
	nt.push(0);
	while (!nt.empty()) {
		t = nt.top();
		nt.pop();
		PushStack(t, 'n');
	}

	
	while (!st.empty()) {
		Top = st.top();
		st.pop();

		//cout << Top.idx << " " << Top.childidx << "\n";
		
		node[Top.idx] += node[Top.childidx];		
		totalCount += Abs(node[Top.childidx]);
		node[Top.childidx] = 0;
		//cout << totalCount << "\n";
	}
	//res = searchCount(0);

	res = node[0];
	if (!res) answer = totalCount;
	else answer = -1;

	return answer;
}

int main() {
	int p,c,n,input;
	cin >> n;
	
	for (int i = 0; i < n; i++) {
		cin >>input;
		node.push_back(input);
	}
	visit = vector<int>(n);
	edge = vector<vector<int>>(n);
	for (int i = 0; i < n-1; i++) {
		cin >> p>>c;
		edge[p].push_back(c);
		edge[c].push_back(p);
	}

	long long int res = solution();
	cout << res<<"\n";

	return 0;
}