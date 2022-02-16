"""
Program used to count base pairs given a RNA sequence
and a secondary structure.

author: Reis Gadsden
version: 09/02/2022
class: CS-5531-101 @ Appalachian State University
instructor: Dr. Mohammad Mohebbi
"""
import os
import matplotlib.pyplot as plt

total_sequence_dict = {
    "AT": 0,
    "AU": 0,
    "CG" : 0,
    "GU" : 0,
    "Total": 0
}

def main() -> None:
    ## sequence = input("Please enter gene sequence: ")
    ## secondary_struct = input("Please enter secondary structure (in dot-bracket notation): ")
    target_seq = input("Please enter the name of the sequence you want to count (type 'all' to print all sequences): ")
    if target_seq.strip().lower() == 'all':
        all_seq = read_all_files()
        for a in all_seq:
            sequence_dict = {
                "AT": 0,
                "AU": 0,
                "CG": 0,
                "GU": 0,
                "Total": 0
            }
            if not get_indexes(a[0], a[1], sequence_dict):
                print("Secondary Structure is not Properly Formatted.")
            else:
                print("Base pair counts for " + a[2])
                for x in sequence_dict.keys():
                    print("\t- " + x + ": " + str(sequence_dict[x]))
        print("\nTotal pair counts")
        for x in total_sequence_dict.keys():
            if x != "Total":
                print("\t- " + x + ": " + str(total_sequence_dict[x]) + "\n\t\t% of Total: "
                      + str((total_sequence_dict[x]/ total_sequence_dict["Total"]) * 100) + "%")
            else:
                print("\t- " + x + ": " + str(total_sequence_dict[x]))
        plot_dict(total_sequence_dict)
    else:
        sequence, secondary_struct = read_data(target_seq)
        if not get_indexes(sequence, secondary_struct):
            print("Secondary Structure is not Properly Formatted.")
        else:
            print("Base pair counts for " + target_seq)
            for x in total_sequence_dict.keys():
                print("\t- " + x + ": " +str(total_sequence_dict[x]))


def get_indexes(sequence, second_struct, single_dict=None) -> bool:
    stack = []
    i = 0
    for x in second_struct:
        if x == "(":
            stack.append(i)
        elif x == ")":
            if single_dict is None:
                count_sequences(stack.pop(), i, sequence)
            else:
                count_sequences(stack.pop(), i, sequence, single_dict)
        i += 1
    return len(stack) == 0



def count_sequences(open_index, close_index, sequence, single_dict=None) -> None:
    open_seq_char = sequence[open_index].upper()
    close_seq_char = sequence[close_index].upper()
    if ord(open_seq_char) > ord(close_seq_char):
        temp = close_seq_char
        close_seq_char = open_seq_char
        open_seq_char = temp
    total_sequence_dict[open_seq_char + close_seq_char] += 1
    total_sequence_dict["Total"] += 1
    if single_dict is not None:
        single_dict[open_seq_char + close_seq_char] += 1
        single_dict["Total"] += 1


def read_data(filename) -> tuple:
    dir_path = ".\\real_sec_structures"
    dir_content = os.listdir(dir_path)
    try_struct_1 = filename.lower() + "_pdb.sec_struct_1"
    try_struct_2 = filename.lower() + "_pdb.sec_struct_2"
    valid_name = try_struct_1
    if try_struct_1 not in dir_content:
        valid_name = try_struct_2
        if try_struct_2 not in dir_content:
            print("Invalid file name, exiting program.")
            exit(0)
    file_path = dir_path + "\\" + valid_name
    f = open(file_path, 'r')
    output = f.readlines()
    f.close()

    return output[1], output[2]


def read_all_files() -> list:
    container = list()
    dir_path = ".\\real_sec_structures"
    dir_content = os.listdir(dir_path)

    for x in dir_content:
        f = open(dir_path + "\\" + x, 'r')
        output = f.readlines()
        container.append([output[1], output[2], output[0][1:5]])
        f.close()

    return container


def plot_dict(dict) -> None:
    new_dict = dict

    for x in new_dict:
        if x != "Total":
            new_dict[x] = (new_dict[x]/new_dict["Total"]) * 100
    del dict["Total"]

    pairs = list(new_dict.keys())
    counts = list(new_dict.values())

    plt.bar(range(len(new_dict)), counts, tick_label=pairs)
    plt.ylim([0, 100])
    plt.show()


if __name__ == "__main__":
    main()