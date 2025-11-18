import java.util.*;

public class Main {
  public static int n;
  public static int[] nums;

  public static int calValue(int left, int right) {
    return (right - left - 1) * Math.min(nums[left], nums[right]);
  }

  public static void main(String[] s) {
    Scanner scanner = new Scanner(System.in);
    n = scanner.nextInt();
    nums = new int[n];
    for (int i = 0; i < n; i++) {
      nums[i] = scanner.nextInt();
    }
    int left = 0, right = n-1;
    int rst = 0;
    while (left < right) {
      rst = Math.max(rst, calValue(left, right));
      if (nums[left] < nums[right]) {
        left++;
      } else {
        right--;
      }
    }
    System.out.println(rst);
    scanner.close();
  }
}
