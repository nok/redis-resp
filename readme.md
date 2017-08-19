# resp

## Installation

```bash
pip install resp
```

## Usage

```bash
python -m resp -i /path/to/big_dump.txt -r 'SET {0} {1}' | recis-cli --pipe
```

If the order of the data isn't relevant, you can split the origin file in multiple chunks and pipe them to the script:

```bash
cat /path/to/big_dump.txt | parallel --block 5M -j 4 --pipe python -m resp -r 'SET {0} {1}' --pipe | recis-cli --pipe
```

Don't forget to install the application [parallel](https://www.gnu.org/software/parallel/) on your system with `sudo apt-get install parallel` on Linux or `brew install parallel` on macOS.

## API

```bash
python -m resp [-h] [-r REDIS_CMD] [-i INPUT] [-d DELIMITER] [-p]
python -m resp [--help] [--redis_cmd REDIS_CMD] [--input INPUT] [--delimiter DELIMITER] [--pipe]
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