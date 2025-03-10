import io
import tempfile
from contextlib import redirect_stdout
from unittest import mock

import pytest

from gibberish_detector_tr.main import main


@pytest.mark.parametrize(
    'text, is_gibberish',
    (
        ('longer sentences have higher chance of being less gibberish', False),
        ('large', False),

        # Shorter words like this (even though it is in the corpus), raises errors.
        ('fox', True),
        ('ertrjiloifdfyyoiu', True),
    ),
)
def test_basic(basic_model_filename, text, is_gibberish):
    output = io.StringIO()
    with redirect_stdout(output):
        assert main(
            ['detect', '-m', basic_model_filename, '--string', text],
        ) == 0

    output.seek(0)
    assert (output.read().strip() == 'True') is is_gibberish


def test_update_model(basic_model_filename):
    # This is a smoke test
    with tempfile.NamedTemporaryFile('w+') as f:
        with redirect_stdout(f):
            assert main([
                'train', 'examples/quote.txt', '--amend', basic_model_filename,
            ]) == 0

        f.seek(0)
        with open(basic_model_filename) as g:
            assert f.read() != g.read()


def test_train_multiple_models():
    with tempfile.NamedTemporaryFile('w+') as f, tempfile.NamedTemporaryFile('w+') as g:
        with redirect_stdout(f):
            assert main(
                'train examples/big.txt examples/quote.txt'.split(),
            ) == 0

        with redirect_stdout(g):
            assert main('train examples/quote.txt'.split()) == 0

        f.seek(0)
        g.seek(0)

        assert f.read() != g.read()


def test_interactive(basic_model_filename):
    # This is a smoke test.
    with mock.patch('gibberish_detector_tr.main.input', side_effect=['blah', EOFError]):
        assert main(['detect', '-m', basic_model_filename, '-i']) == 0


@pytest.fixture(scope='module')
def basic_model_filename():
    with tempfile.NamedTemporaryFile('w+') as f:
        with redirect_stdout(f):
            assert main('train examples/big.txt'.split()) == 0

        f.seek(0)
        yield f.name
