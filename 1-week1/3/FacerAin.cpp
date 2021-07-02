#include <iostream>
#include <vector>
#include <algorithm>

/*
시간복잡도 O(4^N)
4^11 => 수행 가능
*/
using namespace std;

int MAX = -1000000005;
int MIN = 1000000005;
vector<int> num_list;
int N;

void sol(int n, int plus, int minus, int mul, int div)
{
    int oper_num = plus + minus + mul + div;
    if (oper_num == 0)
    {
        MAX = max(n, MAX);
        MIN = min(n, MIN);
    }

    if (plus > 0)
    {
        sol(n + num_list[N - oper_num], plus - 1, minus, mul, div);
    }
    if (minus > 0)
    {
        sol(n - num_list[N - oper_num], plus, minus - 1, mul, div);
    }
    if (mul > 0)
    {
        sol(n * num_list[N - oper_num], plus, minus, mul -1, div);
    }
    if (div > 0)
    {
        sol(n / num_list[N - oper_num], plus, minus, mul, div - 1);
    }
}

int main()
{
    cin >> N;
    int plus, minus, mul, div;
    int num;
	num_list.resize(N);
    for (int i = 0; i < N; i++)
    {
        cin >> num_list[i];

    }

    cin >> plus >> minus >> mul >> div; 

    sol(num_list[0], plus, minus, mul, div);

    cout << MAX << '\n' << MIN;


    return 0;
}