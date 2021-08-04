#include <string>
#include <vector>
#include<iostream>

using namespace std;

vector<long long int> node;
vector<vector<int>> edge;
vector<int> visit;
long long int totalCount = 0;


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
long long solution(vector<int> a, vector<vector<int>> edges) {
	long long answer = -2;
	for (int i = 0; i < a.size();i++) {
		node.push_back(a[i]);
	}
	edge = vector<vector<int>>(a.size());
	visit = vector<int>(a.size());
	for (int i = 0; i < edges.size();i++) {
		edge[edges[i][0]].push_back(edges[i][1]);
		edge[edges[i][1]].push_back(edges[i][0]);
	}

	int res;
	res = searchCount(0);
	if (!res) answer = totalCount;
	else answer = -1;


	return answer;
}
int main() {
	int p,c,n;
	cin >> n;

	vector<vector<int>> ed(0);
	vector<int>a(n);
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	for (int i = 0; i < n-1; i++) {
		cin >> p>>c;
		ed.push_back({ p,c });
	}

	cout<<solution(a, ed);
}