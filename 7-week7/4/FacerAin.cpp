#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

vector<string> words;
const int MAX = 99999999;
int dp[20005];
int main(){
	int n;
	string str;
	cin >> n;

	cin >> str;
	for(int i = 0; i < n; i++){
		string s;
		cin >> s;
		words.push_back(s);
	}
	
	for(int i = 1; i <= str.length(); i++){
		dp[i] = MAX;
	}
	
	for(int i = 1; i <= str.length(); i++){
		for(int j = 0; j < words.size(); j++){
			string s = words[j];

			if(i - s.length() < 0){
				continue;
			}
			bool flag = true;
			for(int k = 0; k < s.length(); k++){
				if(s[k] != str[i - s.length() + k]){
					flag = false;
					break;
				}
			}
			if(flag){
				dp[i] = min(dp[i], dp[i - s.length()] + 1);
			}
		}
	}
	int ans = dp[str.length()];
	if(ans == MAX){
		cout << -1;
	}else{
		cout << ans;
	}
	return 0;
}