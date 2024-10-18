import java.util.Arrays;
import java.util.Random;

public class MergeSortComparison {
    // Threshold for switching to regular merge sort
    private static final int THRESHOLD = 10000;

    public static void parallelMergeSort(int[] arr) {
        if (arr.length < 2)
            return;

        if (arr.length < THRESHOLD) {
            // Use regular merge sort for small arrays
            regularMergeSort(arr);
            return;
        }

        int mid = arr.length / 2;
        int[] left = Arrays.copyOfRange(arr, 0, mid);
        int[] right = Arrays.copyOfRange(arr, mid, arr.length);

        // Create threads for recursive parallel sorting
        Thread leftThread = new Thread(() -> parallelMergeSort(left));
        Thread rightThread = new Thread(() -> parallelMergeSort(right));

        // Start both threads
        leftThread.start();
        rightThread.start();

        try {
            // Wait for both threads to complete
            leftThread.join();
            rightThread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Merge the sorted halves
        merge(arr, left, right);
    }

    // Regular merge sort for smaller arrays
    private static void regularMergeSort(int[] arr) {
        if (arr.length < 2)
            return;

        int mid = arr.length / 2;
        int[] left = Arrays.copyOfRange(arr, 0, mid);
        int[] right = Arrays.copyOfRange(arr, mid, arr.length);

        regularMergeSort(left);
        regularMergeSort(right);
        merge(arr, left, right);
    }

    // Merge function
    private static void merge(int[] arr, int[] left, int[] right) {
        int i = 0, j = 0, k = 0;

        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                arr[k++] = left[i++];
            } else {
                arr[k++] = right[j++];
            }
        }

        while (i < left.length) {
            arr[k++] = left[i++];
        }

        while (j < right.length) {
            arr[k++] = right[j++];
        }
    }

    public static void main(String[] args) {
        // Test with different array sizes
        int[] sizes = { 10000, 100000, 1000000 };

        for (int size : sizes) {
            // Generate random array
            int[] arr = new int[size];
            Random rand = new Random();
            for (int i = 0; i < size; i++) {
                arr[i] = rand.nextInt(1000000);
            }

            // Create copies for both sorting methods
            int[] arr1 = arr.clone();
            int[] arr2 = arr.clone();

            // Test regular merge sort
            long startTime = System.currentTimeMillis();
            regularMergeSort(arr1);
            long regularTime = System.currentTimeMillis() - startTime;

            // Test parallel merge sort
            startTime = System.currentTimeMillis();
            parallelMergeSort(arr2);
            long parallelTime = System.currentTimeMillis() - startTime;

            // Print results
            System.out.println("------------------------------");
            System.out.println("\nArray size Given: " + size);
            System.out.println("Regular Merge Sort time: " + regularTime + " ms");
            System.out.println("Parallel Merge Sort time: " + parallelTime + " ms");

            // verify is array is sorted
            System.out.println("Regular sort correct: " + isSorted(arr1));
            System.out.println("Parallel sort correct: " + isSorted(arr2));


            System.out.println("Parallel Merge Sort is " + String.format("%.2f", (double) regularTime / parallelTime) + " x times faster than regular Merge Sort");

            System.out.println("------------------------------");
        }
    }

    // Helper method to verify sorting
    private static boolean isSorted(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i + 1])
                return false;
        }
        return true;
    }
}