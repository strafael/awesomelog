<div align="center">
  <img src="https://github.com/rtogo/awesomelog/blob/master/doc/example1.png"><br>
</div>

-----------------

# awesomelog: beatiful console and file logging

## What is it
awesomelog is a Python package providing good looking console and file logging
configuration.

AwesomeLog is not a new logging framework, it's only a good looking
configuration for the bult-in `logging` package.

You just import it and move on with your coding.

## Example
```python
import awesomelog
import logging

logger = logging.getLogger(__name__)
logger.info('Log info example')
logger.debug('Log debug example')
```

You can also import logging directly from awesomelog:
```python
from awesomelog import logging
```

## Installation
You can install using `pip`:
```
pip install awesomelog
```

## License
MIT
