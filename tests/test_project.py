import pytest

from main import read_file, count_words, sort_words, write_file


@pytest.fixture
def example_file(tmpdir):
    file_path = tmpdir.join('example.txt')
    with open(file_path, 'w') as file:
        file.write('The quick brown fox jumps over the lazy dog.\n' * 10)
    return file_path


def test_read_file(example_file):
    assert read_file(example_file) == ('The quick brown fox jumps over the lazy dog. ' * 10)


@pytest.mark.parametrize('text, expected', [
    ('The quick brown fox jumps over the lazy dog.', {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}),
    ('', {}),
])
def test_count_words(text, expected):
    assert count_words(text) == expected


@pytest.mark.parametrize('word_count, expected', [
    ({'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}, [('the', 2), ('quick', 1), ('brown', 1), ('fox', 1), ('jumps', 1), ('over', 1), ('lazy', 1), ('dog', 1)]),
    ({}, []),
])
def test_sort_words(word_count, expected):
    assert sort_words(word_count) == expected


@pytest.mark.parametrize('word_count, expected', [
    ([('the', 2), ('quick', 1), ('brown', 1), ('fox', 1), ('jumps', 1), ('over', 1), ('lazy', 1), ('dog', 1)], 'the: 2\nquick: 1\nbrown: 1\nfox: 1\njumps: 1\nover: 1\nlazy: 1\ndog: 1\n'),
    ([], ''),
])
def test_write_file(tmpdir, word_count, expected):
    output_file_path = tmpdir.join('output.txt')
    write_file(word_count, str(output_file_path))
    with open(output_file_path, 'r') as file:
        assert file.read() == expected
