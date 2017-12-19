def maxArea(height):
    i = 0
    j = len(height)-1
    max_water = 0
    while i < j:
        max_water = max(max_water,(j-i)*min(height[j],height[i]))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_water

arr = [1,1]
print maxArea(arr)
