#include<bits/stdc++.h>
using namespace std;
int fun(vector<int> A)
{
    vector<int> arr(A.size(),1);
    for(int i=1;i<A.size();i++)if (A[i]>A[i-1]) arr[i]=arr[i-1]+1;
    for(int i=A.size()-2;i>=0;i--) if (A[i]>A[i+1]) arr[i]=max(arr[i],arr[i+1]+1);
    int ans=0;
    for(auto i:arr)
    ans+=i;
    return ans;
}
int main()
{
    vector<int> arr;

}