#include<bits/stdc++.h>
using namespace std;
bool visited[1000];
void dfs(vector<vector<int>> &graph, int root, int level)
{
    if(visited[root])
    return;
    for(int i=0;i<level;i++)
    cout<<"  ";
    
    cout<<root<<"\n";
    visited[root]=1;
    for(auto i:graph[root])
    {    
        dfs(graph,i,level+1);
        
    }
}

void bfs(vector<vector<int>> &graph, int root, int level)
{   
    vector<int> vis(1000,0);
    queue<int> list;
    list.push(root);
    vis[root]=1;
    while(list.size()>0)
    {   
        int curr=list.front();
        cout<<curr<<"\n";
        
        list.pop();
        for(auto i:graph[curr])
        {
            if(vis[i]==0)
            {
                list.push(i);
                vis[i]=1;
            }
        }

    }
}
int main()
{
    vector<vector<int>> graph(100);
    int v,e;
    cin>>v>>e;
    for(int i=0;i<e;i++)
    {   
        
        int x,y;
        cin>>x>>y;
        graph[x].push_back(y);
        graph[y].push_back(x);
        
    }
    for(int i=0;i<graph.size();i++)
    {       
        if(graph[i].size())cout<<i<<" -> (";
        for(int j=0;j<graph[i].size();j++)
        {
            cout<<graph[i][j]<<" , ";
        }
        if(graph[i].size())
        cout<<")\n";
    }
    cout<<"dfs\n";
    dfs(graph,1,0);
    cout<<"\n";
    
    cout<<"bfs\n";
    bfs(graph,1,0);
}
