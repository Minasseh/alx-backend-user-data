#!/usr/bin/env python3
""" Logging Filter """

import typing
import re


def filter_datum(fields: typing.List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ A function called filter_datum that returns
    the log message obfuscated """
    for f in fields:
        message = re.sub('{}=.+?{}'.format(f, separator),
                         '{}={}{}'.format(f, redaction, separator),
                         message)
    return message
