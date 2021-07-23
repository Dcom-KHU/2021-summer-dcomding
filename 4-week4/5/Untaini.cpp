//solving with union-find, backtracking
#include <cstdio>
#include <stack>
#include <algorithm>
using namespace std;

#define pii pair<int, int>
#define max(a,b) (a>b?a:b)

int n, v, left, right, leftGroup[100002], rightGroup[100002], disFromRoot[100002], res;
stack<int> vStack;
stack<pair<int,pii>> rangeStack;

int findLeft(int num){
    if(leftGroup[num] == num) return num;
    else return leftGroup[num] = findLeft(leftGroup[num]);
}

int findRight(int num){
    if(rightGroup[num] == num) return num;
    else return rightGroup[num] = findRight(rightGroup[num]);
}


int main()
{
    scanf("%d",&n);
    for(int cnt=0;cnt<n;++cnt){
        scanf("%d",&v);
        vStack.push(v);
    }
        
    for(int cnt=0;cnt<=100001;++cnt)
        leftGroup[cnt] = rightGroup[cnt] = cnt;
    
    while(!vStack.empty()){
        v = vStack.top(); vStack.pop();
        left = findLeft(v-1), right = findRight(v+1);
        leftGroup[v] = left, rightGroup[v] = right;
        findLeft(right-1), findRight(left+1);
        rangeStack.push(make_pair(v,make_pair(left,right)));   
    }
    
    while(!rangeStack.empty()){
        v = rangeStack.top().first, left = rangeStack.top().second.first, right = rangeStack.top().second.second;
        rangeStack.pop();
        res+=(disFromRoot[v] = max(disFromRoot[left], disFromRoot[right])+1)-1;
        printf("%d\n",res);
    }
    return 0;
}

/*
//solved with set container
#include <cstdio>
#include <set>
using namespace std;

#define max(x,y) (x>y?x:y)

int n, v, distanceFromRoot[100002], result;
set<int> insertedNum;

int main() {
    scanf("%d", &n);
    insertedNum.insert(0);
    insertedNum.insert(n+1);
    for(int cnt=0; cnt<n; ++cnt){
        scanf("%d", &v);
        auto right = insertedNum.lower_bound(v), left = right; --left;
        result += (distanceFromRoot[v] = max(distanceFromRoot[*left], distanceFromRoot[*right])+1);
        insertedNum.insert(v);
        printf("%d\n", --result);
    }
    return 0;
}
*/

/*
//solved with fenwick tree and binary search
#include <cstdio>

#define max(x,y) (x>y?x:y)

int n, v, fenwickTree[100010], distanceFromRoot[100010], result;

void update(int num, int val){
    while(num<=n)
        fenwickTree[num] += val, num += (num & -num);
}

int sumOneToNum(int num){
    int res = 0;
    while(num)
        res += fenwickTree[num], num -= (num & -num);
    return res;
}

int binarySearch(int val){
    int left = 1, right = n, mid;
    while(left <= right){
        mid = (left+right)/2;
        
        if(sumOneToNum(mid) <= val) left = mid+1;
        else right = mid-1;
    }
    return left;
}

int main() {
    scanf("%d", &n); n+=2;
    update(1,1);
    update(n,1);
    for(int cnt=2; cnt<n; ++cnt){
        scanf("%d", &v); ++v;
        int vSum = sumOneToNum(v), left = binarySearch(vSum-1), right = binarySearch(vSum);
        result += (distanceFromRoot[v] = max(distanceFromRoot[left], distanceFromRoot[right])+1);
        update(v, 1);
        printf("%d\n", --result);
    }
    return 0;
}
*/
