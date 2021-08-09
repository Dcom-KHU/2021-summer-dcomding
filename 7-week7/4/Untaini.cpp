#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int n, wordDp[20010], len, strPos, cur;
char str[20010], words[100][6];
vector<int> apbWords[26];

int main() {
	scanf("%d", &n); getchar();
	scanf("%s", str);
	for(int cnt=0;cnt<n;++cnt){
		scanf("%s",words[cnt]);
		apbWords[words[cnt][0]-'a'].push_back(cnt);
	}
	
	
	for(int cnt=1; cnt<=20000; ++cnt)
		wordDp[cnt] = 1<<30;
	
	for(len=0; str[len]; ++len){
		for(int vCnt = 0; vCnt<apbWords[str[len]-'a'].size(); ++vCnt){
			strPos = apbWords[str[len]-'a'][vCnt];
			bool isMatched = true;
			for(cur = 0; words[strPos][cur] && isMatched; ++cur)
				isMatched &= str[len+cur] == words[strPos][cur];
			if(isMatched) wordDp[len+cur] = min(wordDp[len+cur], wordDp[len]+1);
		}
	}
	
	printf("%d", wordDp[len]==(1<<30)?-1:wordDp[len]);
	return 0;
}