from gendiff.modules import generate_diff


def test_generate_diff():
    with open('tests/test_data/correct_flat_json.txt') as f:
        result = f.read()[:-1]
    assert generate_diff('data/file1.json', 'data/file2.json') == result
    print(generate_diff('data/file1.json', 'data/file2.json') == result)
