#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector<int> cookies;
int main(){
	int n;
	int ans = 0;
	cin >> n;
	for(int i = 0; i < n; i++){
		int num;
		cin >> num;
		cookies.push_back(num);
	}
	for(int i = 0; i < n; i++){
		int l_idx = i;
		int r_idx = i+1;
		int l_sum = cookies[l_idx];
		int r_sum = cookies[r_idx];
		
		while(l_idx != -1 && r_idx != n){
			if(l_sum <= r_sum){
				l_idx--;
				l_sum += cookies[l_idx];
			}else{
				r_idx++;
				r_sum += cookies[r_idx];
			}
			if(r_sum == l_sum){
				ans = max(r_sum, ans);
			}
			
		}
		
		if(l_idx < 0 && r_idx < n){
			while(r_idx < n){
				r_idx++;
				r_sum += cookies[r_idx];
				if(r_sum > l_sum){
					break;
				}
				if(r_sum == l_sum){
					ans = max(r_sum, ans);
				}
			}
		}else if(l_idx >= 0 && r_idx >= n){
			while(l_idx >= 0){
				l_idx--;
				l_sum += cookies[l_idx];
				
			if(r_sum < l_sum){
				break;
			}
			if(r_sum == l_sum){
				ans = max(r_sum, ans);
			}
		}
			

		}
		
		
		//왼쪽을 넣을 것인가
		//오른쪽을 넣을 것인가
		//기준은 바구니 쿠키가 작은 쪽
		//탐색 종료 조건은 양 끝에 도달했을 때
		
		
		
	}
	
	cout << ans;
	
	
	return 0;
}