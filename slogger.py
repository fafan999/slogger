# -*-coding:utf-8 -*-
"""Slogger (Simple Logger) configures a logger for your application that you can use right away."""
import logging.config
import os
from platformdirs import user_data_dir


def setup_logging(loggername="slogger", appname="Simple Logger", appauthor=None):
    """
    Configuring logger for the application.

    :param loggername: The name of the logger. You can use `logging.getLogger(loggername)` to get this logger, defaults to "slogger"
    :param appname: The name of the application, defaults to "Simple Logger"
    :param appauthor: The name of the author of the application, defaults to None
    """
    if not os.path.exists(os.path.join(user_data_dir(appname, appauthor), "logs")):
        if not os.path.exists(user_data_dir(appname, appauthor)):
            os.mkdir(user_data_dir(appname, appauthor))
        os.mkdir(os.path.join(user_data_dir(appname, appauthor), "logs"))
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "log": {
                "format": "%(asctime)s | %(name)s - %(levelname)s | %(filename)s:%(funcName)s:%(threadName)s:%(lineno)s >>> %(message)s",
                "class": "logging.Formatter",
            },
            "display": {
                "format": "%(asctime)s | %(name)s - %(levelname)s | %(message)s",
                "class": "logging.Formatter",
                "datefmt": "%H:%M:%S",
            },
        },
        "handlers": {
            "stdout": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "display",
                "level": "INFO",
            },
            "log": {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": os.path.join(user_data_dir(appname, appauthor), "logs", "slogger.log"),
                "when": "midnight",
                "backupCount": 100,
                "encoding": "UTF-8",
                "formatter": "log",
                "level": "DEBUG",
            },
        },
        "loggers": {
            f"{loggername}": {"handlers": ["stdout", "log"], "level": "DEBUG"},
        },
    }
    logging.config.dictConfig(LOGGING)
