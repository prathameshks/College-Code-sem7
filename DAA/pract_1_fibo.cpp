#include<iostream>
#include<vector>
using namespace std;

int steps = 0;

int fibo(int n,vector<int> &arr){
    steps++;
    if(n<=1){
        arr[n] = n;
        return n;
    }

    arr[n] = fibo(n-1,arr) + fibo(n-2,arr);
    return arr[n];
}

void print_vec(vector<int> &arr){
    for(int a=0;a<arr.size();a++) cout<<arr[a]<<" ";
    cout<<endl;
}

int main(){
    int n;
    cin>>n;
    vector<int> arr(n);
    fibo(n,arr);

    print_vec(arr);

    cout<<steps<<endl;

    return 0;
}