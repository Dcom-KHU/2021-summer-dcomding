/*
트라이를 이용하면 되는 문제.
*/


#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

const int ALPHA_NUM = 26;
vector<string> words;
int toNum(char c){
	return c - 'a';
}

struct TrieNode{
	TrieNode* children[ALPHA_NUM];
	
	bool terminal;
	int count;
	bool isRoot = false;
	
	TrieNode(){
		count = 0;
		terminal = false;
		for(int i = 0; i < 26; i++){
			children[i] = 0;
		}
	}
	
	void insert(const char* key) {
		if(*key == 0){
			terminal = true;
		}else{
			int next = toNum(*key);
			if(children[next] == 0){
				children[next] = new TrieNode();
				count++;
			}
			children[next]->insert(key+1);
			
		}
	}

	
	int find(const char* key, int cnt) {
		//cout << *key << " " << count << endl;
		if(*key == 0){
			return cnt;
		}
		
		int next = toNum(*key);
		if(isRoot){
			cnt++;
		}else{
			if(count > 1){
				cnt++;
			}else if(terminal){
				cnt++;
			}
		}
		
		return children[next]->find(key+1, cnt);
		
		
	}
};

int main(){
	int n;
	cin >> n;
	for(int i = 0; i < n; i++){
		char s[100];
		cin >> s;
		words.push_back(s);
	}
	
	TrieNode* trie = new TrieNode();
	for(int i = 0; i < words.size(); i++){
		trie->insert(words[i].c_str());
	}
	trie->isRoot = true;
	for(int i = 0; i < words.size(); i++){
		cout << trie->find(words[i].c_str(), 0) << "\n";
	}
	return 0;
}