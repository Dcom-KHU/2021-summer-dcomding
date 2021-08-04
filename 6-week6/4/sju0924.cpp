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
long long int solution() {
	long long int answer = -2;
	long long int res;

	res = searchCount(0);

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