from gendiff.modules import generate_diff


def test_generate_diff_flat():
    with open('tests/test_data/result_flat.txt') as f:
        result = f.read()[:-1]
    assert generate_diff('data/file1.json', 'data/file2.json') == result
    assert generate_diff('data/file1.yml', 'data/file2.yml') == result
    assert generate_diff('data/file1.yaml', 'data/file2.yaml') == result
    assert generate_diff('data/file1.yaml', 'data/file2.yml') == result
    assert generate_diff('data/file1.yml', 'data/file2.yaml') == result


def test_generate_diff_flat_expansions():
    with open('tests/test_data/result_flat.txt') as f:
        result = f.read()[:-1]
    assert generate_diff('data/file1.yaml', 'data/file2.yml') == result
    assert generate_diff('data/file1.yml', 'data/file2.yaml') == result
    assert generate_diff('data/file1.yml', 'data/file2.json') == result
    assert generate_diff('data/file1.json', 'data/file2.yaml') == result


def test_generate_diff_stylish():
    with open('tests/test_data/result_stylish.txt') as f:
        result = f.read()[:-1]
    assert generate_diff('data/file3.json', 'data/file4.json') == result
    assert generate_diff('data/file3.yml', 'data/file4.yml') == result
    assert generate_diff('data/file3.json', 'data/file4.yml') == result


def test_generate_diff_plain():
    with open('tests/test_data/result_plain.txt') as f:
        result = f.read()[:-1]
    assert generate_diff('data/file3.json', 'data/file4.json', 'plain') == result  # noqa: E501
    assert generate_diff('data/file3.yml', 'data/file4.yml', 'plain') == result
    assert generate_diff('data/file3.json', 'data/file4.yml', 'plain') == result


def test_generate_diff_json():
    with open('tests/test_data/result_json.txt') as f:
        result = f.read()[:-1]
    assert generate_diff('data/file3.json', 'data/file4.json', 'json') == result
    assert generate_diff('data/file3.yml', 'data/file4.yml', 'json') == result
    assert generate_diff('data/file3.json', 'data/file4.yml', 'json') == result
