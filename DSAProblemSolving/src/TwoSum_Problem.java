import java.util.Arrays;
import java.util.HashMap;

public class TwoSum_Problem {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            if (map.containsKey(complement)) {
                return new int[]{map.get(complement), i};
            }

            map.put(nums[i], i);
        }

        return new int[0];
    }

    public static void main(String[] args) {

        int [] nums = {12, 17, 11, 15, 2, 7};
        int target = 9;
        TwoSum_Problem twoSum = new TwoSum_Problem();
        System.out.println(Arrays.toString(twoSum.twoSum(nums, target)));

    }
}