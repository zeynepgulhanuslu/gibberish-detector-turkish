
# Gibberish Detector

This is based off https://github.com/domanchi/gibberish-detector, and add support for Turkish characters.

## Examples

**Quickstart**:

```bash
$ gibberish-detector-tr train examples/big.txt tr-big.model
$ gibberish-detector-tr detect --model tr-big.model --string "ertrjiloifdfyyoiu"
True
```

**Training Large Corpuses**:

```bash
$ gibberish-detector-tr train $(ls examples/*) generic.model
```

**Interactive Detection**:

```bash
$ gibberish-detector-tr detect --model tr-big.model --interactive
Entering interactive mode. Press ctrl+d to quit.
Input text: "düzgün bir cümle"
False (2.375)
Input text: ertrjiloifdfyyoiu
True  (4.154)
```

## Installation

```
git clone https://github.com/zeynepgulhanuslu/gibberish-detector-turkish.git
cd gibberish-detector-turkish 
python setup.py install
```

## Usage

```
$ gibberish-detector-tr -h
usage: gibberish-detector-tr [-h] [--version] {train,detect} ...

positional arguments:
  {train,detect}
    train         Trains a model to be used for gibberish detection.
    detect        Uses a trained model to identify gibberish strings.

optional arguments:
  -h, --help      show this help message and exit
  --version       Display version information.
```

You can also use this as an imported module:

```python
>>> from gibberish_detector_tr import detector
>>> Detector = detector.create_from_model('big.model')
>>> print(Detector.is_gibberish('ertrjiloifdfyyoiu'))
True
```
