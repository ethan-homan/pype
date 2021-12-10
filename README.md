# Pype
Pype lets you run python on data as you pipe it around in your terminal.

## Installing

```bash
git clone https://github.com/ethan-homan/pype.git
cd pype
pip install .
```

## Usage

To make a string upper case:
```bash
>> echo "python" | pype '_.upper()'
PYTHON
```
To get the last value in a comma separated list:
```bash
>> echo "1,2,3,4,5" | pype '_.split(",")[-1]'
5
```

## Options
If you need to import packages for your one-liner, just pass them using the `-m` option.

We can use this to make GET requests on a list of URLs using `requests`, doing something similar to what could be done with `curl` and `jq`.
```python
cat links.txt | pype 'requests.get(_).json()["coord"]["lon"]' -m requests
```

If you want the variable that your input is called to be different than the default `_`, you can rename it using `-n` to make your one-liner easier to read.
```python
cat links.txt | pype 'requests.get(link).json()["coord"]["lon"]' -m requests -n link
```
