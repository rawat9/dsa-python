import java.util.Arrays;

/**
 * BubbleSort Algorithm
 */
public class BubbleSort {

    public static void main(String[] args) {
        int[] arr = new int[] { 6, 5, 3, 1, 8, 7, 2, 4 };
        bubbleSort(arr);
        System.out.println(Arrays.toString(arr));
    }

    private static void bubbleSort(int[] arr) {
        int n = arr.length;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
}
