from gendiff.modules import generate_diff


def test_generate_diff_flat():
    with open('tests/test_data/correct_flat.txt') as f:
        result = f.read()[:-1]
    assert generate_diff('data/file1.json', 'data/file2.json') == result
    assert generate_diff('data/file1.yml', 'data/file2.yml') == result
    assert generate_diff('data/file1.yaml', 'data/file2.yaml') == result
    assert generate_diff('data/file1.yaml', 'data/file2.yml') == result
    assert generate_diff('data/file1.yml', 'data/file2.yaml') == result


def test_generate_diff_flat_extdiff():
    with open('tests/test_data/correct_flat.txt') as f:
        result = f.read()[:-1]
    assert generate_diff('data/file1.yaml', 'data/file2.yml') == result
    assert generate_diff('data/file1.yml', 'data/file2.yaml') == result
    assert generate_diff('data/file1.yml', 'data/file2.json') == result
    assert generate_diff('data/file1.json', 'data/file2.yaml') == result


def test_generate_diff_recursive():
    with open('tests/test_data/result.txt') as f:
        result = f.read()[:-1]
    assert generate_diff('data/file3.json', 'data/file4.json') == result
    assert generate_diff('data/file3.yml', 'data/file4.yml') == result
    assert generate_diff('data/file3.json', 'data/file4.yml') == result
