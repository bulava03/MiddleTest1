import re


def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().replace('\n', ' ')
    return data


def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


if __name__ == '__main__':
    file_path = 'example.txt'
    output_file_path = 'output.txt'
    text = read_file(file_path)
