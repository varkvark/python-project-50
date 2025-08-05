from gendiff.scripts.modules import generate_diff


def test_generate_diff_flat():
    with open('tests/test_data/result_flat.txt') as f:
        result = f.read()[:-1]

    assert generate_diff(
        'tests/test_data/data/file1.json',
        'tests/test_data/data/file2.json'
    ) == result

    assert generate_diff(
        'tests/test_data/data/file1.yml',
        'tests/test_data/data/file2.yml'
    ) == result

    assert generate_diff(
        'tests/test_data/data/file1.yaml',
        'tests/test_data/data/file2.yaml'
    ) == result

    assert generate_diff(
        'tests/test_data/data/file1.yaml',
        'tests/test_data/data/file2.yml'
    ) == result

    assert generate_diff(
        'tests/test_data/data/file1.yml',
        'tests/test_data/data/file2.yaml'
    ) == result


def test_generate_diff_flat_expansions():
    with open('tests/test_data/result_flat.txt') as f:
        result = f.read()[:-1]

    assert generate_diff(
        'tests/test_data/data/file1.yaml',
        'tests/test_data/data/file2.yml'
    ) == result

    assert generate_diff(
        'tests/test_data/data/file1.yml',
        'tests/test_data/data/file2.yaml'
    ) == result

    assert generate_diff(
        'tests/test_data/data/file1.yml',
        'tests/test_data/data/file2.json'
    ) == result

    assert generate_diff(
        'tests/test_data/data/file1.json',
        'tests/test_data/data/file2.yaml'
    ) == result


def test_generate_diff_stylish():
    with open('tests/test_data/result_stylish.txt') as f:
        result = f.read()[:-1]

    assert generate_diff(
        'tests/test_data/data/file3.json',
        'tests/test_data/data/file4.json'
    ) == result

    assert generate_diff(
        'tests/test_data/data/file3.yml',
        'tests/test_data/data/file4.yml'
    ) == result

    assert generate_diff(
        'tests/test_data/data/file3.json',
        'tests/test_data/data/file4.yml'
    ) == result


def test_generate_diff_plain():
    with open('tests/test_data/result_plain.txt') as f:
        result = f.read()[:-1]

    assert generate_diff(
        'tests/test_data/data/file3.json',
        'tests/test_data/data/file4.json',
        'plain'
    ) == result

    assert generate_diff(
        'tests/test_data/data/file3.yml',
        'tests/test_data/data/file4.yml',
        'plain'
    ) == result

    assert generate_diff(
        'tests/test_data/data/file3.json',
        'tests/test_data/data/file4.yml',
        'plain'
    ) == result


def test_generate_diff_json():
    with open('tests/test_data/result_json.txt') as f:
        result = f.read()[:-1]

    assert generate_diff(
        'tests/test_data/data/file3.json',
        'tests/test_data/data/file4.json',
        'json'
    ) == result

    assert generate_diff(
        'tests/test_data/data/file3.yml',
        'tests/test_data/data/file4.yml',
        'json'
    ) == result

    assert generate_diff(
        'tests/test_data/data/file3.json',
        'tests/test_data/data/file4.yml',
        'json'
    ) == result
