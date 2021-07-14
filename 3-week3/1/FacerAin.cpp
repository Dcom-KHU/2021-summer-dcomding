#include <iostream>
#include <set>
using namespace std;
set<int> s;
int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int n,k;
	cin >> n >> k;
	for(int i = 0; i < n; i++){
		int num;
		cin >> num;
		s.insert(num);
	}
	cout << ((s.size() > k) ? k : s.size());
	return 0;
}