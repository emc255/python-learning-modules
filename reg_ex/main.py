import re


def regular_expression_wildcard_part_two():
    text = "Only find the hyphen-words in this sentence. But you do not know how long-ish they are"
    pattern = r"[\w]+-[\w]+"
    match = re.findall(pattern, text)
    print(match)

    sentence_one = "Hello, would you like some catfish"
    sentence_two = "Hello, would you to take a catnap"
    sentence_three = "Hello, have yous seen this caterpillar"
    pattern = r"cat(fish|nap|claw)"
    match_one = re.search(pattern, sentence_one)
    print(match_one)
    match_two = re.search(pattern, sentence_two)
    print(match_two)
    match_three = re.search(pattern, sentence_three)
    print(match_three)


def regular_expression_wildcard_part_one():
    text = "the dog is here"
    pattern = r"dog|bird"
    match = re.search(pattern, text)
    print(match)
    text = "the bird is here"
    match = re.search(pattern, text)
    print(match)

    text = "the cat in the hat sat here"
    pattern_wildcard = r"at"
    match = re.findall(pattern_wildcard, text)
    print(match)
    pattern_wildcard = r".at"
    match = re.findall(pattern_wildcard, text)
    print(match)

    text = "1 is a number"
    pattern_wildcard_starts_with = r"^\d"
    match = re.findall(pattern_wildcard_starts_with, text)
    print(match)
    text = "is a number 2"
    pattern_wildcard_ends_with = r"\d$"
    match = re.findall(pattern_wildcard_ends_with, text)
    print(match)

    phrase = "there are 5 numbers in 44 and 6 of this is random"
    pattern_exclude = r"[^\d]+"
    match = re.findall(pattern_exclude, phrase)
    print(match)
    phrase = "This is a string! But it has punctuation. How can we remove it?"
    pattern_exclude = r"[^!.?]+"
    match = re.findall(pattern_exclude, phrase)
    print(match)


def regular_expression():
    text = "phone number is 401-441-4421"

    phone_pattern = r"\d{3}-\d{3}-\d{4}"
    phone = re.search(phone_pattern, text)
    print(phone.group())
    text = "phone number is 401-441-4421. mine was 222-212-6665"
    phone_pattern = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
    phones = re.findall(phone_pattern, text)
    print(phones)
    print("GROUPING")
    for index, phone in enumerate(re.finditer(phone_pattern, text)):
        print(f"{index}. {phone.group()}")
    print("CALL INDIVIDUAL")
    for index, phone in enumerate(re.finditer(phone_pattern, text)):
        print(f"{index}. {phone.group(1)}")
    for index, phone in enumerate(re.finditer(phone_pattern, text)):
        print(f"{index}. {phone.group(2)}")


def learning_pattern():
    text = "The agent phone number is 408-123-4444. Call soon"
    print("phone" in text)
    pattern = "phone"
    print(re.search(pattern, text))
    pattern = "not in text"
    print(re.search(pattern, text))
    pattern = "phone"
    match = re.search(pattern, text)
    print(match.span())
    print(match.start())
    text = "phone once,  phone again"
    matches = re.findall("phone", text)
    print(matches)
    for index, match in enumerate(re.finditer("phone", text)):
        print(f"{index}. {match.group()}")


def divider(title):
    print(f"=========={title.upper()}==========")


if __name__ == '__main__':
    divider("learning pattern")
    learning_pattern()

    divider("regular expression")
    regular_expression()

    divider("regular expression wildcard part one")
    regular_expression_wildcard_part_one()

    divider("regular expression wildcard part two")
    regular_expression_wildcard_part_two()
