# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    counter = 0
    current = 0
    end_index = len(c) - 1

    while current < end_index:
        # Skip a cloud if the one after it is safe
        if current < end_index - 1 and c[current + 2] == 0:
            current += 1
        # Increment counter and current
        current += 1
        counter += 1
        print(current)
    return counter
