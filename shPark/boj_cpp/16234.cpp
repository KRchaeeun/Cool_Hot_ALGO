#include <iostream>
#include <queue>
#include <cmath>

using namespace std;

int N, L, R;
int val_arr[51][51];
bool visited[51][51];
int res_date = 0;
int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

// bfs
bool bfs(int x, int y) {
    
    if (visited[x][y]) {
        return false;
    }

    int population = val_arr[x][y];
    int contry_num = 0;

    queue<pair<int, int>> q;
    queue<pair<int, int>> list;
    pair<int, int> tmp;

    visited[x][y] = true;
    q.push(make_pair(x, y));
    list.push(make_pair(x, y));

    int nx, ny;
    while(!q.empty()) {
        tmp.first = q.front().first;
        tmp.second = q.front().second;
        q.pop();

        for(int i=0; i<4; i++) {
            nx = tmp.first + dx[i];
            ny = tmp.second + dy[i];

            // 정해진 범위 내인지 확인
            if (0<=nx && nx<N && 0<=ny && ny<N && visited[nx][ny] == false) {

                int ck_val = abs(val_arr[tmp.first][tmp.second] - val_arr[nx][ny]);

                // 값이 주어진 범위 내인지 확인
                if (L <= ck_val && ck_val <= R) {
                    q.push(make_pair(nx, ny));
                    list.push(make_pair(nx, ny));
                    population += val_arr[nx][ny];
                    contry_num++;
                    visited[nx][ny] = true;
                }
            }
        }
    }

    if (contry_num > 0) {
        contry_num++;
        int last_val = floor(population/contry_num);

        while (!list.empty()) {
            tmp.first = list.front().first;
            tmp.second = list.front().second;
            val_arr[tmp.first][tmp.second] = last_val;
            list.pop();
        }
        return true;
    }
    else {
        return false;
    }
}

void clear_visited () {
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            visited[i][j] = false;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);

    // input
    cin >> N >> L >> R;

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> val_arr[i][j];
        }
    }

    bool flg = true;
    while (flg){
        clear_visited();
        flg = false;
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                if (bfs(i, j)) {
                    flg = true;
                }
            }
        }
        if (flg) {
            res_date++;
        }
    }   

    // output
    cout << res_date << "\n";

    return 0;
}