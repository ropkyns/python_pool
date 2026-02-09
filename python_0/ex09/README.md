# ft_package

This is a simple example package, created from scratch, for the Python Piscine of 42.


#### To generate distribution packages :
    python3 -m pip install --upgrade build
    python3 -m build

#### To install the package (one of the two):
    pip install ./dist/ft_package-0.0.1.tar.gz
    pip install ./dist/ft_package-0.0.1-py3-none-any.whl

#### To test :
    pip show -v ft_package
    python test/test.py

#### To uninstall :
    pip uninstall ft_package
