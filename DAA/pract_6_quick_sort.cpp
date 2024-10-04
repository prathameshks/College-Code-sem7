#include <iostream>
#include <vector>

using namespace std;

// Partition function
int partition(vector<int> &arr, int low, int high) {
    int pivot = arr[low];  // Choosing the first element as pivot
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

// Quick Sort function
void quickSort(vector<int> &arr, int low, int high) {
    if (low < high) {
        int pivotIndex = partition(arr, low, high);  // Partition the array and get pivot index
        quickSort(arr, low, pivotIndex - 1);         // Recursively sort the left part
        quickSort(arr, pivotIndex + 1, high);        // Recursively sort the right part
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
