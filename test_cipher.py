
from main import encrypt, decrypt, caesar


def test_encryption():
    assert encrypt("Hello", 3) == "Khoor"


def test_decryption():
    assert decrypt("Khoor, Zruog!", 3) == "Hello, World!"


def test_invalid_shift_types():
    for shift in [True, False, "3", 2.5]:
        assert caesar("Hello", shift) == "Shift must be an integer value."


def test_shift_boundaries():
    assert encrypt("Hello", 1) == "Ifmmp"
    assert encrypt("Hello", 25) == "Gdkkn"

    for shift in [0, 26, -1, 30]:
        assert caesar("Hello", shift) == "Shift must be an integer between 1 and 25."

