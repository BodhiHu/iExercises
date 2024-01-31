package app.exams;

import java.util.ArrayList;
import java.util.List;

public class ArrayExam {
  public static void moveZeroes(int[] nums, int numsSize) {
    List<Integer> numsList = new ArrayList<>();
    for (int num: nums) {
      if (num != 0) {
        numsList.add(num);
      }
    }

    for (int i = 0; i < numsList.size(); i++) {
      nums[i] = numsList.get(i);
    }

    int zerosCount = nums.length - numsList.size();
    for (int i = 0; i < zerosCount; i++) {
      nums[i + numsList.size()] = 0;
    }
  }
}
