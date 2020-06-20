def count(file_read):
    box = 0
    for _ in file_read:
        box += 1
    return box


def print_line(zip_type):
    for line, N in zip_type:
        if N < 0:
            break
        else:
            print(line)
            N -= 1


