#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<algorithm>

using namespace std;

int is_leader[300001];
int memory_cost[300001];
vector<int> sales;
vector<vector<int>> links;
const int INF = 2147483647;

struct team {
	int leader;
	int leaders_cost;
	vector<pair<int,int>> members;
};
class teams {
private:
	vector<team> info;
	map<int, int> leaders;
	int length;
public:
	void insert(int _leader, int member, int leaderCost,int memberCost) {
		int Team = getTeamByLeader(_leader);
		if (Team == -1) {
			leaders.insert(make_pair(_leader, length));

			team NewTeam;
			NewTeam.leader = _leader;
			NewTeam.leaders_cost = leaderCost;
			info.push_back(NewTeam);

			is_leader[_leader] = 1;

			Team = length;

			length++;

		}
		info[Team].members.push_back(make_pair(memberCost,member));
	}
	teams() {
		length = 0;
	}
	teams(vector<vector<int>>  _links, vector<int> sales) {
		length = 0;
		for (auto item : _links) {
			this->insert(item[0], item[1], sales[item[0]], sales[item[1]]);
		}
		for (int i = 0; i < info.size();i++) {
			sort(info[i].members.begin(), info[i].members.end());
		}
	}
	int getTeamByLeader(int leader){
		if (leaders.find(leader) != leaders.end()) {
			return leaders[leader];
		}
		return -1;
	}
	int getNumberOfTeam() {
		return length;
	}

	int getMinCostWithoutLeader(int _team) {
		team curTeam = info[_team];
		pair<int, int>mem = curTeam.members[0];
		int res = 0;
		bool find=0;
		for (auto item : curTeam.members) {
			if (!is_leader[item.second]) {
				res = item.second;
				find = 1;
				break;
			}
		}

		if (!find) return -1;
		else return res;
	}

	team getTeamInfo(int tn) {
		return info[tn];
	}
	
	void print() {
		for (auto item : info) {
			cout << "leader : " << item.leader << ", members: ";
			for (int i = 0; i < item.members.size();i++) {
				cout << item.members[i].second << "("<<item.members[i].first<<")";
			}
		}
		cout << "\n";
	}
	

};


teams T;

int setInfo();
int getCost(vector<int> res, int curTeam);
int Min(int a, int b);
int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n = setInfo();
	//T.print();

	vector<int> v(n);
	for (int i = 0; i < n; i++) {
		v[i] = -1;
	}
	
	int res = getCost(v, 0);
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
	}

	T = teams(links,sales);
	return T.getNumberOfTeam();
}

int getCost(vector<int> res, int curTeam) {
	int result = INF;
	
	/*
	int sum = 0;
	for (int i = 0; i < res.size();i++) {
		cout << res[i] << " ";
		if(res[i] != -1)
			sum += sales[res[i]];
	}
	cout <<"sum : "<<sum<<", curteam : "<<curTeam<< "\n";
	*/
	
	if (curTeam == T.getNumberOfTeam()) {
		return 0;
	}
	int MinWithoutLeader = T.getMinCostWithoutLeader(curTeam);
	int TeamOfLeader;
	team Team = T.getTeamInfo(curTeam);
	

	for (int i = 0; i < Team.members.size();i++) {
		vector<int> newres = res;
		if (find(newres.begin(), newres.end(), Team.members[i].second) != newres.end()) {
			result = Min(getCost(newres, curTeam + 1), result);
		}
		
		if (is_leader[Team.members[i].second]) {
			//TeamOfLeader = T.getTeamByLeader(Team.members[i].second);
			//newres[TeamOfLeader] = Team.members[i].second;
			newres[curTeam] = Team.members[i].second;			
			result = Min(getCost(newres, curTeam + 1) + Team.members[i].first, result);	
			//newres[TeamOfLeader] = -1;
			newres[curTeam] = -1;
		}

		if (Team.members[i].second == MinWithoutLeader) {
			newres[curTeam] = Team.members[i].second;
			result = Min(getCost(newres, curTeam + 1) + Team.members[i].first, result);
			newres[curTeam] = -1;
		}
	}
	
	vector<int> newres = res;
	if (find(res.begin(), res.end(), Team.leader) == res.end()) {
		newres[curTeam] = Team.leader;
		result = Min(getCost(newres, curTeam + 1) + Team.leaders_cost, result);
		newres[curTeam] = -1;
	}
	return result;
}