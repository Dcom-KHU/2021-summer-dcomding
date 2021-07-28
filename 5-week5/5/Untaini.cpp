#include <cstdio>
#include <cstring>

class Trie{
private:
    char ch;
    int abtCnt, endStringPtr, listPtr;
    Trie* abt[26];
    int abtList[26];
    
public:
    Trie(char ch){
        this->ch = ch;
        abtCnt = listPtr = 0;
        endStringPtr = -1;
        memset(abt, 0, sizeof(abt));
        memset(abtList, 0, sizeof(abtList));
    }
    
    ~Trie(){
        for(int cnt=0; cnt<26; ++cnt)
            if(abt[cnt])
                delete abt[cnt];
    }
    
    Trie* insert(int ch){
        ++abtCnt;
        
        if(ch>=1000 || !ch){
            endStringPtr = ch-1000;
            return this;
        }
        
        if(!abt[ch-='a']){
            abt[ch] = new Trie(ch+'a');
            abtList[listPtr++] = ch;
        }
        else
            --abtCnt;
        
        return abt[ch];
    }
    
    void inOrder(int arr[], int tCnt){
        if(endStringPtr>=0)
            arr[endStringPtr] = tCnt;
        
        tCnt += abtCnt>1;
        
        for(int cnt=0; cnt<listPtr; ++cnt)
            abt[abtList[cnt]]->inOrder(arr, tCnt);
    }
};

int n, typingCnt[100000];
char word[100];
Trie oriTrie = Trie(0);

int main()
{   
    scanf("%d",&n); getchar();
    for(int cnt=0; cnt<n; ++cnt){
        scanf("%s",word);
        
        Trie* triePtr = &oriTrie;
        for(int wordCnt=0; word[wordCnt]; ++wordCnt)
            triePtr = triePtr->insert(word[wordCnt]);
        triePtr->insert(cnt+1000);
    }
    
    oriTrie.insert(0)->inOrder(typingCnt, 0);
    
    for(int cnt=0; cnt<n; ++cnt)
        printf("%d\n",typingCnt[cnt]);
        
    return 0;
}
