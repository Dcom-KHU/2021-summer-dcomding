//Trie + DP로 풀기
#include <cstdio>
#include <cstring>
#define min(a,b) (a<b?a:b)

class Trie{
public:
    Trie* abt[26];
    bool isEnd; //끝난지점을 확인하기 위해 변수 추가
	
    Trie(){
        memset(abt, 0, sizeof(abt));
		isEnd=false;
    }
    
    ~Trie(){
        for(int cnt=0; cnt<26; ++cnt)
            if(abt[cnt]) delete abt[cnt];
    }
    
    Trie* insert(int ch){
        if(!abt[ch-='a'])
			abt[ch] = new Trie();
        return abt[ch];
    }
};

//wordDp[n] : n-1번째 문자열을 완성하는데까지 사용한 단어의 최소 개수
int n, wordDp[20010], cnt, len, cur;
char str[20010], word[6];
Trie root;
Trie* trie;

int main(){
	scanf("%d",&n); getchar();
	scanf("%s", str);
	for(cnt=0; cnt<n; ++cnt){
		scanf("%s",word);
		trie = &root;
		
		//단어를 트라이 자료구조에 넣음
		for(cur=0; word[cur]; ++cur)
			trie = trie->insert(word[cur]);
		
		//단어의 마지막 알파벳 위치에 단어가 끝났다는 것을 저장함
		trie->isEnd = true;
	}
	
	//DP 초기값 설정
	for(cnt=1; cnt<=20000; ++cnt)
		wordDp[cnt] = 1<<30;
	
	for(len=0; str[len]; ++len){
		trie = &root, cur=len;
		
		//문자열이 끝나지 않았고 트라이에 str[cur]에 해당하는 알파벳이 없을 때까지 반복
		while(str[cur] && trie = trie->abt[str[cur++]-'a']){
			
			//단어가 끝났다면 DP값을 갱신함
			if(trie->isEnd) wordDp[cur] = min(wordDp[cur], wordDp[len]+1);
		}
	}
	
	//주어진 단어들로 문자열을 만들 수 없다면 -1, 아니면 dp값을 출력함
	printf("%d", wordDp[len]==(1<<30)?-1:wordDp[len]);
	return 0;
}

/*
//첫 알파벳으로 정리한 배열 + DP로 풀기
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

//wordDp[n] : n-1번째 문자열을 완성하는데까지 사용한 단어의 최소 개수
int n, wordDp[20010], len, strPos, cur;
char str[20010], words[100][6];
vector<int> apbWords[26];

int main() {
	scanf("%d", &n); getchar();
	scanf("%s", str);
	for(int cnt=0;cnt<n;++cnt){
		scanf("%s",words[cnt]);
		
		//반복문 횟수를 줄이기 위해 단어의 첫 알파벳을 이용해 정리함
		apbWords[words[cnt][0]-'a'].push_back(cnt);
	}
	
	for(int cnt=1; cnt<=20000; ++cnt)
		wordDp[cnt] = 1<<30;
	
	for(len=0; str[len]; ++len){
		//주어진 알파벳으로 시작하는 단어들을 하나씩 사용해봄
		for(int vCnt = 0; vCnt<apbWords[str[len]-'a'].size(); ++vCnt){
			strPos = apbWords[str[len]-'a'][vCnt];
			
			//단어와 주어진 문자열을 하나씩 비교해보고 단어가 먼저 끝나거나 중간에 서로 다른 문자가 적혀 있다면 for문 종료
			bool isMatched = true;
			for(cur = 0; words[strPos][cur] && isMatched; ++cur)
				isMatched &= str[len+cur] == words[strPos][cur];
			
			//단어와 문자열이 모두 일치한다면 dp를 갱신함
			if(isMatched) wordDp[len+cur] = min(wordDp[len+cur], wordDp[len]+1);
		}
	}
	
	//주어진 단어들로 문자열을 만들 수 없다면 -1, 아니면 dp값을 출력함
	printf("%d", wordDp[len]==(1<<30)?-1:wordDp[len]);
	return 0;
}
*/
