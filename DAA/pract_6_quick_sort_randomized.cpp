#include <iostream>
#include <vector>
#include <cstdlib>  // For rand() function

using namespace std;

// Function to swap two elements
void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

// Partition function
int partition(vector<int> &arr, int low, int high) {
    int pivot = arr[low];  // Choosing the pivot (which will be swapped to a random position)
    int left = low + 1;
    int right = high;

    while (true) {
        // Move left pointer to the right until an element greater than or equal to the pivot is found
        while (left <= right && arr[left] <= pivot) {
            left++;
        }

        // Move right pointer to the left until an element less than or equal to the pivot is found
        while (left <= right && arr[right] > pivot) {
            right--;
        }

        // If the left and right pointers have crossed, break out of the loop
        if (left > right) {
            break;
        }

        // Swap elements at left and right pointers
        swap(arr[left], arr[right]);
    }

    // Swap pivot element with element at right pointer to place the pivot in the correct position
    swap(arr[low], arr[right]);

    return right;  // Return the position of the pivot
}

// Randomized partition function to select pivot randomly
int randomizedPartition(vector<int> &arr, int low, int high) {
    int randomIndex = low + rand() % (high - low + 1);  // Generate a random index between low and high
    swap(arr[low], arr[randomIndex]);  // Swap the random element with the first element to use it as pivot
    return partition(arr, low, high);  // Call the partition function
}

// Quick Sort function
void quickSort(vector<int> &arr, int low, int high) {
    if (low < high) {
        int pivotIndex = randomizedPartition(arr, low, high);  // Partition the array using a random pivot
        quickSort(arr, low, pivotIndex - 1);                   // Recursively sort the left part
        quickSort(arr, pivotIndex + 1, high);                  // Recursively sort the right part
    }
}

int main() {
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    
    vector<int> arr(n);
    
    cout << "Enter the elements: " << endl; 
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    cout << endl;

    // Print original array
    cout << "Original Array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    // Perform Quick Sort
    quickSort(arr, 0, arr.size() - 1);

    cout << "Sorted Array: ";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}


/*
8
1 2 6 4 8 12 95 1

10
12 65 32 12 0 15 98 15 14 4

*/