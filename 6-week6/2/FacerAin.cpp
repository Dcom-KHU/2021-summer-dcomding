#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector<int> v;
int main(){
	int a, b;
	int num;
	cin >> a >> b;
	for(int i = 0; i < a+b; i++){
		cin >> num;
		v.push_back(num);
	}
	sort(v.begin(), v.end());
	int result = 0;
	for(int i = 0; i < v.size() - 1; i++){
		if(v[i] == v[i+1]){
			i++;
		}else{
			result++;
		}
	}
	
	cout << result + 1;
	return 0;
}

//1 2 3 4 5 6 7 8
//1 2 3 4 5 6 7 8 8