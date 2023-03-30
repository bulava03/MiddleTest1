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


def sort_words(word_count):
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:10]


def write_file(word_count, output_file_path):
    counter = 0
    with open(output_file_path, 'w') as file:
        for word, count in word_count:
            file.write(f'{word}: {count}\n')
            counter += 1
            if counter == 10:
                break


if __name__ == '__main__':
    file_path = 'example.txt'
    output_file_path = 'output.txt'
    text = read_file(file_path)
    words = count_words(text)
    sorted_words = sort_words(words)
    write_file(sorted_words, output_file_path)
