# resp

Resp makes the [Redis Mass Insertion](https://redis.io/topics/mass-insert) simple.

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