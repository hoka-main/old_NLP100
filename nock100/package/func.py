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


def to_split_row(file, split, indent):
    to_split_list = []
    for line in file:
        list_box = line.split(split)
        to_split_list.append(list_box[indent])
    return to_split_list


def make_line_list(file, split):
    result = []
    for line in file:
        r_strip_line = line.rstrip('\n')
        list_in_list = r_strip_line.split(split)
        num_box3 = list_in_list.pop()
        num_box2 = list_in_list.pop()
        list_in_list.append(int(num_box2))
        list_in_list.append(int(num_box3))
        result.append(list_in_list)
    return result

