
# time O(n ^ 2) Space O(1)
def min_number_jumps(array: [int]):
    cur_idx = 0
    bound_idx = cur_idx + array[cur_idx]
    max_idx_val = 0
    jumps_count = 0
    while cur_idx < len(array):
        if cur_idx > bound_idx:
            cur_idx = max_idx_val
            jumps_count += 1
            bound_idx = cur_idx + array[cur_idx]
            max_idx_val += 1
            cur_idx += 1
        else:
            if array[max_idx_val] < array[cur_idx]:
                max_idx_val = cur_idx
            cur_idx += 1

    jumps_count += 1
    return jumps_count

def min_number_jumps_dp(array:[int]):
    pass
print(min_number_jumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))
