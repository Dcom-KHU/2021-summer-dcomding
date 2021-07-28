#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

class Tree{
private:
    int ch;
    vector<Tree> treeVec;
    
public:
    Tree(int ch){
        this->ch = ch;
        treeVec = vector<Tree>();
    }
    
    int getChar() {
        return this->ch;
    }
    
    Tree* insert(int ch){
        for(auto iter = treeVec.begin(); iter != treeVec.end(); ++iter)
            if(iter->ch == ch) return &treeVec[iter-treeVec.begin()];
        treeVec.push_back(Tree(ch));
        return &treeVec[treeVec.size()-1];
    }
    
    void inOrder(int arr[], int cnt){
        bool needTyping = treeVec.size()>1;
        cnt += needTyping;
        for(auto iter = treeVec.begin(); iter != treeVec.end(); ++iter)
            if(iter->ch>=1000)
                arr[iter->ch-1000] = cnt - needTyping;
            else
                iter->inOrder(arr, cnt);
    }
};

int n, typingCnt[100000];
char word[100];
Tree oriTree = Tree(0);

int main()
{
    
    scanf("%d",&n); getchar();
    for(int cnt=0; cnt<n; ++cnt){
        scanf("%s",word);
        
        Tree* treePtr = &oriTree;
        for(int wordCnt=0; word[wordCnt]; ++wordCnt)
            treePtr = treePtr->insert(word[wordCnt]);
            
        treePtr->insert(cnt+1000);
    }
    
    oriTree.insert(0);
    oriTree.inOrder(typingCnt, 0);
    
    for(int cnt=0; cnt<n; ++cnt)
        printf("%d\n",typingCnt[cnt]);
    return 0;
}
