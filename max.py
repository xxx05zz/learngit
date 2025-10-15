def max_subarray_sum(nums):
    """
    求解最大子数组和（Kadane算法）
    
    参数:
        nums: 整数列表，可能包含负数
        
    返回:
        最大子数组的和
    """
    if not nums:
        return 0  # 处理空列表情况
    
    max_current = max_global = nums[0]
    
    for num in nums[1:]:
        # 要么将当前元素加入现有子数组，要么从当前元素重新开始
        max_current = max(num, max_current + num)
        # 更新全局最大值
        if max_current > max_global:
            max_global = max_current
    
    return max_global


# 示例用法
if __name__ == "__main__":
    test_cases = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],  # 预期输出: 6 (子数组 [4,-1,2,1])
        [1],                                # 预期输出: 1
        [5, 4, -1, 7, 8],                   # 预期输出: 23
        [-1, -2, -3],                       # 预期输出: -1
        []                                  # 预期输出: 0
    ]
    
    for i, case in enumerate(test_cases):
        result = max_subarray_sum(case)
        print(f"测试用例 {i+1}: {case}")
        print(f"最大子数组和: {result}\n")
