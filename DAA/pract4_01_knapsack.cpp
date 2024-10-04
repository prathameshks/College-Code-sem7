#include <iostream>
#include <vector>
using namespace std;

int knapsack_01(vector<int> &weights, vector<int> &profits, int n, int m, vector<vector<int>> &dp) {
    if (n < 0) return 0;

    if (dp[n][m] != -1) return dp[n][m]; // Return if already calculated

    // If we cannot select the item at index n
    if (weights[n] > m) {
        return dp[n][m] = knapsack_01(weights, profits, n - 1, m, dp);
    }

    // If we select the item
    int acc = knapsack_01(weights, profits, n - 1, m - weights[n], dp) + profits[n];

    // If we don't select the item
    int not_acc = knapsack_01(weights, profits, n - 1, m, dp);

    return dp[n][m] = max(acc, not_acc);
}

int main() {
    cout << "0/1 KNAPSACK PROBLEM" << endl;
    vector<int> weights;
    vector<int> profits;

    int n, m;
    cout << "Enter number of items: ";
    cin >> n;

    cout << "Enter capacity of sack: ";
    cin >> m;

    weights.resize(n);
    profits.resize(n);

    for (int i = 0; i < n; i++) {
        cout << "Enter weight " << i + 1 << ": ";
        cin >> weights[i];
        cout << "Enter profit " << i + 1 << ": ";
        cin >> profits[i];
    }

    // Initialize dp array for memoization
    vector<vector<int>> dp(n, vector<int>(m + 1, -1));

    // Compute the maximum profit
    int max_profit = knapsack_01(weights, profits, n - 1, m, dp);
    cout << "Maximum Profit: " << max_profit << endl;

    return 0;
}


/*
sample input output
5
35
10
5
15
10
20
20
25
40
30
50

output
50

4
8
3
2
4
3
6
1
5
4

*/