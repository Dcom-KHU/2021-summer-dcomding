/*
N이 크지 않으므로
문제에서 주어진대로 구현만 하면 되는
시뮬레이션 문제
*/

#include <iostream>
#include <cmath>
using namespace std;
int N, L;
int ans = 0;
const int MAX = 105;
bool isMake(int i, int j, int map[MAX][MAX]){//수행속도 향상을 위해 Pass By Reference로 배열을 넘기는 것이 바람직하나 귀찮으므로 생략
	for(int k = j+1; k < j+L; k++){
		if(map[i][j] != map[i][k]){
			return false;
		}
	}
	return true;
}

void search(int map[MAX][MAX]){
	for(int i = 0; i < N; i++){
		bool isRoad = true;
		int len = 1;
		for(int j = 0; j < N-1; j++){
			if(abs(map[i][j] - map[i][j+1]) >= 2)//높이 차이가 2 이상이라면 길 생성 불가
			{
				isRoad = false;
				break;
			}
			if(map[i][j] == map[i][j+1]){//평평한 길일 경우
				len++;
			}else if(map[i][j] > map[i][j+1]){//내려와야 하는 경우
				if(isMake(i,j+1, map)){
					j += L-1;
					len = 0;
				}else{
					isRoad = false;
					break;
				}
				
			}else if(map[i][j] < map[i][j+1]){//올라가야 하는 경우
				if(len >= L){
					len = 1;
				}else{
					isRoad = false;
					break;
				}
			}
		}
		if(isRoad){
			ans++;
		}
		
	}
}

int main(){

	cin >> N >> L;
	int map1[MAX][MAX];
	int map2[MAX][MAX];
	for(int i = 0; i < N; i++){
		for(int j = 0; j < N; j++){
			cin >> map1[i][j];
			map2[j][i] = map1[i][j];
		}
	}
	search(map1);
	search(map2);
	cout << ans;
	return 0;
}