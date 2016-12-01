#!/usr/bin/env python
# encoding: utf-8


def main():
    try:
        2 / 1
    except Exception as e:
        response = e
    else:
        2 / 0
        response = "ok"
    finally:
        print response


if __name__ == '__main__':
    main()
