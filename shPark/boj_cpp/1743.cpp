#include <iostream>
#include <queue>

using namespace std;

bool fld[101][101];
bool visited[101][101];
int n, m, k;
int dx[] = { 1,0,-1,0 };
int dy[] = { 0,1,0,-1 };


int bfs(int x, int y){
    queue<pair<int, int>> q;
    pair<int, int> tmp;
    pair<int, int> tmp2;
    tmp.first = x;
    tmp.second = y;
    visited[x][y] = true;
    q.push(tmp);
    int cnt = 1;
    while (!q.empty()){
        tmp = q.front();
        q.pop();
        for(int i=0;i<4;i++){
            int nx = tmp.first + dx[i];
            int ny = tmp.second + dy[i];
            if (0<nx && nx<=n && 0<ny && ny<= m && visited[nx][ny] == false && fld[nx][ny]==true){
                cnt++;
                visited[nx][ny] = true;
                tmp2.first = nx;
                tmp2.second = ny;
                q.push(tmp2);
            }
        }
    }
    return cnt;
}


int main(){
    ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

    cin >> n >> m >> k;

    int x, y;
    for(int i=0;i<k;i++){
        cin >> x >> y;
        fld[x][y] = true;
    }

    int res = 0;
    int tmp;
    for(int i=1;i<=n;i++){
        for(int j=1;j<=m;j++){
            if(fld[i][j]==true && visited[i][j]==false){
                tmp = bfs(i, j);
                res = max(tmp, res);     
            }
        }
    }
    cout << res << "\n";
    return 0;
}