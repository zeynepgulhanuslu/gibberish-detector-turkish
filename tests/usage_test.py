import pytest

from gibberish_detector_tr.usage import parse_args


def test_invalid_file():
    with pytest.raises(SystemExit):
        parse_args('train fake-file'.split())
