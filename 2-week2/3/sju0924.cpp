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
<<<<<<< HEAD
<<<<<<< HEAD

ticket tickets[100001];
bool visit[100001];
string res[100001];



class findNextClub {
private:
	int len;
	string club[5001];
	vector<vector<int>>Myticket;

public:
	findNextClub() {
		len = 0;
	}
	void Add_ticket(ticket _t,int tnum) {
		string f = _t.first;
		string s = _t.second;

		for (int i = 0; i < len; i++) {
			//cout <<"club["<<i<<"]: "<<club[i] << " " << f << "\n";
			if (club[i] == f) {
				Myticket[i].push_back(tnum);
				return;
			}
		}
		club[len] = f;
		len++;
		vector<int> newV;
		newV.push_back(tnum);
		Myticket.push_back(newV);
		return;
	}
=======
pair<string, string> tickets[100001];
bool visit[100001];
vector<string> res;
>>>>>>> parent of 47c11a5 (Update sju0924.cpp)

	vector<int> getNextClub(string _s) {

		for (int i = 0; i < len; i++) {
			if (club[i] == _s) {
				return Myticket[i];
			}
		}
		return vector<int>(0);
		
	}

	void print() {
		for (int i = 0; i < len; i++) {
			cout << "club: " << club[i] << " : ";
			for (int j = 0; j < Myticket[i].size();j++) {
				cout << tickets[Myticket[i][j]].first << "-"<<tickets[Myticket[i][j]].second<<", ";
			}
			cout << "\n";
		}
	}


};
=======
pair<string, string> tickets[100001];
bool visit[100001];
vector<string> res;
>>>>>>> parent of 47c11a5 (Update sju0924.cpp)

findNextClub info;

int search(string cur,int cnt);
int N;
int main()
{
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int cnt=0,nf,nt,Size = 0;
	string from,to;
	
	cin >> N;

	for (int i = 0; i < N; i++) {
<<<<<<< HEAD
<<<<<<< HEAD
		cin >> from>>to;
		tickets[i].first = from;
		tickets[i].second = to;
=======
		cin >> from>>to;		
		tickets[i] = make_pair(from, to);		
>>>>>>> parent of 47c11a5 (Update sju0924.cpp)
=======
		cin >> from>>to;		
		tickets[i] = make_pair(from, to);		
>>>>>>> parent of 47c11a5 (Update sju0924.cpp)
	}
	sort(tickets, tickets + N);
	/*
	for (int i = 0; i <= N; i++) {
		cout << tickets[i].first<<" "<<tickets[i].second << "\n";
	}
	*/



	for (int i = 0; i < N; i++) {
		info.Add_ticket(tickets[i],i);
	}
	//info.print();
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
<<<<<<< HEAD
<<<<<<< HEAD
	int curTicket;
	vector<int>next = info.getNextClub(cur);
	//cout << next.size() << "\n";
	for (int i = 0;i <next.size();i++) {
		curTicket = next[i];
		if (visit[curTicket] == false and cur == tickets[curTicket].first) {
			visit[curTicket] = true;
			is_searched = search(tickets[curTicket].second, cnt + 1);
=======
=======
>>>>>>> parent of 47c11a5 (Update sju0924.cpp)

	
	for (int i = 0;i <N;i++) {
		if (visit[i] == false and cur == tickets[i].first) {
			visit[i] = true;
			res.push_back(cur);
			is_searched = search(tickets[i].second, cnt + 1);
>>>>>>> parent of 47c11a5 (Update sju0924.cpp)
			if (is_searched) {
				return true;
			}
			visit[i] = false;
			res.pop_back();
		}
		

	}


	return false;
}