#! /usr/bin/env python3


def get_key(val, script):
    for key, value in script.items():
        if val == value:
            return key

