#include <iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

struct ticket {
	string first;
	string second;

	bool operator<(ticket& other) {
		if (this->second.size() < other.second.size()) {
			return true;
		}
		if (this->second < other.second) {
			return true;
		}
		return false;
	}

	
};
pair<string, string> tickets[100001];
bool visit[100001];
vector<string> res;


int search(string cur,int cnt);
int N;
int main()
{
	int cnt=0,nf,nt,Size = 0;
	string from,to;
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> from>>to;		
		tickets[i] = make_pair(from, to);		
	}
	sort(tickets, tickets + N);

	int temp;
	int start;

	
	search("DCOM", 0);
	for (int i = 0; i <= N; i++) {
		cout << res[i] << " ";
	}

}
int search(string cur,int cnt) {
	//cout << "cur: " << cur << " cnt : " << cnt << "\n";
	bool is_searched=false, is_left = false;

	if (cnt == N) {
		res.push_back(cur);
		return true;
	}

	
	for (int i = 0;i <N;i++) {
		if (visit[i] == false and cur == tickets[i].first) {
			visit[i] = true;
			res.push_back(cur);
			is_searched = search(tickets[i].second, cnt + 1);
			if (is_searched) {
				return true;
			}
			visit[i] = false;
			res.pop_back();
		}
		

	}


	return false;
}