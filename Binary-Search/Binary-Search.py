def binarySearch(target,arr):
    floor_index = -1
    ceiling_index = len(arr)
    while floor_index + 1 < ceiling_index:
        distance = floor_index + ceiling_index
        half_distance = distance/2
        guess_index = floor_index + half_distance
        guess_value = arr[guess_index]
        if guess_value == target:
            return True
        if guess_value > target:
            ceiling_index = guess_index
        else:
            floor_index = guess_index
    return False
