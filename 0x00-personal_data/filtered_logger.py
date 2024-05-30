#!/usr/bin/env python3
""" Logging Filter """

import typing
import re


def filter_datum(fields: typing.List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ A function called filter_datum that returns
    the log message obfuscated """
    return re.sub(r'(?<=\{})(.*?)(?={})'.format(separator, separator),
                  redaction, message)
