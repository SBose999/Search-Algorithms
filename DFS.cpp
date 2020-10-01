#include<bits/stdc++.h>
using namespace std;


// Global
map<int, vector<int>> adjList;
map<int, int> vis;


void dfs(int src) {
    if(vis[src])
        return;
    vis[src] = true;
    for(auto &i: adjList[src])
        dfs(i);
}

int main () {
    // Input
    
    // Process
    
    
    return 0;
}
