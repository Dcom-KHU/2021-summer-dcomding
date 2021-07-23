/*
이진 탐색 트리
N의 크기는 10만

C의 값은 곧 랭크 누적
매번 insert 함수를 수행한다면
시간복잡도는 O(N)이므로 수행 시간을 보장할 수 없다.
또한 최악의 경우 편향 이진 트리가 될 수 있어 O(N^2)

이진탐색트리 삽입 원리를 이해하자
*/

#include <iostream>
#include <map>
#include <utility>
#include <algorithm>

using namespace std;

map<int, int> m;

int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n;
	cin >> n;
	long long C = 0;
	int depth;
	
	/*
	최대 최소 값 처리 테크닉
	*/
	m.insert({0,-1});
	m.insert({100005, -1});
	
	for(int i = 0; i < n; i++){
		int num;
		cin >> num;
		auto up_iter = m.upper_bound(num);
		auto low_iter = up_iter;
		--low_iter;//후위 연산자를 사용하면 이전 값을 반환하기 때문에 임시 객체가 생겨 성능이 낮아진다고 함.
		depth = max(up_iter->second, low_iter->second) + 1;
		m.insert({num, depth});
		C += depth;
		cout << C << '\n';
	}
	return 0;
}