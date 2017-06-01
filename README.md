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

### Common install problems

Generic build steps could be found at [.travis.yml](.travis.yml) & [.appveyor.yml](.appveyor.yml)

#### Python version

*Not support python2.* At least python 3.3 with *setuptools (pip)* is required but newest version is recommanded especially on Windows

#### lupa build fails

See [lupa/INSTALL.rst#building-with-luajit2](https://github.com/scoder/lupa/blob/master/INSTALL.rst#building-with-luajit2)

#### Run fails

* Do not install from wheel or sdist. Directly install or install from egg. This is because the path of installed `data_files` is vary in other ways
* lupa *must bind with luajit,* not lua. It's not matter whether JIT is enabled (no big diff on speed) but it must be luajit
