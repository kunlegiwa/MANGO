# Mango Test

This is a Python package to draw distributions.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Mango Test.

```bash
pip install --upgrade git+https://kunlegiwa:@github.com/kunlegiwa/MANGO.git
```

## Usage

```python
from Mango_Dist import distribution_functions as df
from Mango_Dist.distribution_classes import Distribution

print(df.draw('lognormal', size=5, mean=4, sigma=2))

dist1 = Distribution(size=3)
print(dist1.draw())
dist1.size = None
print(dist1.draw())
print(dist1.summarise())
```

## Contributing
Not currently being developed

## License
[MIT](https://choosealicense.com/licenses/mit/)