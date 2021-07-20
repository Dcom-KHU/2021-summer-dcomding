#include <iostream>
#include <utility>
#include <algorithm>
#include <vector>


using namespace std;
bool compare(pair<int,int> a, pair<int,int> b){
	if(a.second == b.second){
		return a.first < b.first;
	}
	return a.second < b.second;
}
vector<pair<int,int>> v;
int main(){
	int n;
	cin >> n;
	for(int i = 0; i < n; i++){
		int a,b;
		cin >> a >> b;
		v.push_back({a,b});
	}
	sort(v.begin(), v.end(), compare);
	
	int ans = 1;
	int start = v[0].first;
	int end = v[0].second;
	for(int i = 1; i < n; i++){
		if(v[i].first >= end){
			ans++;
			end = v[i].second;
		}
	}
	
	cout << ans;
	
	
	return 0;
	
}