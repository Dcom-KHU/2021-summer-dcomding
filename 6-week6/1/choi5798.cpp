#include <iostream>
using namespace std;

int main()
{
    unsigned long long n;
    int answer = 0;
    int i=1;
    cin >> n;
    for(; i<=n; i*=2)
    {
        if(i > n) break;
    }
    cout << (unsigned long long)i/2;
    

    
}