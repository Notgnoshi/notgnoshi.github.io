---
layout: post
title: Using your favorite iDevice on Linux
meta: A list of out-of-date methods for syncing music to your Apple iDevice on Linux
---

Anyone that has tried to use their iDevice alongside a Linux install knows the excruciating pain of attempting to sync music or, God forbid, other media to their device. Reddit, Ask Ubuntu, the Ubuntu Forums, and other various and assorted places on the internet people turn to for help in their darkest hours are littered with questions relating to these issues. However, not a single one of the myriad of answers and third party tools I found helped. I suspect this is because many of the answers I found were several years old, and in Apple's infinite wisdom, Apple continually changes their device protocols.

The simple answer to one asking how to use their device on a Linux OS is either "You don't." or "Just use Apple's music store, so you can download right on your device." This isn't acceptable for most people (people like me who buy their music from Amazon's store). However, this is not for lack of trying to find a solution to our woes. I keep finding what feels like an infinite number of solutions that while looking promising, fail to deliver. It just doesn't make sense to complain about incomplete solutions without adding my own incomplete solution to the chaos, so here we go.

## My Solution:

The first thing to note is that I have an iPhone 6 running jailbroken iOS 8.4. I wanted a solution that would allow me to use the default Music App so that I could control my phone from my car stereo. Oh the vanity. I therefore focused on trying to either get a third party tool to sync my music, or getting iTunes to work. After messing around with Banshee and Rhythmbox, I quickly decided to turn my focus to running iTunes, third party tools just didn't seem to work at all. I am able to play the music *off* my phone using Rhythmbox, but I'm completely unable to copy music *to* my phone.

Everything I read about running iTunes using Wine indicated that it just wasn't going to happen, so I shifted focus to using a virtual machine. Ugh. I had limited success using Windows 7 in a VirtualBox VM. The first issue was that my product key would not work, and I'm not sure why. You can still use Windows 7 without a license, but it can be fairly frustrating. Another issue I had was that networking did not seem to work right out of the box as most of the solutions I found online seemed to indicate. Later, after I got everything working, the biggest problem I had was that iTunes would stop syncing my music after it copied anywhere from 80-200 songs; iTune's CPU usage in the guest OS dropped to 0%, and VirtualBox's CPU usage did the same in the host OS. Setting Virtualbox's priority to a higher setting, and setting iTune's priority higher seemed to help, but I'm not sure by how much.

### The Stepwise Process:

* Get Windows running inside VirtualBox.
  * Download and install the latest version of VirtualBox.
  * Download and install the Oracle VM VirtualBox Extension Pack.
  * Create a USB device filter for your device. Do this after you install the extension pack.
  * Set up a shared folder for your music library. I share my entire second hard drive.
    * This lets me copy music to the hard drive, and import it nicely into my library using iTunes, which will copy it into the appropriate artist's and album's folder.
    * I share my library between iTunes and Rhythmbox.
    * I have my music on my slower HDD so I don't fill up my SSD.
    * This folder will appear on your guest OS as a network drive.
  * Download and install iTunes.
    * I would also download and install Firefox.
* Get iTunes up and running.
  * The default iTunes library location will be in your C: drive. Don't do this unless you're okay with duplicating your music library on your virtual hard drive.
  * Change your iTunes library location.
    * Preferences > Advanced > iTunes Media folder location
    * My directory structure looks like:

      ```
HDD
└── Music Library
    ├── Automatically Add to iTunes
    ├── Books
    ├── Downloads
    └── Music
                ├── Artist 1
                ├── Artist 2
                └── Artist n
    ```
    * In my iTunes preferences, I have my library set as `E:\Music Library`
    * I have my library location set as `/media/Nots/HDD/Music Library/Music` in Rhythmbox's preferences. Most of the default options should work for you.
  * Import your music into your new iTunes library. Hopefully this won't duplicate your files, if it does, that's a mess.
* Sync your device.
  * Sadly, this will all register as a new music library, which will mean you will lose your ratings, playlists, play counts, etc. It also means that iTunes will have to delete all the music off your device and recopy it all.

### Problems:

* Syncing froze. A lot.
  * Enabling WiFi syncing helped considerably (700-800 songs before freezing) when I could get it to work, but did not eliminate the freezing.
  * Every time it froze, I had to force close the VM, and reboot my device.
  * Setting the VM's priority higher in Ubuntu's performance monitor, and iTune's priority in Window's task manager seemed to help, but this might have been psychological.
  * Using the Windows 10 Developer preview helped immensely, but invited its own problems. The least of which is what will happen July 29th when Windows 10 goes public.
    * The start button wouldn't work, I click, nothing happens. Not a big deal as I'm only using Windows 10 for iTunes.
    * Shared folders don't work out of the box. This might have been fixed by now with updates to VirtualBox, the extension pack, and the Guest Additions CD Image.
      * To fix, Disable 3D Acceleration under the VM `Settings > Display > Video`.
      * Open up the Guest Additions CD, and run the proper `VBoxWindowsAdditions` executable for your system.
      * Accept all the default options the wizard gives you until you get to the "Choose Components" page. Make sure that Direct3D Support is disabled.
      * Finish installing with the wizard. You'll know it worked if you get to a page asking you to reboot.
    * Networking did not work right out of the box for me using the NAT Network option. I had to use the Bridged Adapter setting. Even then half the time it doesn't work. But I'm using the VM to sync my music, not browse the internet.
  * Using Windows 10 helped the freezing, but did not eliminate it entirely. I instead froze every 300-600 songs, which was far better. I still had to force close the VM and reboot my device.
* I was unable to keep my old library.
  * I think there's a way to import/export an old library so you can keep your playlists and ratings, but I'm not sure how.
* Moving from Windows 7 to Windows 10 reset my library yet again.
* This method sadly doesn't sync playlists between Rhythmbox and iTunes. There might be a way, but I haven't investigated at all.
* Syncing with Windows 7 would not sync any of my album artwork. Using Windows 10 did.
* I was able to hear sound from the VM at one point, but not any more, I'm not sure what I changed, but I broke it. Also, the media keys on my keyboard work fine with Rhythmbox, but not iTunes, so I prefer to use Rhythmbox for listening anyways.

## Other Attempts/Things to Look Into:

While I finally settled on using iTunes inside a virtual machine, I did try a few other things. Most of these require having a jailbroken device though, so ignore these if that doesn't apply to you.

* Opening the device's file system with Nautilus. This requires using [Apple File Conduit 2](https://cydia.saurik.com/info/com.saurik.afc2d/){:target="_blank"} to access the interesting parts of your device's file system. Music is located in `/var/mobile/Media/iTunes_Control/Music/`. Opening the file system with Nautilus defaults to the `/var/mobile/Media/` directory. Inside the `Music` directory, you should see a bunch of different folders named `F00`, `F01`, ..., `Fnn`. Your music is seemingly randomly located in these folders without rhyme or reason. If we try to copy our music into these folders, we will not see our music show up in the Music app.

* This is where another jailbreak "tweak" comes in, but it's really an app. [Filza File Manager](https://moreinfo.thebigboss.org/moreinfo/depiction.php?file=filzafilemanagerDp){:target="_blank"} will allow us to not only view and edit files on our device's file system, it will allow us to import music from one location on our device to our music library. Boom. Exactly what we wanted. Except for one thing. You have to drag and drop your music files (copy paste if you're sophisticated) from your hard drive to your device. Not hard, except it freezes just like iTunes does. Because of this, I suspect that the freezing is because Ubuntu doesn't work so well with the AFC protocol, if you want to call it that. Unlike iTunes, which will pick up right where it left off, you have to find the last file to successfully transfer, and pick up from there. This was so frustrating I abandoned this method.

* Filza, however, has another tool that was fairly promising. Filza can host a webserver that allows you to browse, upload, download, and edit files on your device over your network, circumventing the USB AFC protocol entirely. This worked okay, but the webserver interface isn't as powerful as a local file manager like Nautilus. If you're patient, try this. After you upload all your files to your device though, you still have to import them to your device's music library, so uploading is only half the battle. I believe it would be possible to write a script to automate the uploading process, but I don't think it would be possible to do so on your device to automate adding your music to your music library. However, you can install Python 2.6 and a terminal emulator, so someone smarter than me with a lot more free time might be interested in this.

* It is important to note though, that your device doesn't have an omnipotent CPU, if you try to do too much at once, your device will freeze, and you'll have to respring.

* I also looked into using SSH to copy my music, but I didn't get very far with this. You'd have to use Filza to import the files to your library anyways. This requires you installing [OpenSSH](https://cydia.saurik.com/openssh.html){:target="_blank"} and changing your device's passwords, but that isn't too hard.

* The first thing I tried was also the most fruitless. I can open the music on my device with Rhythmbox and Banshee, but any attempt to sync my device, with or without AFC failed. Nearly every time I plug my device in, a Rhythmbox dialog opens asking if I want to initialize my iPod. It says:

  <br/>

  "Rhythmbox has detected a device that is probably an uninitialized or corrupted iPod. It must be initialized before Rhythmbox can use it, but this will destroy any song metadata already present. If you wish Rhythmbox to initialize the iPod, please fill in the information below. If the device is not an iPod, or you do not wish to initialize it, please click cancel."

  <br/>

  However, any attempt I make of initializing my device never does anything that I've noticed.

* Someone suggested to me that I try using Google Play Music. This involves uploading my sizable music library over a 0.31Mbps connection, something that I'm just not willing to do. However, if you have a connection that can handle uploading ten's and ten's of gigabytes of music, then I think this is the most promising. Note though, that it requires a network connection to stream the music to your device, or to download your library. Uploading my library only to download it again on a crappy rural network just doesn't appeal to me, but this does sound like the simplest solution. Google Play Music let's you upload up to 50,000 songs.

* It was also suggested to me that I try a commandline utility called `ifuse`. I was not able to figure out how to do this though.

I hope you find something that works for you!
