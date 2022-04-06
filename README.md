# python-boilerplate

This template repository serves as a boilerplate for new python projects, and assumes that your project has the potential to be distributed as a package on [PyPI](https://pypi.org/), comes with a readthedocs page, and includes testing.


**Last Updated: April 6th, 2022**


The structure is as follows:

```
~/python-package-boilerplate/
    README.md
    LICENSE
    pyproject.toml
    setup.cfg
    src/
        python_package_boilerplate/
            __init__.py
            core.py
    docs/
        ...
    tests/
        ...
```

## `python-package-boilerplate/` files

[README.md]() is the README file for your project, in Markdown.

[LICENSE]() is the license your project is distributed under (the default for this template is [MIT](https://opensource.org/licenses/MIT)).

[pyproject.toml]() is specifies the build system, and in this template is filled out with default information[^1].

[^1]: https://setuptools.pypa.io/en/latest/build_meta.html


[setup.cfg]() is a configuration file used to configure `setuptools` and provide metadata about your project. Because this template assumes a `src/` structure for the package (that is, the code for the package is included in a subdirectory named `src/`), `setup.cfg` instructs `setuptools` to look there for the package itself[^2]. If your package has dependencies, they should be put here under `[options]` like so[^3]:

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



## `src/` files

This template assumes a `src/` structure for your project, which has a few benefits, making your project easier to test and distribute for other users[^4].

[^4]: https://hynek.me/articles/testing-packaging/

[python_package_boilerplate/]() is the top level directory for the code of your project.

[\_\_init\_\_.py]() essentially let's python know that this directory indeed is a package, it's left empty for this boilerplate project.

[core.py]() is your main module, assuming your package would be put into one module. Be sure to rename this to something better for your own project!



## `docs/` files



## `tests/` files



## Using the Template

### Building and Distributing 
Instructions for building and distributing your package can be found at [this link](https://packaging.python.org/en/latest/tutorials/packaging-projects/).
