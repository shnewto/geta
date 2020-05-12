# geta, for when you need to "get a" random thing
A Python CLI app to get a random instance of a _thing_. It's starting out with simply providing random names, but I like the idea of the `geta` being able to get many more _things_.

## Installing 

Note: If you're not using a virtual environment, add a `--user` flag to the end of these commands.

#### pip
`geta` is pip installable so `python3 -m pip install geta` should do the trick. 

#### Build from source 
`python3 -m setup.py install` 

## Usage

### `geta name`

`geta name` uses the [names package](https://pypi.org/project/names/) to generate random first, last, and full names derived from 1990 US census data.

`geta name` defaults to providing a full name but you can specify first, last, or full.

```
✘ geta name
Sabrina Fusco

✘ geta name --full
Kenneth Halligan

✘ geta name --first
Valentina

✘ geta name --first
Patrica

✘ geta name --last
Monzo

✘ geta name --last
Walker
```
