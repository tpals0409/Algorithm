T = int(input())
for tc in range(1, T + 1):
    nums, change = input().split()
    change = int(change)

    num_list = list(nums)
    length = len(num_list)

    max_value = [0]

    visited = set()


    def dfs(nums, swaps_left):
        state = (''.join(nums), swaps_left)

        if state in visited:
            return
        visited.add(state)

        if swaps_left == 0:
            max_value[0] = max(max_value[0], int(''.join(nums)))
            return

        for i in range(length):
            for j in range(i + 1, length):
                nums[i], nums[j] = nums[j], nums[i]

                if nums[0] != '0':
                    dfs(nums, swaps_left - 1)

                nums[i], nums[j] = nums[j], nums[i]


    dfs(num_list, change)
    print(f"#{tc} {max_value[0]}")