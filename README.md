# Slogger

**Slogger** is a simple preconfigured logger based on the built-in [logging](https://docs.python.org/3/library/logging.html) module. It is useful for small Python projects to simplify logging and debugging.

## Features

Slogger configures one logger with two handlers:

- **Standard Output**: Logs output to the console in a simplified format.
  ```
  06:00:03 | slogger - INFO | Configuring Simple Logger finished.
  ```
- **Log File Output**: Logs detailed output to a file with timestamps, thread, and module information.
  ```
  2024-09-09 06:00:03,053 | slogger - INFO | slogger.py:my_function:MainThread:614 >>> Configuring Simple Logger finished.
  ```
- A new log file is created daily in the platform-specific log folder, and the last 100 log files will be retained.

## Installation

1. Download `slogger.py`.
2. Place it in your project's directory or your Python path.

## Usage

Here is how you can use Slogger in your Python project:

```python
import logging
from slogger import setup_logging

# Setup the logger
setup_logging(loggername="slogger", appname="Simple Logger")

# Get the configured logger
app_logger = logging.getLogger("slogger")

# Log a message
app_logger.info("Configuring Simple Logger finished.")
```

## Requirements

- Python 3.8 or above.
- [platformdirs](https://pypi.org/project/platformdirs/) to determine the appropriate log folder.
