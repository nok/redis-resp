# resp

[![Build Status](https://img.shields.io/travis/nok/resp/master.svg)](https://travis-ci.org/nok/resp)
[![PyPI](https://img.shields.io/pypi/v/resp.svg)](https://pypi.python.org/pypi/resp)
[![PyPI](https://img.shields.io/pypi/pyversions/resp.svg)](https://pypi.python.org/pypi/resp)
[![GitHub license](https://img.shields.io/pypi/l/sklearn-porter.svg)](https://raw.githubusercontent.com/nok/resp/master/license.txt)

Making the [Redis](https://redis.io/) [Mass Insertion](https://redis.io/topics/mass-insert) simple.

## Installation

```bash
pip install resp
```

## Usage

```bash
python -m resp -i /path/to/dump.txt -d ',' -r 'RPUSH {0} {1}' | recis-cli --pipe
```

If the order of the data isn't relevant, you can split the origin file in multiple chunks and pipe them to the script concurrently:

```bash
cat /path/to/dump.txt | parallel -j4 --block 1M -I ,, --pipe 'python -m resp -r "SET {0} {1}" -p' | recis-cli --pipe
```

If [parallel](https://www.gnu.org/software/parallel/) isn't already installed on your system, you can install it with `sudo apt-get install parallel` on Linux or `brew install parallel` on macOS. 

## API

```bash
python -m resp [-h] -r REDIS [-i INPUT] [-d DELIMITER] [-p]
python -m resp [--help] --redis REDIS [--input INPUT] [--delimiter DELIMITER] [--pipe]
```

## Development

### Environment

Install the required [environment modules](environment.yml) by executing the script [environment.sh](recipes/environment.sh):

```bash
conda env create -c conda-forge -n resp python=2 -f environment.yml
source activate resp
```

### Testing

```bash
python -m unittest discover -vp '*Test.py'
```


## Questions?

Don't be shy and feel free to contact me by e-mail or on [Twitter](https://twitter.com/darius_morawiec).


## License

The module is Open Source Software released under the [MIT](license.txt) license.