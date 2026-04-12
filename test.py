def find_peaks(array):
    N = len(array)
    peak = array[0]
    index = 0
    output = []

    for x in range(1, N):
        # same sign check
        if array[x] * array[x - 1] >= 0:
            if peak < 0 and array[x] < peak:
                peak = array[x]
                index = x
            elif peak >= 0 and array[x] > peak:
                peak = array[x]
                index = x
        else:
            output.append((index, peak))
            peak = array[x]
            index = x

    # last segment
    output.append((index, peak))

    return output


# Test
array = [1,4,2,-2,-9,10,2,12,2,-4,-4,-4,-4,2,6,7]
print(find_peaks(array))