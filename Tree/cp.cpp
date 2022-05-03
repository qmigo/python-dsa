#include<bits/stdc++.h>
using namespace std;
int numRescueBoats(vector<int>& people, int limit) 
{   
    int n=people.size();
    sort(people.begin(),people.end());
    int l=0,r=n-1,ans=0;
    while(l<r){
        int sum = people[l]+people[r];
        if (sum>limit)
        r--;
        else
        {
            ans++;
            l++;
            r--;
        }
    }
    return n-ans;
}
int main()

{
    vector<int> arr;
    int n,lim;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        int x;
        cin>>x;
        arr.push_back(x);
    }
    cin>>lim;
    cout<<numRescueBoats(arr,lim);
}
