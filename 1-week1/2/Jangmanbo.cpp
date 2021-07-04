#include <iostream>
using namespace std;

int total;

void hanoi(int n, int start, int end, int stopover)
{
    if (n == 1) total += end;
    else
    {
        hanoi(n - 1, start, stopover, end);
        total += end;
        hanoi(n - 1, stopover, end, start);
    }
}
int main() {
    int num;
    cin >> num;
    hanoi(num, 1, 3, 2);
    cout << total;
    return 0;
}