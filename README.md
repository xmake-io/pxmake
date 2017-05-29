# pxmake
xmake implement on python focuses on reuse python's library and API compatibility

## Intro

[xmake](https://github.com/tboox/xmake) is a make-like build utility based on Lua. Its low-level API (xmake machine) is implemented in C with library [tbox](https://github.com/tboox/tbox)

This repo, *pxmake*, is the reimplement of xmake machine on Python. Notice that the main part is still written in Lua and is same as xmake

pxmake created because to extend API for xmake in C is a little matter. pxmake focuses on reuse python's library and API compatibility with xmake

## Install

```console
$ python3 setup.py install
```
