# some
A Python CLI app to provide you random instances of some _thing_. It's starting out with simply random names, but I like the idea of the `some` producing many more _things_.

## Usage

### `some name`

`some` uses the [names package](https://pypi.org/project/names/) to generate random first, last, and full names derived from 1990 US census data. 

`some` defaults to providing a full name but you can specify first, last, or full.

```
✘ python3 some/main.py name
Sabrina Fusco

✘ python3 some/main.py name --full
Kenneth Halligan

✘ python3 some/main.py name --first
Valentina

✘ python3 some/main.py name --first
Patrica

✘ python3 some/main.py name --last
Monzo

✘ python3 some/main.py name --last
Walker
```
