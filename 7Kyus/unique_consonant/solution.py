def count_consonants(text):
    voyelles = "aeiou"
    count = 0
    already_seen = []
    for letter in text.lower():
        if letter not in voyelles and letter not in already_seen and letter.isalpha():
            count += 1
            already_seen.append(letter)
    print(already_seen)
    return count

if __name__ == "__main__":
    print(count_consonants('sillystring'), 7)
    print(count_consonants('aeiou'), 0)
    print(count_consonants('abcdefghijklmnopqrstuvwxyz'), 21)
    print(count_consonants('Count my unique consonants!!'), 7)
