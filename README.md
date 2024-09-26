# dummy-vrf
A dummy VRF implementation that is mostly for the purpose of testing libsodium.

## Prerequisites

- [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- [Libsodium](https://doc.libsodium.org/)

## Setup

- Install `libsodium`
```sh
$ sudo apt-get install libsodium-dev
```

- Install PyNacl library
```sh
$ pip install pynacl
```

## Run

- Execute script
```sh
$ python main.py
```
you should note that the `Output, Proof and Is valid` is printed out without errors.
