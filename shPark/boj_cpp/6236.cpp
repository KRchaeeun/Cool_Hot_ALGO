#include <iostream>

using namespace std;

int n, m;
int money[100001];

int main () {
    ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);

    cin >> n >> m;

    int left = 0;
    int right = 0;

    for (int i=0; i<n; i++) {
        cin >> money[i];
        left = max(left, money[i]);
        right += money[i];
    }

    int mid = 0;
    int now_money = 0;
    int cnt = 0;
    while (left < right) {
        mid = (left + right) / 2;

        cnt = 0;
        for (int i=0; i<n; i++) {
            if ((now_money + money[i]) > mid) {
                now_money = 0;
                cnt++;
            }
            now_money += money[i];
        }
        if (now_money > 0) {
            cnt++;
            now_money = 0;
        }

        if(cnt <= m) right = mid - 1;
        else left = mid + 1;
    }

    cout << left << "\n";

    return 0;
}