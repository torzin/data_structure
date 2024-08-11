#include<bits/stdc++.h>
using namespace std;

#define MAX 123456
typedef long long ll;


int n, bit[MAX], nlis[MAX];

int setbit(int pos, int diff){
    while (pos <= n){
        bit[pos] += diff;
        pos += pos & -pos;
    }
}

int getbit(int pos){
    int ans = 0;
    while (pos){
        ans += bit[pos];
        pos -= pos & -pos;
    }
    return ans;
}

int main(void){
    int i, x, c, d;
    ll ans = 0;
    scanf("%d", &n);
    memset(bit, 0, sizeof(bit));
    for (i = 1; i <= n; i++){
        scanf("%d", &x);
        nlis[i] = x;
        setbit(i, x);
    }
    while (scanf("%c %d", &d, &c) != EOF){
        if (d == 'a'){
            setbit(c, -nlis[c]);
        }
        if (d == '?'){
            int ans = getbit(c-1);
            printf("%d", ans);
        }
    }
}