<?php
class Solution {
    /**
     * @param Integer[]
     * @param Integer
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        $hasher = [];
        foreach ($nums as $idx => $num) {
            $complement = $target - $num;
            if (array_key_exists($complement, $hasher)) {
                return [$hasher[$complement], $idx];
            }
            $hasher[$num] = $idx;
        }
        return [];
    }
}

$nums = [2, 7, 11, 15];
$target = 9;

$sol = new Solution();
$result = $sol->twoSum($nums, $target);
print_r($result);
