# Gdb Scripts to Make Your Life Easier
## Overview
This repository contains a collection of scripts and Pretty Print functions to aid in your gdb workflow. Just a few examples included are:
* The ability to printer vectors with `print_vector VECNAME INDEX`
* Clean printing of Eigen matrices
* Clean printing of `boost::posix_time` structures.

## Install
### Repository Scripts
To install, run:
```
$ git clone --recursive https://github.com/ellislm/gdb_scripts.git ~/.gdb.d
```
Then add the following to your `~/.gdbinit`

```
source ~/.gdb.d/load_modules.py
source ~/.gdb.d/gdb_scripts
```
### Latest GDB
GDB 7+ is required for Python scripting to work. You can find the latest [version of gdb here](https://www.gnu.org/software/gdb/download/). Upon downloading and extracting the archive, run the following commands:
```
$ cd /path/to/extracted/gdb
$ ./configure --prefix=~/.local/ # Installs to local bin instead of root
$ make
$ make install
```
Ensure you've added `~/.local/bin` to your `$PATH` variable.
