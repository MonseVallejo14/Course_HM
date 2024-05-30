from pprint import pprint

string = "murphy es un buen gato"


def no_space(text):
    return [char for char in text if char != " "]


def how_often(list):
    dictionary = {}
    for char in list:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary


def order(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True,
    )


def greater_tuples(list):
    maximum = list[0][1]
    answer = {}
    for order in list:
        if maximum > order[1]:
            break
        answer[order[0]] = order[1]
    return answer


def create_message(dictionary):
    message = "The ones that are most repeated are: \n"
    for key,  value in dictionary.items():
        message += f"- {key} with {value} repetitions\n"
    return message


without_spaces = no_space(string)
counted = how_often(without_spaces)
ordered = order(counted)
greater = greater_tuples(ordered)
message = create_message(greater)
print(message)
