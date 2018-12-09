from main import data_path

DATA = data_path(__file__)


def node_sum(nums):
    childs = nums[0]
    shift = 2
    meta_sums = 0
    for ch in range(childs):
        next_shift, meta_sum = node_sum(nums[shift:])
        shift += next_shift
        meta_sums += meta_sum

    node_shift = shift + nums[1]
    meta_sums += sum(nums[shift:node_shift])

    return node_shift, meta_sums


def puzzle1():
    with open(DATA, 'r') as f:
        nums = f.read()

    nums = list(map(int, nums.split(' ')))

    _, meta_sum = node_sum(nums)

    print(meta_sum)


def node_sum2(nums):
    childs = nums[0]
    shift = 2
    meta_sums = []
    for ch in range(childs):
        next_shift, meta_sum = node_sum2(nums[shift:])
        shift += next_shift
        meta_sums.append(meta_sum)

    node_shift = shift + nums[1]
    if childs == 0:
        meta_sum = sum(nums[shift:node_shift])
    else:
        meta_sum = 0
        for meta in nums[shift:node_shift]:
            if meta <= len(meta_sums):
                meta_sum += meta_sums[meta - 1]

    return node_shift, meta_sum


def puzzle2():
    with open(DATA, 'r') as f:
        nums = f.read()

    nums = list(map(int, nums.split(' ')))

    _, meta_sum = node_sum2(nums)

    print(meta_sum)
