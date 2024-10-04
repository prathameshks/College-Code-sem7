#include <iostream>
#include <bits/stdc++.h>
using namespace std;

struct weights{
    int weight;
    int profit;
    double pw_ratio;

    weights(int w,int p){
        weight = w;
        profit = p;
        pw_ratio = (double)p/(double)w;
    }
};

void print(vector<weights> a){
    cout<<"-----------"<<endl;
    cout<<" W "<<" P "<<"P/W"<<endl;
    for(int i=0;i<a.size();i++){
        cout<<a[i].weight<<" "<<a[i].profit<<" "<<a[i].pw_ratio<<endl;
    }
    cout<<"-----------"<<endl;
}

bool cmp(weights a,weights b){
    return a.pw_ratio > b.pw_ratio;
}

int f_knapsack(vector<weights>arr,int capacity){
    int rem = capacity;
    int profit = 0;
    for(weights w:arr){
        cout<<"Selected -> Weight:"<<w.weight<<", Profit:"<<w.profit<< ", P/W Ratio:"<<w.pw_ratio<<endl;
        if(w.weight <= rem){
            rem-= w.weight;
            profit += w.profit;
        }else{
            // factional 
            int pf = w.pw_ratio * rem;
            profit += pf;       
            rem = 0;
            return profit;
        }
        cout<<"Capacity Remained:"<<rem<<", Profit:"<<profit<<endl;
    }
    return profit;
}

int main(){
    int n;
    cout<<"Enter Number of Weights:";
    cin>>n;

    vector<weights> arr;

    for(int i=0;i<n;i++){
        int a,b;
        cout<<"Enter Weight "<<i+1<<":";
        cin>>a;
        cout<<"Enter Profit "<<i+1<<":";
        cin>>b;
        weights w(a,b);
        arr.push_back(w);
    }
    cout<<endl;

    // sort(arr.begin(),arr.end(),[](weights a,weights b) return a.pw_ratio > b.pw_ratio);
    sort(arr.begin(),arr.end(),cmp);

    print(arr);

    int capacity;
    cout<<"Enter Capacity:";
    cin>>capacity;

    cout<<endl;
    cout<<"Maximum Profit:"<<f_knapsack(arr,capacity)<<endl;

    return 0;
}

/*
INPUT
5
10 5
15 10
20 20
25 40
30 50
60

OP
profit :95



*/