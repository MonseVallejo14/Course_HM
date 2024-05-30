def no_space(text):
    new_text = ""
    for char in text:
        if char != " ":
            new_text += char
    return new_text


def reverse(text):
    flipped_text = ""
    for char in text:
        flipped_text = char + flipped_text
    return flipped_text


def palindrome(text):
    text = no_space(text)
    flipped_text = reverse(text)
    return text.lower() == flipped_text.lower()


print(palindrome("Hello Murphy"))
print(palindrome("Radar"))
print(palindrome("reconocer"))
print(palindrome("yo hago yoga hoy"))
