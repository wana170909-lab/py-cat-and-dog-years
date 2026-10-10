import pytest

from app import main


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 28, [2, 2]),
        (28, 28, [3, 2]),
        (28, 29, [3, 3]),
        (31, 33, [3, 3]),
        (32, 34, [4, 4]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, expected",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (27, 2),
        (28, 3),
        (31, 3),
        (32, 4),
        (100, 21),
    ],
)
def test_cat_age_only(cat_age: int, expected: int) -> None:
    assert main.get_human_age(cat_age, 0) == [expected, 0]


@pytest.mark.parametrize(
    "dog_age, expected",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (28, 2),
        (29, 3),
        (33, 3),
        (34, 4),
        (100, 17),
    ],
)
def test_dog_age_only(dog_age: int, expected: int) -> None:
    assert main.get_human_age(0, dog_age) == [0, expected]


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (-1, -1, [0, 0]),
        (-15, -15, [0, 0]),
        (-100, -100, [0, 0]),
        (-1, 15, [0, 1]),
        (15, -1, [1, 0]),
    ],
)
def test_negative_ages(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "invalid_age",
    ["10", 10.5, None, [10], True],
    ids=["string", "float", "none", "list", "bool"],
)
def test_invalid_cat_age_type(invalid_age: object) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(invalid_age, 10)


@pytest.mark.parametrize(
    "invalid_age",
    ["10", 10.5, None, [10], True],
    ids=["string", "float", "none", "list", "bool"],
)
def test_invalid_dog_age_type(invalid_age: object) -> None:
    with pytest.raises(TypeError):
        main.get_human_age(10, invalid_age)


def test_returns_list_of_two_elements() -> None:
    result = main.get_human_age(10, 10)
    assert isinstance(result, list)
    assert len(result) == 2


def test_returns_integers() -> None:
    result = main.get_human_age(50, 50)
    assert all(isinstance(age, int) for age in result)
