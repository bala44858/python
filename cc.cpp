#include<bits/stdc++.h>
using namespace std;
int main(){
    int n1;
    cin>>n1;

    vector <int> v1(n1);
    for(int& i : v1) cin>>i;
    
    int n2;
    cin>>n2;
    vector <int> v2(n2);
    for(int& i:v2) cin>>i;
    set <int> set;
    // set.insert(90);
    for(int i : v1) set.insert(i);
    for(int j : v2) set.insert(j);

    for(int u:set)cout<<u<<" ";
    
    return 0;
}