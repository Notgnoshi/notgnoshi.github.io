---
layout: post
title: Downloading your iPhone text messages as a SQLite database
meta: Here's how to access and download your iPhone text messages as a SQLite database. Requires your phone to be jailbroken. Also works for retrieving your voicemail.
---

<!-- Custom styles for the images -->
<link rel="stylesheet" href="{{ "/assets/styles/tables.css" | prepend: site.baseurl }}">

I wanted to find a specific message a friend sent me a while back, but we've sent so many messages back and forth it was impossible to find. Here's how you can access your entire text message history provided your iPhone is jailbroken.

First off, you'll need `openSSH` installed. The password for `root` and `mobile` accounts is `alpine` by default. You should change it immediately to something secure, like `hunter2` or `password`. My personal favorite password is `a`.

SSH into your iPhone. The local IP should be available under `Settings > WiFi > Whatever network you're on > IP Address`. Ignore my hell-themed hostnames -- it's been a rough semester. It should look something like this.

```
nots@abyss ~ $ ssh root@192.168.0.101
root@192.168.0.101's password:
root@abaddon ~ #
```

Next, change your password for both `mobile` and `root` accounts. Seriously. Do it.

```
root@abaddon ~ # passwd
Changing password for mobile.
Old password:
New password:
Retype new password:
root@abaddon ~ # passwd mobile
Changing password for mobile.
New password:
Retype new password:
root@abaddon ~ #
```

Now change to the `mobile` user -- we're not modifying *anything* on the phone so there's no need to tempt fate as `root`

```
root@abaddon ~ # su mobile
mobile@abaddon /var/root $
```

Everything we need is located in `/var/mobile/Library/SMS/`

```
mobile@abaddon /var/root $ cd /var/mobile/Library/SMS
mobile@abaddon ~/Library/SMS $
```

A quick `ls` tells us we're in the right spot

```
mobile@abaddon ~/Library/SMS $ ls
Attachments  Drafts  EmergencyAlerts  sms.db  sms.db-shm  sms.db-wal
mobile@abaddon ~/Library/SMS $
```

I've never had good luck doing *anything* over SSH on my iPhone, so I just elected to SCP everything to my desktop and work from there.

```
mobile@abaddon ~/Library/SMS $ scp sms.db nots@192.168.0.104:~/
The authenticity of host '192.168.0.104 (192.168.0.104)' can't be established.
Are you sure you want to continue connecting (yes/no)? yes
nots@192.168.0.104's password:
sms.db                                                          100% 2404KB   2.4MB/s   00:01    
mobile@abaddon ~/Library/SMS $ scp -r Attachments nots@192.168.0.104:~/
nots@192.168.0.104's password:
.
.
.
mobile@abaddon ~/Library/SMS $
```

We can now use a database browser to view our texts. I'm partial to [`sqlitebrowser`](http://sqlitebrowser.org/) which is in the default Ubuntu repositories.

```
nots@abyss ~ $ sudo apt install sqlitebrowser
nots@abyss ~ $ sqlitebrowser sms.db &
nots@abyss ~ $
```

The `handle` table has a list of all the numbers you've texted. Use the following to grab the message handle of the conversation you wish to view. `xxxyyyzzzz` is the phone number I'm interested in with no special characters, and no spaces.

```sql
SELECT * FROM `handle` WHERE `uncanonicalized_id` LIKE 'xxxyyyzzzz';
```

You should get the following

| ROWID | id           | country | service  | uncanonicalized-id |
|-------|--------------|---------|----------|--------------------|
| 178   | +1xxxyyyzzzz | us      | iMessage | xxxyyyzzzz         |

Make note of the `ROWID`, it's the `handle_id` we're going to use in the next statement. If you only use iMessage, the `account` field of the `message` table has each message's sender's phone number. However, I text more than just people with iPhones.

```sql
SELECT `text`, `is_from_me` FROM `message` WHERE `handle_id` LIKE '178';
```

This produces the following table of the last few texts between one of my roommates and I. He knows me well.

|     | text                | is-from-me |
|-----|---------------------|------------|
| &#8942; |                 |            |
| 160 | You in robotics lab | 0          |
| 161 | Yes                 | 1          |
| 162 | You in robotics lab | 0          |
| 163 | No, my room         | 1          |
| 164 | You in robotics lab | 0          |
| 165 | Yeah                | 1          |

One last thing to mention is the `Attachments/` folder. Attachments are not stored in a human-friendly format, so you might want to flatten the directory. Execute the following one level above the `Attachments/` directory

```sh
nots@abyss ~ $ find Attachments/ -mindepth 2 -type f -exec mv -i '{}' Attachments/ ';'
```

This will leave lots of empty directories scattered about, so run the following from inside `Attachments/` to clean it up.

```sh
nots@abyss ~/Attachments $ find . -type d -empty -delete
```

---

Related sidenote: your voicemails are stored as `.amr` files inside `/var/mobile/Library/Voicemail/`
