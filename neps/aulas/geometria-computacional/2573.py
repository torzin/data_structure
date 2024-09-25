import bisect
import bisect

def count_valid_squares(poles):
    poles.sort(key=lambda pole: (pole[0], pole[1]))

    y_coords = []
    count = 0

    for x, y in poles:
        # Check if the top-left corner is unique
        if not y_coords or y_coords[-1] < y + 1:
            # Find the range of y-coordinates for a valid square
            left_index = bisect.bisect_left(y_coords, y - 1)
            right_index = bisect.bisect_right(y_coords, y + 1)

            # Check if there are any poles within this range
            if right_index > left_index:
                # Check if the other three corners are valid
                for i in range(left_index, right_index):
                    y2 = y_coords[i]
                    if (x - 1, y2) in poles and (x, y2 - 1) in poles and (x - 1, y2 - 1) in poles:
                        count += 1

        # Add the current pole's y-coordinate to the data structure
        bisect.insort(y_coords, y)

    return count
# Get the number of poles
N = int(input())

# Read the pole positions
poles = []
for _ in range(N):
    x, y = map(int, input().split())
    poles.append((x, y))

# Count the number of valid squares
result = count_valid_squares(poles)

print(result)