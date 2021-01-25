import operator

# heights = [0, 1, 0, 2, 1, 0, 1, 3, 3, 2, 1, 2, 1]
# heights = [4, 2, 0, 3, 2, 5]
# heights = [4, 2, 3]
# heights = [0, 0, 0, 2, 0, 2, 0, 0, 0]
# heights = [4,4,4,3,4,4]
# heights = [2, 1, 0, 1, 2, 3, 4]
# heights = [5, 4, 3, 2, 1, 2, 3]
# heights = [8, 6, 4, 2, 0, 2, 4, 6, 6, 5, 4, 3, 2, 1, 1, 1, 4, 6, 7, 4, 1, 0, 10, 5]
# heights = [4, 3, 2, 1, 2, 3, 4]
# heights = [3, 0, 3]
# heights = [0, 3, 0]

size = len(heights)


def fill_left_bucket():
    global final_bucket
    final_left_bucket = 0
    max_idx, max_height = max(enumerate(heights), key=operator.itemgetter(1))

    temp_max_idx = max_idx
    while 1:
        temp_heights = heights[: temp_max_idx]
        if temp_max_idx >= 1:
            left_max_idx, left_max_height = max(enumerate(temp_heights), key=operator.itemgetter(1))
            final_left_bucket += calculate_size(heights, left_max_idx, temp_max_idx)
            temp_max_idx = left_max_idx
        else:
            break

    return final_left_bucket


def fill_right_bucket():
    global final_bucket
    final_right_bucket = 0
    rev_heights = heights[::-1]
    max_idx, max_height = max(enumerate(rev_heights), key=operator.itemgetter(1))

    # special handling in case the highest is the first and the last of a list e.g. [4,3,2,1,2,3,4]
    if heights[0] == heights[size - 1] and heights[0] == heights[max_idx]:
        temp_max_idx = size - 1
    else:
        temp_max_idx = max_idx

    # left side fill
    while 1:
        temp_heights = rev_heights[: temp_max_idx]
        if temp_max_idx >= 1:
            left_max_idx, left_max_height = max(enumerate(temp_heights), key=operator.itemgetter(1))
            final_right_bucket += calculate_size(rev_heights, left_max_idx, temp_max_idx)
            temp_max_idx = left_max_idx
        else:
            break

    return final_right_bucket


def calculate_size(in_heights, left_fill_idx, right_fill_idx):
    if in_heights[left_fill_idx] < in_heights[right_fill_idx]:
        bucket = abs(in_heights[left_fill_idx] * (right_fill_idx - left_fill_idx))
        for idx in range(left_fill_idx, right_fill_idx):
            if in_heights[idx] <= in_heights[left_fill_idx]:
                bucket = bucket - in_heights[idx]
            else:
                bucket = bucket - in_heights[left_fill_idx]
    else:
        bucket = abs(in_heights[right_fill_idx] * (left_fill_idx - right_fill_idx))
        for idx in range(left_fill_idx, right_fill_idx):
            if in_heights[idx] <= in_heights[right_fill_idx]:
                bucket = bucket - in_heights[idx]
            else:
                bucket = bucket - in_heights[right_fill_idx]
    return bucket


l_idx = 0
r_idx = 0
for x_idx, x_height in enumerate(heights):
    if x_height != 0:
        l_idx = x_idx
        break

for x_idx, x_height in enumerate(reversed(heights)):
    if x_height != 0:
        r_idx = x_idx
        break

heights = heights[l_idx: size - r_idx]
size = len(heights)

final_bucket = fill_left_bucket() + fill_right_bucket()
print("Final Bucket Size = " + str(final_bucket))

