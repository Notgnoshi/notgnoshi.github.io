---
layout: post
title: My favorite shell utilities
meta: Some of my favorite shell utilities for cleaning whitespace, colorizing output, directory navigation, and file manipulation.
---

This is a collection of shell scripts and utilities that I've written and/or collected. Some of them I use regularly, some of them I've only used once but want to keep around for reference. All of these can be found in my dotfiles [repository](https://github.com/Notgnoshi/dotfiles).

* [up](#up)
* [ps and kill](#ps-and-kill)
* [man](#man)
* [fzf](#fzf)
* [gl](#gl)
* [uhist](#uhist)
* [notes.py](#notespy)
* [PS1](#ps1)
* [additions](#additions)
* [dsort](#dsort)
* [localip](#localip)
* [publicip](#publicip)
* [Running a command repeatedly](#running-a-command-repeatedly)
* [emailip.py](#emailippy)
* [window](#window)
* [rsync](#rsync)
* [Terminal colors](#terminal-colors)
* [rhyme](#rhyme)
* [randman](#randman)

## up

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

## ps and kill

I frequently need to find and kill processes, especially after a Python script that deals with multiple threads or processes fails to exit cleanly. The two commands below list, and then kill the desired processes. Note the use of `"[b]..."`! This prevents `grep` from finding the process running the `ps aux | grep "[b]asic_motion"` command.

```shell
$ ps aux | grep "[b]asic_motion"
nots     18684  0.1  0.4 2740052 66152 pts/2   S    18:07   0:00 python3 ./basic_motion.py
nots     18728  0.2  0.4 2740044 65792 pts/2   S    18:07   0:00 python3 ./basic_motion.py
nots     18797  0.3  0.4 2740044 65764 pts/2   S    18:07   0:00 python3 ./basic_motion.py
nots     18839  0.5  0.4 2740044 65776 pts/2   S    18:07   0:00 python3 ./basic_motion.py
nots     18881  0.6  0.4 2740040 65728 pts/2   S    18:07   0:00 python3 ./basic_motion.py
nots     18923  1.2  0.4 2740048 66012 pts/2   S    18:07   0:00 python3 ./basic_motion.py
$ kill -9 $(ps aux | grep "[b]asic_motion" | awk '{print $2}')
```

## man

I redefine `man` in my `.bashrc` to enable colored output in my man pages. This is extremely helpful when parsing through `printf(3)`, for example.

```shell
# Enable colored man pages
man()
{
    env \
    LESS_TERMCAP_mb="$(printf "\e[1;31m")"    \
    LESS_TERMCAP_md="$(printf "\e[1;31m")"    \
    LESS_TERMCAP_me="$(printf "\e[0m")"       \
    LESS_TERMCAP_se="$(printf "\e[0m")"       \
    LESS_TERMCAP_so="$(printf "\e[1;44;33m")" \
    LESS_TERMCAP_ue="$(printf "\e[0m")"       \
    LESS_TERMCAP_us="$(printf "\e[1;32m")"    \
        man "$@"
}
```

Here's a screenshot of `printf(3)`.

<img class="centered-full" src="{{ "/assets/posts/shell-utilities/colored-man.png" | prepend: site.baseurl }}" alt="colored-man">

## fzf

[`fzf`](https://github.com/junegunn/fzf) is a life-changer that I can no longer do without. It's the single best improvement I've made to my `.bashrc`. Install it, and learn how to use it. You can use `<ctrl-r>` to fuzzily seach your command history, similar to the default reverse history search, but several orders of magnitude better. You can use `<alt-c>` as a replacement for `cd` and readline-powered tab-completion. It takes some getting used to, but can save lots of time when you frequently need quick access to directories in a deep tree. You can use `<ctrl-t>` to fuzzily complete file arguments to commands.

I have the following settings in my `.bashrc`:

```shell
# Enable fzf
[ -f ~/.fzf.bash ] && source ~/.fzf.bash

# fzf settings to preview file tree when using <alt-c> and <ctrl-t>
export FZF_ALT_C_OPTS="--preview 'tree -C {} | head -200'"
export FZF_CTRL_T_OPTS="--preview 'tree -C {} | head -200'"
```

Here's a screenshot of the `<ctrl-r>` reverse history search. I was experimenting with a Bash script to recursively convert SVGs to PDFs because LaTeX apparently cannot directly include an SVG image.

<img class="centered" src="{{ "/assets/posts/shell-utilities/ctrl-r.png" | prepend: site.baseurl }}" alt="ctrl-r">

And here's a screenshot of `<ctrl-t>` with the preview tree enabled.

<img class="centered-full" src="{{ "/assets/posts/shell-utilities/ctrl-t.png" | prepend: site.baseurl }}" alt="ctrl-t">

## gl

I could have picked a better name for this utility, but now that it's in my muscle memory, I'm stuck with it. It's a Git commit browser that uses [`fzf`](https://github.com/junegunn/fzf) to fuzzily search, navigate, and preview the contents of a Git repository's commit log. I cannot live without this utility.

```shell
# Browse git log
gl()
{
    git log --graph --color=always \
        --format="%C(auto)%h%d %s %C(black)%C(bold)%an, %cr" "$@" |
    fzf --ansi --no-sort --reverse --preview  "echo {} | grep -o '[a-f0-9]\{7\}' | head -1 | xargs -I % sh -c 'git show --color=always %'" \
        --bind "enter:execute:
                (grep -o '[a-f0-9]\{7\}' | head -1 |
                xargs -I % sh -c 'git show --color=always % | less -R') << 'FZF-EOF'
                {}
FZF-EOF"
}
```

Note that you can use `<ctrl-j>` and `<ctrl-k>` or your arrow keys to navigate the list of commits, and if you hit `<enter>`, you'll open the full diff in `less`. I then alias `git gl` in my global `.gitconfig` as follows. For completeness, I've also included my `lg` and `ll` aliases.

```conf
gl    = !bash -c 'source ~/bin/utils.sh && gl'
lg    = log --color --graph --pretty=format:'%C(auto)%h%d %s %C(black)%C(bold)%an, %cr' --abbrev-commit --decorate
ll    = log --pretty=format:'%C(red)%h%C(reset) -%C(yellow)%d%C(reset) %s %C(bold blue) <%an>' --decorate --numstat --abbrev-commit
```

Here's a screenshot of some progress on a particularly frustrating homework problem in my Robotics class that just got pushed back by three weeks today.

<img class="centered-full" src="{{ "/assets/posts/shell-utilities/git-gl.png" | prepend: site.baseurl }}" alt="git-gl">

## uhist

This utility prints out your most common commands from your `.bash_history` commands. I used to have a Bash one-liner that did this, but I was unhappy with the format of the output, and the fact that it couldn't tell `git status` from `git push --force`.

```python
#!/usr/bin/env python3
"""
Analyze and print statistics about ~/.bash_history
"""
import argparse
from collections import Counter
from os.path import expanduser

# Commands like 'git' where 'git add' and 'git rebase' should be treated as
# distinctly different.
MULTI_COMMAND_COMMANDS = [
    'git',
    'ip',
    'route',
    'apt'
    'service',
    'sudo',
    'systemctl',
]

BASH_HISTORY = expanduser('~/.bash_history')

def get_subcommands(command):
    """Takes the root, or root + subcommand if indicated by MULTI_COMMAND_COMMANDS."""
    if not command:
        return ''
    root = command[0]
    if root in MULTI_COMMAND_COMMANDS and len(command) >= 2:
        root = root + ' ' + command[1]
    return root

def main(n):
    with open(BASH_HISTORY, 'r') as history:
        history = Counter(get_subcommands(c.split()) for c in history)
        total = sum(history.values())

        for command, count in history.most_common(n):
            print('\t{}\t{:05.2f}%\t{}'.format(count, (count / total) * 100, command))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', default=10, type=int, help='The number of most-common items to show')

    args = parser.parse_args()

    main(args.number)
```

## notes.py

I wrote this script to facilitate easier note-taking with Vim. So far I'm quite satisfied. Note that it's dependent on `parsedatetime` to parse the relative dates from the commandline arguments.

```python
#!/usr/bin/env python3
import argparse
import os
from datetime import datetime
from pathlib import Path
from subprocess import call

import parsedatetime

def parse_args():
    """
        Defines and parses commandline arguments for note-taking script.
    """
    DESCRIPTION = "A small script to facilitate taking, searching, and organizing notes."
    VERSION = "0.2"

    parser = argparse.ArgumentParser(description=DESCRIPTION)
    group = parser.add_mutually_exclusive_group()

    parser.add_argument('--version', action='version', version=VERSION)
    group.add_argument('--todo',
                       action='store_true',
                       default=False,
                       help='Open the TODO list.')
    group.add_argument('-r', '--relative',
                       nargs='+',
                       help='Open the note from a relative time. E.g. "yesterday" or "3 days ago"')
    return parser.parse_args()


def main():
    """
        Opens the note file, etc.
    """
    args = parse_args()

    # Try to use the default editor, or just insist on Vim.
    EDITOR = os.environ.get('EDITOR', 'vim')
    # Save the notes in a reasonable directory.
    NOTES_PATH = f'{Path.home()}/Documents/notes/'
    # E.g., '# Friday May 04 at 14:35:52', with an important newline.
    HEADER = f'# {datetime.now().strftime("%A %B %d at %X")}\n'

    if args.todo:
        FILENAME = 'todo.md'
    elif args.relative:
        args.relative = ' '.join(args.relative)
        cal = parsedatetime.Calendar()
        time, status = cal.parse(args.relative)

        if not status:
            print('Failed to parse relative time:', args.relative)
            exit(1)

        FILENAME = f'{datetime(*time[:6]).strftime("%Y-%m-%d")}.md'
    else:
        # E.g., '2018-05-04.md'.
        FILENAME = f'{datetime.now().strftime("%Y-%m-%d")}.md'

    path = Path(NOTES_PATH)
    if not path.exists():
        path.mkdir(parents=True)

    note = Path(NOTES_PATH + FILENAME)
    # Append the markdown header to file. Also creates the file if it doesn't exist.
    with open(note, 'a') as f:
        f.write(HEADER)

    # Ensure the file is read/writeable only by user, but only after the file is saved.
    os.chmod(note, 0o600)
    # Finally, open the file with the editor.
    call([EDITOR, note])


if __name__ == '__main__':
    main()
```

## PS1

I've fancified my PS1 to do a few things. First, it prepends my prompt with `(ssh)` when I'm connected via SSH. Second, it colors the ending `$` red if the previous command had a non-zero exit status.

```shell
# colored text variables.
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
export RESET=$(tput sgr0)

# Prints different escape codes to stdout indicating the exit code of the previous command
decorate_exit_status()
{
    if [ $? -eq 0 ]; then
        echo -e "${WHITE}"
        # echo -e "${BOLD}${GREEN}"
    else
        echo -e "${BOLD}${RED}"
    fi
}

# Determine if connected over ssh.
SSH_FLAG=0
if [ -n "$SSH_CLIENT" ] || [ -n "$SSH_TTY" ]; then
    SSH_FLAG=1
else
    case $(ps -o comm= -p $PPID) in
        sshd|*/sshd) SSH_FLAG=1;;
    esac
fi

if [ "$color_prompt" = yes ]; then
    # Set the base $PS1
    PS1="\u@\h \[${GREEN}\]\w"
    # If connected over SSH, prepend a red (ssh) to the $PS1
    if [ $SSH_FLAG -eq 1 ]; then
        PS1="\[${BOLD}${RED}\](\[${RESET}${RED}\]ssh\[${BOLD}\]) \[${RESET}\]${PS1}"
    fi
    # Append a colored $ to the end of the $PS1 indicating the exit code
    PS1="${PS1}\[\$(decorate_exit_status)\] \$ \[${RESET}\]"
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
```

Here are screenshots of both.

<img class="centered-real" src="{{ "/assets/posts/shell-utilities/ps1-exit-status.png" | prepend: site.baseurl }}" alt="ps1-exit-status">

<img class="centered-real" src="{{ "/assets/posts/shell-utilities/ps1-ssh.png" | prepend: site.baseurl }}" alt="ps1-ssh">

## additions

This Bash one liners give you the number of additions and removals the given author has made in a Git repository.

```shell
# Gives number of additions author has made in current git repo
additions()
{
    git log --author="$*" --pretty=tformat: --numstat |                        \
        awk '{ add += $1; subs += $2; loc += $1 - $2 } END                     \
             { printf "added lines: %s removed lines: %s total lines: %s\n", add, subs, loc }' -
}
```

Note that you can provide an author name (even one that includes spaces!). By default, it will show the total number of additions and removals.

```shell
$ additions AuthorName1
added lines: 67 removed lines: 22 total lines: 45
$ additions Author Name 2
added lines: 5405 removed lines: 3171 total lines: 2234
$ additions
added lines: 5472 removed lines: 3193 total lines: 2279
```

## dsort

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

Here's one to grab your local IP address for those too lazy to read through the output of `ifconfig`.

```shell
# grabs the local IP
localip()
{
    echo "local IP(s):"
    echo ""
    # ifconfig | perl -nle'/dr:(\S+)/ && print $1'
    echo "local IP: $(hostname -I)"
}
```

Depending on your distribution, you may need to scrape the output of `ifconfig`, or use the `hostname` command.

Example usage:

```shell
$ localip
local IP(s):

192.168.0.100
127.0.0.1
```

## publicip

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

```shell
$ publicip
public IP:

192.30.252.153
```

## Running a command repeatedly

This is just because I don't use Bash enough to memorize the syntax. Occasionally I find a need to repeat a command some fixed number of times. I can *never* remember where the semicolons go...

```shell
~ $ for i in {1..10}; do echo $i; done
```

## emailip.py

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

```text
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

I've found myself needing to transfer very large amounts of data from one device to another on my local network. I have normally just used a portable SSD hard drive, but it only has 250 GB of storage. Just a few days ago I needed to transfer 300 GB (which could have been avoided with proper planning) and found SCP too slow to use for that much data, so I did some googling and found this:

```shell
~ $ rsync -aAXK --compress --progress /home user@host:/media/backup
```

Note `rsync` treats trailing slashes differently than you expect, so avoid including them.

## Terminal colors

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

## rhyme

I stumbled across this one-liner a few years ago, and kept it in my path for those times I've needed something to save my sanity from the problem I'm facing.

```shell
# attempt to rhyme the given word
rhyme()
{
    { cat /usr/share/dict/words; printf %s\\n "$1"; } | rev | sort | rev | grep -FxC15 -e "${1?}" | grep -Fxve "$1" | shuf -n1;
}
```

Example:

```shell
$ rhyme purple
tipple
$ rhyme purple
Berle
$ rhyme purple
Marple
$ rhyme purple
dapple
```

As you can see, I've managed to replace an entire class of liberal arts students with a simple script.

## randman

I've learned about several new commands from the following utility to open a random man page.

```shell
# View a random man page
randman()
{
    man "$(ls -1 /usr/share/man/man?/ | shuf -n1 | cut -d. -f1)"
}
```
