# Pype

For when you forget the syntax for awk, grep, curl, sed etc. but have the perfect python
one-liner for the job. Pype lets you run python on data as you pipe it around in your terminal.

```bash
echo "python" | pype '_.upper()'
```
```
PYTHON
```

Import packages with the `-m` flag and change the name of the line variable with the `-n` flag.
```python
cat links.txt | pype 'requests.get(link).json()["coord"]["lon"]' -m requests -n link
```
