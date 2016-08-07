---
layout: post
title: Argument Parsing in Python
meta: A brief example of argument parsing in Python using the argparse library
---

Argument parsing is one of those problems that occurs so often that it's foolish for us to reinvent the wheel every time. Luckily, someone more thoughtful than myself has written an amazing [tool](https://docs.python.org/3/library/argparse.html) to help parse Python script arguments.

Here's an extremely simple example script:

```python
#!/usr/bin/python3
import argparse

VERSION = '0.0.1 alpha'

parser = argparse.ArgumentParser(description='A simple demonstration of argparse.')

group = parser.add_mutually_exclusive_group()
group.add_argument('-v', '--verbose', action='store_true', help='increase output verbosity.')
group.add_argument('-q', '--quiet', action='store_true', help='decrease output verbosity.')

parser.add_argument('--foo', help='enable the FOO option', default='true', choices=('true', 'false', 'sometimes'))
parser.add_argument('bar', type=float, help='required input for the script (float)')
parser.add_argument('-c', '--count', action='count', help='-ccc --> 3')
parser.add_argument('--version', action='version', version=VERSION)

args = parser.parse_args()

if args.quiet:
    print('quiet mode.')
elif args.verbose:
    print('verbose mode.')

if args.foo == 'sometimes':
    print('enabling non-determinalistic mode.')

if args.count:
    print('--count flag used {} times (-{})'.format(args.count, 'c'*args.count))

print('bar = {}'.format(args.bar))
```

This produces the following help info

```
$ python3 argparse_test.py --help
usage: argv.py [-h] [--version] [-v | -q] [--foo {true,false,sometimes}] [-c] bar

A simple demonstration of argparse.

positional arguments:
  bar                   required input for the script (float)

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity.
  -q, --quiet           decrease output verbosity.
  --foo {true,false,sometimes}
                        enable the FOO option
  -c, --count           -ccc --> 3
  --version             show program's version number and exit
```

And the following output when run with `python3 argparse_test.py -cccc --verbose 42`

```
$ python3 argparse_test.py -cccc --verbose 42
verbose mode.
--count flag used 4 times (-cccc)
bar = 42.0
```

**Don't manually parse `sys.argv`!!** As easy as this is, everyone should be using it, even (especially) if all you need is simple functionality. Reinventing the wheel isn't worth the time you could spend procrastinating on something more valuable.
