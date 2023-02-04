# singlepy

Collection of Python modules for common tasks, in single module files with no dependencies

## Introduction

This repository holds a number of self-contained Python modules, all in a single file and
with no dependencies besides the Python standard library. Some dependencies might be
used if available in the system or virtual environment, but they are never mandatory.

The projects were developed for contexts where installing dependencies is impossible
or undesired, and to limit the scope of the projects themselves.

## Projects

The projects currently included in `singlepy`:

  - *`unicode2ascii`*: a simpler version of [`unidecode`](https://pypi.org/project/Unidecode/)

## Building

The projects don't require any dependency to run, but some dependencies are necessary to
build them. The building process is also necessary to update metadata information about
them, such as date of build, version, etc. A virtual environment to build the
project can be setup with the common Python practices:

```bash
$ python -m venv env
$ pip install -U pip wheel setuptools
$ pip install -r requirements.txt
```

The projects are built with:

```bash
$ ./build_projects.py
```