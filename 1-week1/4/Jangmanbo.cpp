#include <iostream>
using namespace std;

int main() {
    int n, k, people = -1, skip = 0;
    bool next = true;
    cin >> n >> k;
    int* stones = new int[n];
    for (int i = 0; i < n; i++)
    {
        cin >> stones[i];
    }
    k--;
    do
    {
        people++;
        for (int i = 0; i < n; i++)
        {
            if (stones[i] > 0) {
                stones[i]--;
                skip = 0;
            }
            else if (skip < k) {
                skip++;
            }
            else {
                next = false;
                break;
            }
        }
        skip = 0;
    } while (next);
    cout << people;
    return 0;
}