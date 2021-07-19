#include <cstdio>
#include <algorithm>
using namespace std; 

int n, v, fenwickTree[100010], distanceFromRoot[100010], result;

void update(int num, int val){
    while(num<=100010)
        fenwickTree[num] += val, num += (num & -num);
}

int sumOneToNum(int num){
    int res = 0;
    while(num>0)
        res += fenwickTree[num], num -= (num & -num);
    return res;
}

int binarySearch(int val){
    int left = 1, right = n+2, mid;
    while(left <= right){
        mid = (left+right)/2;
        
        if(sumOneToNum(mid) <= val) left = mid+1;
        else right = mid-1;
    }
    return left;
}

int main() {
    scanf("%d", &n);
    update(1,1);
    update(n+2,1);
    for(int cnt=0; cnt<n; ++cnt){
        scanf("%d", &v); ++v;
        int vSum = sumOneToNum(v), left = binarySearch(vSum-1), right = binarySearch(vSum);
        result += (distanceFromRoot[v] = max(distanceFromRoot[left], distanceFromRoot[right])+1);
        update(v, 1);
        printf("%d\n", --result);
    }
    return 0;
}
