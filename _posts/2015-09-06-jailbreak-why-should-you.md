---
layout: post
title: Why Should You Jailbreak?
meta: A list of my favorite jailbreak tweaks.
---

I made a lot of references to jailbreaking in a [post]({% post_url 2015-07-28-idevices-on-linux %}) about syncing music to my iPhone from Ubuntu. I could spend a lot of time telling you about the freedoms it gives you, but instead I'd like to just show you what tweaks I've installed on my device. The purpose here is twofold; I want to proselytize the [Holy Jailbreak Religion](https://reddit.com/r/jailbreak) while at the same time being a record of what I've done so far, so that if I ever have to restore my device (it's happened) I know exactly what I need to do to get my device back the way it was. Let's get started. I'll go through the tweaks by alphabetical order and ignore the dependencies that will be installed alongside them.

* **Acapella II**
  This allows you to swipe to skip songs on the lock screen, in Control Center, and in the music app. It also allows you to tap the app to play/pause. It doesn't work as well as some of the other older tweaks in my opinion, but they don't work yet in the new music app.
* **Activator**
  This is a good one. It allows you to activate (hence the name) different actions given various triggers. I have the following assignments:
  * Unlock the screen, turn off auto lock, and turn the brightness up to 80% when connected to a power source.
  * Turn on auto lock and turn the brightness down to 25% when disconnected from a power source.
  * Turn on your flashlight when you double press the sleep button.

  There are tons more things you can do, such as toggling your mobile data when you connect to WiFi, but I've elected to keep it simple.
* **Alkaline**
  This lets you change your battery icon.
* **AppInfo**
  This gives you information about the tweaks you have installed on your device. It also allows you to email yourself a detailed list of all installed tweaks and repos.
* **Apple File Conduit "2"**
  As indicated in my post about syncing music linked above, this let's you view your device's file system from your computer. It doesn't work so hot on Windows, but works pretty good fro browsing with Ubuntu.
* **Cylinder**
  Fancy schmancy icon animations when you swipe from page to page on your home screen.
* **Eclipse 2**
  Night mode. Quality varies by app, but I love it, especially for the settings app.
* **Filza File Manager**
  Lets you browse and edit your device's file system. Includes an editor for a variety of different filetypes.
* **Gauss 2 for iOS 8.4+**
  Makes the new Music app fancier looking. While, I couldn't get it looking right, you can set the tint color, the primary and secondary text colors, etc.

  <div style="width:100%px; margin:0 auto;">
    <img src="{{ "/assets/posts/why-jailbreak/now-playing.png"  | prepend: site.baseurl }}" alt="Now Playing" style="float:left; width:33.3%;"/>
    <img src="{{ "/assets/posts/why-jailbreak/album-view.png"  | prepend: site.baseurl }}" alt="Album View" style="float:left; width:33.3%;"/>
    <img src="{{ "/assets/posts/why-jailbreak/gauss-settings.png"  | prepend: site.baseurl }}" alt="Gauss Settings" style="float:left; width:33.3%;"/>
  </div>

  I know what you're thinking. Isn't that gorgeous?
* **iCleaner**
  Much like CCleaner for Windows, it cleans log files, temp files, you can deleted unused dictionaries and languages.
* **KeyboardVibrate8**
  This enables haptic feedback just like an Android device. I love it. You can set the duration of each vibrate in the Settings app.
* **LyricForMusic**
  If you tap the album artwork of a song in the Music app, you'll be greeted with the lyrics of the song. If you've added the lyrics to the song with iTunes. Just kidding, this tweak will search the internet for the lyrics, and automatically add them for you. It's worked flawless for me so far, and is one of my favorite tweaks.
* **Mesalation**
  This is another favorite of mine. If you enable Touch ID, your device will require either your fingerprint or your passcode immediately in order to unlock your device. Why this is, I don't know, Mesalation allows you to choose the interval just like you would if you had Touch ID disabled. Without this tweak I refuse to use Touch ID. Period. End of story.
* **NoAppStoreRedirect**
  If you accidentally touch one of those pesky banner ads that opens the App Store, this tweak adds a confirmation dialog. I couldn't live without it.
* **NoRespringChirp**
  This one's an overly complicated gargantuan tweak that tries to be everything you will possibly ever need. Not really, it doesn't even have any settings. All it does is keep your device silent when you reboot or respring it. Yay.
* **OpenSSH**
  Allows you to connect to your device over an SSH connection. Careful, you should change your device's passwords immediately after installation. By default your device's password is `alpine`.
* **Pheromone**
  Cydia always used to run as root. This meant no one could tweak its functionality. No more. Saurik changed this, and now Pheromone adds some nice things to Cydia. It adds a cancel button to the search screen, a nice blur to the installation screen, and adds a brown (because of the icon color) tint throughout the app. It might do more, but I can't remember.
* **SafariAlwaysPrivate**
  This is another complicated one guys, I'm not sure if I'm smart enough to explain it. It forces Safari to open pages in Private mode. Similar to Incognito mode in Chrome. Hmm.
* **StatusTime+**
  Allows you to modify the time in your status bar. I love it. Mostly because it shows the date. Currently, I have my time formatted like this: `Tue 28, 04:19:03 PM`.
* **StatusVol 2**
  This one removes the infernal volume HUD, and makes it more subtle. It slides down from the top of the screen, and temporarily replaces the status bar with the volume.
* **SwipeSelection Pro**
  I can't live without SwipeSelection. It allows you to move your cursor by swiping the keyboard. A simple tweak, but combined with KeyboardVibrate8, it makes me not hate typing on my phone.
* **top**
  Allows you to see your CPU usage. Exactly the same as the `top` command in a Linux terminal.
* **VirtualHome 8**
  This one's subtle, but without it, my phone feels alien and weird. It uses Touch ID to act as a home button. This means you don't have to push the home button, only lightly tap it.
* **WhiteTerminal**
  The most polished terminal emulator I've found. Allows you to access your device's bash shell. You can install a ton of different packages for the terminal. Using `apt-get` doesn't query your "distro's" repos though, it queries the terminal packages available through Cydia. You can install Python, Java, Ruby, various compliers, Git, Vim, zip utilities, etc. A must have for the power user.
* **Zeppelin**
  The only thing I use this for is remove the "Verizon" from my phone's status bar. To me, I know what carrier I'm on, I don't need to know that information. But Zeppelin is far more powerful than that. Zeppelin allows you to replace your carrier name with an image. You can install hundreds of different images with Cydia, but I haven't found one that I like enough to clutter my status bar.

This list forgoes my all time favorite tweak, but it has not updated to iOS 8.4 yet, and I doubt that it ever will. It's name is Forecast, and if you swiped left on your lock screen, it would show a clean polished 5 day forecast, and replace the swipe to unlock text with the current local temperature as well as today's high and low. This was my most used and most liked tweak. Opening the Weather app just seems clunky and slow to me now. You can also buy a tweaks that enable caller ID on your device, send push notifications when you have an orangered, etc.

So I hope you got a good idea of what jailbreaking your device can do. I'm by no means a representative sample of the jailbreak community; there are far more things you can do with a jailbroken device, but I've tweaked my device to my own preferences. It does what I want it to do, and I'm happy with it. You might be too. If you're interested in jailbreaking your device, go check out Reddit's [jailbreak](https://reddit.com/r/jailbreak) community. They have lots of good information in their sidebar. Best of luck!
