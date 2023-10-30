from project import get_user_input, set_up_spotify, get_username
import mock
import builtins


def test_get_user_input():
    with mock.patch.object(builtins, "input", lambda _: "cat"):
        assert get_user_input() == "cat"
    with mock.patch.object(builtins, "input", lambda _: "dog"):
        assert get_user_input() == "dog"


def test_set_up_spotify():
    with mock.patch.object(builtins, "input", side_effect=["cat ", "dog "]):
        value1, value2 = set_up_spotify()
        assert value1 == "cat"
        assert value2 == "dog"

    with mock.patch.object(builtins, "input", side_effect=[" cat ", " dog "]):
        value1, value2 = set_up_spotify()
        assert value1 == "cat"
        assert value2 == "dog"

    with mock.patch.object(builtins, "input", side_effect=["cat", "dog"]):
        value1, value2 = set_up_spotify()
        assert value1 == "cat"
        assert value2 == "dog"


def test_get_username():
    with mock.patch.object(builtins, "input", lambda _: "cat"):
        assert get_username() == "cat"

    with mock.patch.object(builtins, "input", lambda _: " cat"):
        assert get_username() == "cat"

    with mock.patch.object(builtins, "input", lambda _: " cat "):
        assert get_username() == "cat"
