import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
  public static int[] getSmallestKNums(int[] nums, int k) {
    return Arrays.copyOfRange(quickSort(nums), 0, k);
  }

  public static int[] quickSort(int[] nums) {
    if (nums == null || nums.length <= 1) {
      return nums;
    }

    int base = nums[0];
    List leftNums = new ArrayList<Integer>();
    List rightNums = new ArrayList<Integer>();
    for (int i = 1; i < nums.length; i++) {
      if (nums[i] <= base) {
        leftNums.add(nums[i]);
      } else {
        rightNums.add(nums[i]);
      }
    }

    leftNums = quickSort(leftNums.toArray());
    rightNums = quickSort(rightNums.toArray());

    leftNums.add(base);
    leftNums.addAll(rightNums);
    return leftNums.toArray();
  }
}
