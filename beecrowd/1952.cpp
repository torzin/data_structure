#include<bits/stdc++.h>
using namespace std;

#define MAX 112
#define INF 112345678

struct pos{
    int i, j, k;
    pos() {}
    pos(int _i, int _j, int _k) : i(_i), j(_j), k(_k) {}
};


int n, m, l, dist[MAX][MAX][MAX];

int di[] = {2, 1, -2 , -1, 2, 1, -2, -1, 2, 0, -2, 0, 2, 0, -2, 0, 1, 0, 1, 0, 1, 0 -1, 0};
int dj[] = {1, 2, 1, 2, -1, -2, -1, -2, 0, 2, 0,-2, 0, 2, 0, -2, 0, 1, 0, -1, 0, 1, 0, -1};
int dk[] = {0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, -1, -1, -1, -1, 2 ,2, 2, 2, -2, -2, -2 , -2, -2};


int bfs(pos s, pos t){
    int i, j, k;
    queue<pos> q;
    for (i = 1; i <= n; i++)
        for(j = 1; j <= m; j++)
            for (k = 1; k <= l; k++) dist[i][j][k] = INF;
    dist[s.i][s.j][s.k] = 0; q.push(s);
    while (!q.empty()){
        pos u = q.front(); q.pop();
        for (int mov = 0; mov < 24; mov++){
            i = u.i + di[mov];
            j = u.j + dj[mov];
            k = u.k + dk[mov];
            if (i >= 1 && i <= n && 
                j >= 1 && j <= m && 
                k >= 1 && k <= l && dist[i][j][k] == INF){
                dist[i][j][k] = dist[u.i][u.j][u.k] + 1;
                q.push(pos(i, j, k));
            }}}

    return dist[t.i][t.j][t.k];
};


int main(void){
    pos s, t;
    scanf("%d %d %d", &n, &m, &l);
    scanf("%d %d %d", &s.i, &s.j, &s.k);
    scanf("%d %d %d", &t.i, &t.k, &t.k);
    printf("%d\n", bfs(s, t));
    return 0;
}