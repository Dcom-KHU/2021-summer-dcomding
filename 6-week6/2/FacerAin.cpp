#include <iostream>
#include <set>
using namespace std;
set<int> s;
int main(){
	int a,b;
	int num;
	int ans;
	cin >> a >> b;
	for(int i = 0; i < a; i++){
		cin >> num;
		s.insert(num);
	}
	ans = s.size();
	for(int i = 0; i < b; i++){
		cin >> num;
		if(s.count(num) == 0){
			ans++;
		}else{
			ans--;
		}
	}
	cout << ans;
	return 0;
}