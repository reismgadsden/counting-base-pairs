"""
Program used to count base pairs given a RNA sequence
and a secondary structure.

author: Reis Gadsden
version: 09/02/2022
class: CS-5531-101 @ Appalachian State University
instructor: Dr. Mohammad Mohebbi
"""
sequence_dict = {
    "AU": 0,
    "CG" : 0,
    "GU" : 0
}

def main():
    sequence = input("Please enter gene sequence: ")
    secondary_struct = input("Please enter secondary structure (in dot-bracket notation): ")
    if not get_indexes(sequence, secondary_struct):
        print("Secondary Structure is not Properly Formatted.")
    else:
        for x in sequence_dict.keys():
            print(x + ": " +str(sequence_dict[x]))


def get_indexes(sequence, second_struct) -> bool:
    stack = []
    i = 0
    for x in second_struct:
        if x == "(":
            stack.append(i)
        elif x == ")":
            count_sequences(stack.pop(), i, sequence)
        i += 1
    return len(stack) == 0



def count_sequences(open_index, close_index, sequence):
    open_seq_char = sequence[open_index]
    close_seq_char = sequence[close_index]
    if ord(open_seq_char) > ord(close_seq_char):
        temp = close_seq_char
        close_seq_char = open_seq_char
        open_seq_char = temp
    sequence_dict[open_seq_char + close_seq_char] += 1


if __name__ == "__main__":
    main()