#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for index in range(length):

        complementary_number = limit - weights[index]
        found = hash_table_retrieve(ht, complementary_number)

        if found is not None:
            return (index, found)

        hash_table_insert(ht, weights[index],index)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
