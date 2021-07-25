//solving with union-find, backtracking : 80ms
#include <cstdio>
#include <stack>
#include <algorithm>
using namespace std;

#define max(a,b) (a>b?a:b)

int n, v, left, right, leftGroup[100002], rightGroup[100002], disFromRoot[100002];
long long res;
stack<int> vStack;
stack<pair<int,pair<int,int>>> rangeStack;

int findLeft(int num){
    if(leftGroup[num] == num) return num;
    else return leftGroup[num] = findLeft(leftGroup[num]);
}

int findRight(int num){
    if(rightGroup[num] == num) return num;
    else return rightGroup[num] = findRight(rightGroup[num]);
}

//알고리즘 배경
//이진트리의 빠른 삽입은 삽입하고자 하는 값과 가장 가까이에 있는 값 중 비어있는 가지에 넣는 것이다.
//예시로 이진트리 안에 1 6 4 2 순으로 넣었다면 5를 넣을 때는 4와 6 중에 비어있는 가지인 4오른쪽에 넣고(6왼쪽에는 4가 들어가 있다)
//5가 들어간 후 3을 넣는다면 2와 4 중에 비어있는 가지인 2의 오른쪽에 넣는 것이다.(4왼쪽에는 2가 들어가 있다)
//여기서 문제는 '삽입하고자 하는 값과 가장 가까운 두 수를 어떻게 얻을 것인가' 이다.
//만약 O(1)만에 값을 얻고자 가장 가까운 두 수를 저장하는 배열을 만들었다고 해보자.
//초기에는 배열1은 모드 0으로 초기화 되어 있고, 배열2는 n+1로 초기화 되어 있을 것이다.
//하지만 값을 삽입한 뒤, 배열1은 [값,n]구간을 값으로 업데이트하고, 배열2는 [1,값]구간을 값으로 업데이트하면 시간적 손실이 굉장히 많이 나게 된다.
//여기서 두 배열은 모든 값을 삽입한 후 (배열[값] == 값) 이라는 특성을 이용해 백트래킹을 진행한다.
int main()
{
    scanf("%d",&n);
    for(int cnt=0;cnt<n;++cnt){
        scanf("%d",&v);
        vStack.push(v);
    }
    
    //union-find 초기 세팅, 여기서 자기자신을 가리킨다는 건 이진트리에 삽입되어 있음을 의미함
    for(int cnt=0;cnt<=100001;++cnt)
        leftGroup[cnt] = rightGroup[cnt] = cnt;
    
    while(!vStack.empty()){
        v = vStack.top(); vStack.pop();
        
        //자신과 가장 가까이에 있는 왼쪽값과 오른쪽 값을 구함
        left = findLeft(v-1), right = findRight(v+1);
        
        //자신은 이제 트리에 없는 값이 될 것이므로 자신을 가리키지 않도록 왼쪽과 오른쪽 값을 저장함
        leftGroup[v] = left, rightGroup[v] = right;
        
        //재귀함수 스택 오버플로우 방지용
        //[v,right-1], [left+1,v] 구간에 있는 모든 값은 모두 이진트리에 없기 때문에 이를 이용해 배열을 업데이트 함
        findLeft(right-1), findRight(left+1);
        
        //삽입할 값과 가장 가까운 왼쪽값, 오른쪽값을 스택에 저장함
        rangeStack.push(make_pair(v,make_pair(left,right)));   
    }
    
    while(!rangeStack.empty()){
        v = rangeStack.top().first, left = rangeStack.top().second.first, right = rangeStack.top().second.second;
        rangeStack.pop();
        
        //구간 중 루트와 거리가 더 먼 노드를 채택해 v노드에 기록하고 result에 높이를 반영함
        res+=(disFromRoot[v] = max(disFromRoot[left], disFromRoot[right])+1)-1;
        
        printf("%lld\n",res);
    }
    return 0;
}

/*
//solved with fenwick tree and binary search : 200ms
#include <cstdio>

#define max(x,y) (x>y?x:y)

int n, v, fenwickTree[100010], distanceFromRoot[100010];
long long result;

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
        
        if(sumOneToNum(mid <= val) left = mid+1;
        else right = mid-1;
    }
    return left;
}

int main() {
    ("%d", &n); n+=2;
    update(1,1);
    update(n,1);
    for(int cnt=2; cnt<n; ++cnt){
        scanf("%d", &v); ++v;
        int vSum = sumOneToNum(v), left = binarySearch(vSum-1), right = binarySearch(vSum);
        result += (distanceFromRoot[v] = max(distanceFromRoot[left], distanceFromRoot[right])+1)-1;
        update(v, 1);
        printf("%lld\n", result);
    }
    return 0;
}
*/

/*
//solved with set container : 300ms
#include <cstdio>
#include <set>
using namespace std;

#define max(x,y) (x>y?x:y)

int n, v, distanceFromRoot[100002];
lojg long result;
set<int> insertedNum;

int main() {
    scanf("%d", &n);
    insertedNum.insert(0);
    insertedNum.insert(n+1);
    for(int cnt=0; cnt<n; ++cnt){
        scanf("%d", &v);
        auto right = insertedNum.lower_bound(v), left = right; --left;
        result += (distanceFromRoot[v] = max(distanceFromRoot[*left], distanceFromRoot[*right])+1)-1;
        insertedNum.insert(v);
        printf("%lld\n", result);
    }
    return 0;
}
*/
