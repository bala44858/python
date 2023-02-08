#include<bits/stdc++.h>
using namespace std;



int main() {
    int n1;
    cin>>n1;
    vector <int> v1(n1);
    for(int& i:v1){
        cin>>i;
    }
    int n2;
    cin>>n2;
    vector <int> v2(n2);
    for(int& i:v2){
        cin>>i;
    }
    set  <int> set;

    for (int j :v1) set.insert(j);
    for (int jj :v2) set.insert(jj);
    for (int u :set) cout<<u<<" ";
    // map <int, int> dic;



    
    // vector <int> v2();
    // set<int> sett;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
