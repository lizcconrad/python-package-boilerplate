# python-boilerplate

This template repository serves as a boilerplate for new python projects, and assumes that your project has the potential to be distributed as a package on [PyPI](https://pypi.org/), comes with a readthedocs page, and includes testing.

#### Contents
- [Top level files](#python-package-boilerplate-files)
- [`src/` files](#src-files)
- [`src/` files](#src-files)
- [`docs/` files](#docs-files)
- [`tests/` files](#tests-files)
- [Using the template](#using-the-template)
    - [Building and Distribution](#building-and-distributing)
    - [Running your tests](#running-your-tests)

**Last Updated: April 11th, 2022**


The structure is as follows:

```
~/python-package-boilerplate/
    README.md
    LICENSE
    pyproject.toml
    setup.cfg
    .gitignore
    src/
        python_package_boilerplate/
            __init__.py
            module.py
    docs/
        build/
            ... 
        source/
            _static/
            _templates/
            conf.py
            index.rst
            install.rst
        make.bat
        Makefile
    tests/
        __init__.py
        tests_module.py
```

## `python-package-boilerplate/` files

[README.md](https://github.com/lizcconrad/python-package-boilerplate/blob/master/README.md) is the README file for your project, in Markdown.

[LICENSE](https://github.com/lizcconrad/python-package-boilerplate/blob/master/LICENSE) is the license your project is distributed under (the default for this template is [MIT](https://opensource.org/licenses/MIT)). **FILL IN THE YEAR AND YOUR NAME!**

[pyproject.toml](https://github.com/lizcconrad/python-package-boilerplate/blob/master/pyproject.toml) is specifies the build system, and in this template is filled out with default information[^1].

[^1]: https://setuptools.pypa.io/en/latest/build_meta.html


[setup.cfg](https://github.com/lizcconrad/python-package-boilerplate/blob/master/setup.cfg) is a configuration file used to configure `setuptools` and provide metadata about your project. Because this template assumes a `src/` structure for the package (that is, the code for the package is included in a subdirectory named `src/`), `setup.cfg` instructs `setuptools` to look there for the package itself[^2]. If your package has dependencies, they should be put here under `[options]` like so[^3]:

```
[options]
#...
install_requires =
    req1
    req2 ==1.1
```

This `setup.cfg` also assumes that the project you're working on requires Python 3.6 or greater, which is also under `[options]`.

[^2]: https://setuptools.pypa.io/en/latest/userguide/declarative_config.html#declarative-config

[^3]: https://setuptools.pypa.io/en/latest/userguide/dependency_management.html

[.gitignore](https://github.com/lizcconrad/python-package-boilerplate/blob/master/.gitignore) includes a number of things that should not be pushed to the git repo for your project, this may need to be updated for your needs. A great template for putting together your own `.gitignore` file can be found [here](https://github.com/github/gitignore/blob/main/Python.gitignore).

## `src/` files

This template assumes a `src/` structure for your project, which has a few benefits, making your project easier to test and distribute for other users[^4].

[^4]: https://hynek.me/articles/testing-packaging/

`python_package_boilerplate/` is the top level directory for the code of your project.

[src/](https://github.com/lizcconrad/python-package-boilerplate/tree/master/src) is a subdirectory of `python_package_boilerplate/`

[mypackage/](https://github.com/lizcconrad/python-package-boilerplate/tree/master/src/mypackage) is a subdirectory of `src/` and contains the actual code for your package.

[\_\_init\_\_.py](https://github.com/lizcconrad/python-package-boilerplate/blob/master/src/mypackage/__init__.py) essentially let's python know that this directory indeed is a package, it's left empty for this boilerplate project.

[module.py](https://github.com/lizcconrad/python-package-boilerplate/blob/master/src/mypackage/module.py) is your main module, assuming your package would be put into one module. Be sure to rename this to something better for your own project!



## `docs/` files
This directory contains some starter Sphinx documentation files.

`build/` is the directory for the built files of your Sphinx documentation, you shouldn't touch anything here. It isn't present in this repository, but it will appear when you build the documentation. 

[source/](https://github.com/lizcconrad/python-package-boilerplate/tree/master/docs/source) is the directory with the files you'll actually work with. As it is now, `conf.py` is set up appropriately to generate the Sphinx documentation with AutoAPI so that it pulls docstrings from your python code in 'src/'. Do whatever you need to do with this documentation!

A readthedocs tutorial can be found [here](https://sphinx-tutorial.readthedocs.io/step-1/).

When working on your documentation, it's very helpful to set it to autobuild so you don't need to rebuild and refresh your browser every time you make a change[^5]. In order to do this, do the following:

```sh
pip install sphinx-autobuild
sphinx-autobuild [path/to/source/docs/] [path/to/build/html]
```

Then point your browser to [http://localhost:8000](http://localhost:8000)

[^5]: https://frankwiles.com/posts/automatically-rebuild-sphinx-docs/

When pushing your repository to github, you can import it as a project on your readthedocs account and it should generate correctly.


## `tests/` files
[\_\_init\_\_.py](https://github.com/lizcconrad/python-package-boilerplate/blob/master/tests/__init__.py) essentially let's python know that this directory is a package, it's left empty for the test directory too. 

[tests_module.py](https://github.com/lizcconrad/python-package-boilerplate/blob/master/tests/tests_module.py) contains a very basic unit test, though depending on the size of your project, you may want to split your tests into multiple files. You can learn about the python `unittest` framework [here](https://docs.python.org/3/library/unittest.html) and [here](https://geekflare.com/unit-testing-with-python-unittest/).




## Using the Template

### Building and Distributing
Instructions for building and distributing your package can be found at [this link](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

### Running your tests
Because this template assumes a `src/` layout for unit tests, you must install your package as an "edtiable install"[^6] in order for the testing package to be able to find it in your `$PYTHONPATH` and run the tests properly. To do this, simply run the following from the top directory of the project within the environment you're using:

```sh
pip install -e .
```

Then, from within your `tests/` directory you can run your tests like so:

```sh
python -m unittest tests_module
```


[^6]: https://pip.pypa.io/en/stable/cli/pip_install/#editable-installs