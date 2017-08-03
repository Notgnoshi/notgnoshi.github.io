---
layout: post
title: My favorite shell utilities
meta: Some of my favorite shell utilities for cleaning whitespace, colorizing output, directory navigation, and file manipulation.
---

This is a collection of shell scripts and utilities that I've written and/or collected. Some of them I use regularly, some of them I've only used once but want to keep around for reference.

## up

---

The utility I use the most is a little script to enhance `cd ../`. All it does is go up `n` directories. However, it saves your last directory -- allowing the use of `cd -`, allowing you to jump back and forth between two directories.

```shell
# go up n levels
up()
{
    TMP=$PWD
    # default to one level
    LEVELS=${1:-1}
    for _ in $(seq "$LEVELS"); do
        cd ..
    done
    # $OLDPWD allows for `cd -`
    export OLDPWD=$TMP
}

alias back="cd -"
```

Example usage:

```shell
~ $ up
/home $ back
~ $ cd Documents/Projects/project/src/module/internal/include/
~/Documents/Projects/project/src/module/internal/include/ $ up 4
~/Documents/Projects/project/ $ back
~/Documents/Projects/project/src/module/internal/include/ $ touch generic.h
```

## additions and removals

These two Bash one liners give you the number of additions and removals the given author has made in a Git repository.

```shell
# Gives number of additions author has made in current git repo
additions()
{
    git log --author="$*" --pretty=tformat: --numstat | gawk ' { total += $1 } END { print total}
	
}

# Gives number of removals author has made in current git repo
removals()
{
    git log --author="$*" --pretty=tformat: --numstat | gawk ' { total += $2 } END { print total}
}

# Gives the value of (additions - removals) of removals author has made in current git repo
difference()
{
    git log --author="$*" --pretty=tformat: --numstat | gawk ' { delta += ($1 - $2) } END { print delta}
}
```

## dsort

---

I don't use this one often, but it has come in handy. It lists out folders in the current directory sorted by size.

```shell
# sorts directories by size
dsort()
{
    du -a -d 1 -h | sort -h
}
```

Example usage:

```shell
~ $ dsort
4.0K    ./.bash_aliases
4.0K    ./.bashrc
4.0K    ./.gitconfig
4.0K    ./.vimrc
16K     ./.bash_history
16K     ./.viminfo
40K     ./.ssh
40K     ./Desktop
840K    ./bin
374M    ./Documents
7.1G    ./Downloads
```

If you would like to reverse the sort order, add the `-r` flag to `sort`.

## localip

---

Here's one to grab your local IP address for those too lazy to read through the output of `ifconfig`.

```shell
# grabs the local IP
localip()
{
    echo "local IP(s):"
    echo ""
    ifconfig | perl -nle'/dr:(\S+)/ && print $1'
    # echo "local IP: $(hostname -I)"
}
```

There are a number of methods of grabbing this information. Scraping the output of `ifconfig` with Perl is what I've found to be the most reliable. If you do not want to get the `127.0.0.1` address, you can try using `hostname -I`, but it doesn't always work for me.

Example usage:

```shell
~ $ localip
local IP(s):

192.168.0.100
127.0.0.1
```

## publicip

---

Here's one to grab your public IP address.

```shell
# grabs the external IP
publicip()
{
    echo "public IP:"
    echo ""
    curl -s 'ipecho.net/plain'
    echo ""
}
```

Example usage:

```
~ $ publicip
public IP:

192.30.252.153
```

## Running a command repeatedly

---

This is just because I don't use Bash enough to memorize the syntax. Occasionally I find a need to repeat a command some fixed number of times. I can *never* remember where the semicolons go...

```shell
~ $ for i in {1..10}; do echo $i; done
```

## clean.sh

---

This is one I wrote to clean up a number of $$\LaTeX$$ documents I had that were poorly formatted. It strips trailing whitespace, converts tabs to a specified number of spaces, and makes sure there is a single trailing newline at the end of the file. It has a dependency on `sponge`, which is not installed by default.

```shell
#!/bin/sh

set -o errexit
set -o nounset

usage() {
    echo ""
    echo "    Usage: $0 <number of spaces> <filename>"
    echo ""
    echo "Converts tabs to the specified number of spaces and strips trailing whitespace from the given file,"
    echo "in addition to ensuring that there is one and only one newline at the end of the file."
    echo ""
}

main() {
    if [ $# -ne 2 ]; then
        usage
        exit 1
    else
        echo "Stripping trailing whitespace."
        sed -i 's/[ \t]*$//' "$2"

        echo "Converting tabs to spaces."
        expand -i --tabs="$1" "$2" | sponge "$2"

        echo "Ensuring only one newline at end of file"
        awk '/^$/ {nlstack=nlstack "\n";next;} {printf "%s",nlstack; nlstack=""; print;}' "$2" | sponge "$2"
    fi
}

main "$@"
```

I have not yet implemented file globbing, so to run on multiple files, you must do something like this:

```shell
for f in `ls *.tex`; do sh clean.sh 4 $f; done
```

## emailip.py

---

This one checks my external IP address against one saved in a file, and if they differ, emails me with the new IP address. I wrote this one a while ago, so please ignore the sloppy style.

I have two versions of this one, one that can run on a cronjob, and one that doesn't save my email password in plaintext. If you manage to get a script running on a cronjob to access a keyring, *please* let me know.
### Version 1
Depends on [`yagmail`](https://github.com/kootenpv/yagmail), does not save password in plaintext, but doesn't work in a cronjob.

```python
#!/usr/bin/python3
from datetime import datetime
import socket
import os
from urllib.request import urlopen
import yagmail


def gen_email(previous_ip, current_ip):
    f_time = datetime.now().strftime('%a %b %d at %H:%M')
    gw = os.popen('ip -4 route show default').read().split()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((gw[2], 0))

    gateway = gw[2]
    local_ip = s.getsockname()[0]
    hostname = socket.gethostname()

    p1 = '<p>Hostname: <code>{}</code></p>'.format(hostname)
    p2 = '<p>Gateway: <code>{}</code></p>'.format(gateway)
    p3 = '<p>Previous IP: <code>{}</code></p>'.format(previous_ip)
    p4 = '<p>Local IP: <code>{}</code></p>'.format(local_ip)
    p5 = '<p>Public IP: <code>{}</code></p>'.format(current_ip)

    body = p1 + p2 + p3 + p4 + p5

    # c.f. https://github.com/kootenpv/yagmail#username-and-password
    # TODO: get to work with a cronjob
    yag = yagmail.SMTP('username@example.com')
    to = 'username@example.com'
    subject = 'IP Address on ' + f_time

    try:
        yag.send(to=to, subject=subject, contents=body)
        print('Successfully sent {} at {}'.format(current_ip, f_time))
    except:
        print('Failed to send email.')


def main():
    with open('ip', 'r+') as f:
        ip1 = f.read()
        ip2 = urlopen('http://ipecho.net/plain').read().decode('utf-8')

        if ip1 != ip2:
            gen_email(ip1, ip2)
            f.seek(0)
            f.write(ip2)
            f.truncate()
        else:
            print('Your IP Address ({}) hasn\'t changed'.format(ip1))


if __name__ == '__main__':
    main()
```

### Version 2
Does not depend on a non-standard library, stores password in plaintext, will run on a cronjob. Sorry for the poor formatting, this was one of my first ever scripts that's been hacked together, features added, and Python versions changed.
```python
#!/usr/bin/python3
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import socket
import os
from urllib.request import urlopen
import json


def gen_email(old_ip):
    f_time = datetime.now().strftime('%a %d %b at %H:%M')
    gw = os.popen("ip -4 route show default").read().split()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((gw[2], 0))
    ip_addr = s.getsockname()[0]
    gateway = gw[2]
    hostname = socket.gethostname()

    ip = urlopen('http://httpbin.org/ip').read()
    ip = ip.decode('utf-8')
    ip = json.loads(ip)

    local_ip = "IP: " + ip_addr + "\n\tGW: " + gateway + "\n\tHost: " + hostname
    # public_domain, alias, addresslist = socket.gethostbyaddr(ip['origin'])

    toaddr = 'username@example.com'
    me = 'username@example.com'
    # TODO: use a keychain
    # c.f. https://github.com/kootenpv/yagmail#username-and-password
    gmail_pwd = 'xxxxxxxxxxxxxxxxxxx'
    subject = 'IP Address on ' + f_time

    ipDetails = "Local " + local_ip + "\n\tPublic IP: " + \
        ip['origin'] + "\n\tPrevious IP: " + old_ip  # + "\n\tPublic Domain: " + public_domain

    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s""" % (me, toaddr, subject, ipDetails)

    try:
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.ehlo()
        # s.starttls()
        s.login(me, gmail_pwd)
        s.sendmail(me, toaddr, message)
        s.quit()
        print("Successfully sent: " + ipDetails + "\non " + f_time)
    except:
        print("Failed to send mail")


def main():
    with open("ip", "r+") as f1:
        ip1 = f1.read()

        ip2 = urlopen('http://ipecho.net/plain').read().decode('utf-8')
        if ip1 != ip2:
            gen_email(ip1)
            f1.seek(0)
            f1.write(ip2)
            f1.truncate()
        else:
            print("Your IP Address hasn't changed")


main()
```

## window

---

There have been a few times I've needed to get all but the first few lines of a file, or ignoring the first few, grab the next few lines of a file. This can be accomplished by combining `head` and `tail` like so:

```shell
~ $ seq 1 10 > seq.txt
~ $ cat seq.txt
1
2
3
4
5
6
7
8
9
10
~ $ cat seq.txt | head --lines=6 | tail --lines=3
4
5
6
```

You can also use `head --lines=-NUM` to grab all but the last `NUM` lines, and you can use `tail --lines=+NUM` to grab all but the first `NUM` lines. What I wanted was a `window` command that would give me an arbitrary window that I could specify using `+NUM` to specify number of lines from the beginning and `-NUM` to specify number of lines from the end. This can be accomplished by properly piping together `head` and `tail` in some configuration, but the configuration can change based on how you specify the start point and end point.

My first attempt was in Bash, but I quickly abandoned that in favor of Python.

```python
#!/usr/bin/python3
import argparse
import sys


def parse_args():
    VERSION = '0.2'
    DESCRIPTION = 'window - an advanced head/tail.'
    parser = argparse.ArgumentParser(description=DESCRIPTION)

    parser.add_argument('-v', '--version',
                        action='version',
                        version=VERSION)
    parser.add_argument('--verbose',
                        action='store_true',
                        help='Print window dimensions.')
    parser.add_argument('from',
                        type=int,
                        nargs='?',
                        help='Beginning line number. Positive values are counted from the \
                              beginning, negative values from the end. Inclusive.',
                        default=1)
    parser.add_argument('to',
                        type=int,
                        nargs='?',
                        help='Ending line number. Positive values are counted from the    \
                              beginning, negative values from the end. Inclusive.',
                        default=-1)
    parser.add_argument('file',
                        type=argparse.FileType('r'),
                        default=sys.stdin,
                        nargs='?',
                        help='A file to use. Defaults to stdin.')

    # Turn args into a dictionary.
    args = vars(parser.parse_args())

    return args['verbose'], args['from'], args['to'], args['file']


def main():
    verbose, from_val, to_val, window_file = parse_args()
    if verbose:
        print('Taking window from line', from_val, 'to line', to_val)

    # Convert line number to index
    if from_val > 0:
        from_val -= 1

    # Negative values are one-indexed, but slicing uses exclusive endpoints.
    if to_val is -1:
        # Neat trick, list[x:None] is equivalent to list[x:]
        to_val = None
    elif to_val < 0:
        to_val += 1

    # Inefficient for extremely large amounts of data.
    for line in list(window_file)[from_val:to_val]:
        sys.stdout.write(line)


if __name__ == '__main__':
    main()
```

This can be called in a number of ways:

```shell
~ $ cat seq.txt | ./window.py 1 3
1
2
3
~ $ ./window.py 1 3 seq.txt
1
2
3
~ $ cat seq.txt | ./window.py -5 -1
6
7
8
9
10
```

I've wrapped `window.py` in a shell script to make if feel more native:

```shell
window()
{
    python3 ~/bin/window.py "$@"
}
```

After sourcing the function, it can be used it like so:

```
~ $ window --help
usage: window.py [-h] [-v] [--verbose] [from] [to] [file]

window - an advanced head/tail.

positional arguments:
  from           Beginning line number. Positive values are counted from the
                 beginning, negative values from the end. Inclusive.
  to             Ending line number. Positive values are counted from the
                 beginning, negative values from the end. Inclusive.
  file           A file to use. Defaults to stdin.

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
  --verbose      Print window dimensions.
```

## rsync

---

I've found myself needing to transfer very large amounts of data from one device to another on my local network. I have normally just used a portable SSD hard drive, but it only has 250 GB of storage. Just a few days ago I needed to transfer 300 GB (which could have been avoided with proper planning) and found SCP too slow to use for that much data, so I did some googling and found this:

```shell
~ $ rsync -aAXK --compress --progress /home user@host:/media/backup
```

Note `rsync` treats trailing slashes differently than you expect, so avoid including them.

## Terminal colors

---

I've exported a series of variables that will change the terminal color for use in larger scripts. For more information on the available color codes, see [this](https://unix.stackexchange.com/a/269085) Unix Stack Exchange answer. It has most everything you might want to know about terminal color codes.

```shell
export UNDERLINE=$(tput sgr 0 1)
export BOLD=$(tput bold)
export BLACK=$(tput setaf 0)
export RED=$(tput setaf 1)
export GREEN=$(tput setaf 2)
export YELLOW=$(tput setaf 3)
export BLUE=$(tput setaf 4)
export PURPLE=$(tput setaf 5)
export CYAN=$(tput setaf 6)
export WHITE=$(tput setaf 7)
export GRAY=$(tput setaf 8)
export LIGHTRED=$(tput setaf 9)
export LIGHTGREEN=$(tput setaf 10)
export LIGHTYELLOW=$(tput setaf 11)
export LIGHTBLUE=$(tput setaf 12)
export LIGHTPURPLE=$(tput setaf 11)
export LIGHTCYAN=$(tput setaf 11)
export RESET=$(tput sgr0)
```

Example usage:

```shell
~ $ echo "${BLUE}blue${RESET} ${RED}red${RESET}"
blue red
~ $ for i in {0..255}; do echo "$(tput setaf $i)test"; done
...
```
