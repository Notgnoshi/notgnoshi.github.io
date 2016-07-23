---
layout: post
title: How I set up Github User Pages
meta: A description of how I set up my GitHub User page using Jekyll
---

I want to give a short and very non-comprehensive tutorial on how I set up my blog. I started with [this](http://24ways.org/2013/get-started-with-github-pages/) tutorial from Anna Debenham. I found it to be quite informative and well-written. However, I did do quite a few things different than Anna; I'm using a User page and not a Project page, and I used slightly different `_includes/` and `_layouts/` (more on that in a bit). [Here's](https://github.com/Notgnoshi/notgnoshi.github.io) a link to the repository my code lives in. Feel free to take a look so you can see how it all fits together. Note though that I'm not a professional, and if you find an example online that differs it might be worth trying that instead.

I want to give a tutorial for people with my own experience level, or slightly lower. This is *not* a tutorial for people experienced with Git, Ruby, Linux, or web development in general. If you want more information in better detail, the Jekyll [documentation](http://jekyllrb.com/docs/home/) is probably for you. I've linked quite a few different tutorials, but most of them go into more detail than what we need, so keep that in mind.
Let's get started.

* **Install Git**.
  On a Linux system, this is a piece of cake. However, if you're like me, you find tutorials that include things like `sudo apt-get install git` as the only explanation for installing a software package rather frustrating because you're new to ideas such as programming, package dependencies, the command line, and other assorted flavors of witchcraft and sorcery.
  - **On Linux:**
  First things first, we need to open up a terminal. If you know how to do that, you're probably way ahead of me and have `sudo apt-get install` all typed out and ready to go. If not, there's a few ways to open up the terminal, but the easiest is to use the `ctrl+alt+t` keyboard shortcut. After you have the terminal open, simply use the `sudo apt-get install git` command to install, and input the administrator password when prompted. Note that you will be unable to see any characters you type when you input the password so be careful!
  - **On Windows:**
  Windows is a different beast entirely. You can't do a whole lot from the command line, so we have to download and run an installer. [Here's](http://git-scm.com/download/win) a direct download link. It's been a while since I've last used Windows, and even longer since I've installed Git in a Windows environment, but if my memory serves me correctly, you should just be able to accept all the default options from the installation wizard. I don't want to lead you astray, so if you have questions on what to do after downloading the installer, you should check [here](http://code.tutsplus.com/tutorials/git-on-windows-for-newbs--net-25847) for a nice tutorial on how to use the Git for Windows GUI client, and [here](http://guides.beanstalkapp.com/version-control/git-on-windows.html#installing-git) for a nice tutorial on how to install and use Git Bash. Because I'm using Ubuntu and I've never used the GUI version, in this tutorial I'll be sticking with Git Bash, so that's what I recommend installing and learning how to use.
  - **On Mac OS:**
  My apologies, I've never used a Mac, and have no clue how their software installation works, so all I can do is tell you to read the Mac portion of [this](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) guide.

  Yay. If all has gone the way it was supposed to, you now have Git installed on your device. We'll install Jekyll, then look at how to put this all together.

* **Install Jekyll**.
  Time for some more software installation goodness. Just to make sure my bias shows I'll mention that installing Jekyll is a piece of cake on Ubuntu or other Linux flavored systems. Ha! Now that that's out of the way let's get to work.
  - **On Linux:**
  We could use `sudo gem install jekyll`, but I ran into problems trying this. About a week later I found out this was because I did not have `ruby-dev` installed. If you wanted to, you could install with `gem`, but don't use both `apt-get` *and* `gem` as bad things can happen. The easiest way to install Jekyll on Linux in my opinion would be to simply use `sudo apt-get install jekyll` just like we did for Git above.
  - **On Windows:**
  Oh boy, you're a glutton for punishment (I'm biased, remember?) According to the Jekyll [website](http://jekyllrb.com/docs/windows/) Jekyll isn't officially supported on Windows. However it's still possible to use it if you follow [this](http://jekyll-windows.juthilo.com/) guide. You'll have to install Ruby as well.
  - **On Mac:**
  Supposedly all you have to do is run `gem install jekyll` from the terminal. I've not verified this. The only mention the Jekyll website makes of Mac OS X is that there's a possibility you might need to install Xcode and the Command-Line Tools it ships with. [Here's](http://internet-inspired.com/wrote/install-jekyll-in-osx-mavericks/) a tutorial that seems pretty good for you Mac people.

* **In this tutorial we're going to be making a *user* page, not a *project* page.** This is a small difference that only has to do with the Github repository name and what repository branch you decide to host your content on.

* **Create, then clone your repository.**
  - The very first thing we're going to do after we've installed our shiny new software is to create a new GitHub repository for our site to live on. [Here's](https://github.com/new) a convenient link to GitHub's "create a new repository" page. If you don't have a GitHub account you need to make one before you can continue.
  - Since we're going to be creating a user page, you must name the repository `"your GitHub username here".github.io` (without the quotes!)
  - Decide where you want to have your copy of your new blog's content to live on your computer. I recommend a folder on your desktop to experiment with because it'll be easy to delete once you're done figuring things out, then you can put it somewhere more organized later when you're ready to make the real deal. Or you could put it wherever you want because it's your computer and not mine. I put mine in `~/Documents/Blog/` (I'm using Linux, so the `~` symbol means my user's home directory, which is analogous to `C:/users/user_name/`.) If you're using the command line for this part, you can `cd` into whatever directory you want, then use the `mkdir` command to create a folder for your blog to live in.
  - This is an excellent opportunity to familiarize yourself with the terminal if you have never used it before.
  - From here on you should have a terminal open. If you're using Windows, Command Prompt is ***not*** what you want for this. There might be a way to get it or Powershell to work, but that's not within the scope of this tutorial. You should be using Git Bash if you're on a Windows computer, and the normal terminal if you're using anything else. If you right click in your Windows file browser there should be a context menu option that says `Open Git Bash Here`. It's far easier to click that than it is to `cd` to where you want your blog content saved, especially if some of your folder names contain spaces.
  - If you navigate to your repository page at [GitHub.com](https://github.com) there's a small text field in the lower right hand corner. It says "HTTPS clone URL." Click the little clipboard symbol to copy the URL to your clipboard.
  ![Clone URL]({{ "/assets/posts/gh-pages/clone-url.png" | prepend: site.baseurl }})
  Assuming you've managed to `cd` into the proper directory from the command line, type in `git clone ` then paste the clone URL by pressing `shift+insert` then press enter. For my repository my command looks like this: `git clone https://github.com/Notgnoshi/notgnoshi.github.io.git`. Awesome. There's now a folder named `notgnoshi.github.io` in my `~/Documents/Blog/` folder.
  - Everything we do from here on will be inside this new folder. So `cd` into it. For me the command is `cd notgnoshi.github.io`. Some terminals have tab-complete functionality, so once you start typing out `notg` you can press tab. I know, I know, I'm lazy.
  - This folder should be empty. Use the `ls` command to make sure. If you're on Windows, you'll be able to see a folder named `.git`. You can ignore this folder, but don't delete it! If the folder is *not* empty our next step will fail. There shouldn't be anything in the folder unless you followed GitHub's suggestion to initialize your repository with a `.gitignore` file and a `README.md` file. I would recommend moving these so you can keep them, especially the `.gitignore` file as we're going to use that later.


* **Initialize your Jekyll site in your repository folder.**
  - Assuming you've successfully installed Jekyll, all we have to do is run `jekyll new .` If it was successful, the terminal should now say something like: `New jekyll site installed in /home/Nots/Documents/Blog/notgnoshi.github.io.`
  - Yay. We now have a blog, but it only lives on our computer, and not out on the internet. We can get our blog running from our own computer with a little bit of port-forwarding and domain name registration, but that defeats the purpose of using GitHub Pages. So now we're going to 'push' our new blog out onto GitHub's servers.


* **Commit and Push**
  Here's all the fun Git stuff that people new to the command line environment are terrified of. At this point you should still have your terminal open to your blog directory. It's important to note that Git and GitHub are two different things. Git is a commandline tool for dealing with version control. GitHub is a company who's business is hosting other people's code repositories open for everyone to see. There are others that do the same thing, but GitHub is the most popular. This is a gross oversimplification, but for our purposes it works.
  - The first thing we're going to do is run the command `git status`. The very first time you run this, you'll see a bunch of red text mentioning a lot of different things. This is because running the `jekyll new .` command *generated* quite a few different files and folders, but the Git repository doesn't know what to do with them yet. That's okay.
  - The next thing we're going to do is run the command `git add --all`. If you wanted to, you could add each individual folder and file one at a time, but again, I'm lazy. This tells Git that these are the files we're interested in, and that it should only pay attention to changes we make in these files only.
  - After we finish adding the files and folders to our repository, we need to *commit* our changes. In other words, after we tell Git to pay attention to a file, we can to commit our changes to that file once we're done with it. The command for this is `git commit -m "put some message here that explains the changes you made in quotes."`
  - Great, we've told Git to pay attention to our files, and we've told it that we're done making changes, but when we try to look at `"your username here".github.io` in the browser we get nothing. This is because we haven't told Git that the changes we've made are ready for everyone to see. We haven't *pushed* them to the public. The command for this is `git push origin master`. Git will prompt you for your GitHub username and password. As when you used `sudo apt-get`, you won't be able to see your password as you type it in, so be careful when you type it.
  - If you don't get any error messages you should be able to navigate to `"your username here".github.io` in your web browser, and after a while you should be able to see the Jekyll demo blog. Awesome.
  - Here's a video of me doing the previous steps:

    <script type="text/javascript" src="https://asciinema.org/a/24367.js" id="asciicast-24367" async></script>


* **.gitignore, README.md, and licensing**
  - I mentioned `.gitignore` a little before. It would have been easier for me to tell you want to do before now, but I think you might have a little bit of understanding of what's going on now. If you add a filename to `.gitignore` it tells Git to ignore that file. Real creative, right? You can do the same for folders. This is nice, because there are a few files and folders that are in our blog directory that are only useful to us, and not the public. One of these folders is the `_drafts/` folder, which I'll get to later in a little more detail. I don't really want the public to be able to read my drafts before I decide I'm done with them, so I added `_drafts/` to my `.gitignore`. I can do this by opening up `.gitignore` in my favorite text editor (Sublime Text 3 or Atom) and adding the line `_drafts/` to the file, with no extra spaces, quotes, or anything else. I also added `_site/` to `.gitignore` too because while `_site/` is what actually contains the generated version of our blog, GitHub Pages will generated it itself so it gets the most secure and recent version. Although, for more advanced users, if `_site` is the only thing in your Git repository, GitHub Pages will use that to render your site, so if there's a plugin that changes the functionality of your site, and all it does is change the static page generation, you can use this to get around the fact that GitHub Pages doesn't support many Jekyll plugins. So while we can browse through `_site/` for our own curiosity, we can really just ignore it.
  - However, this doesn't remove them from the GitHub repository if they were already present. We use the `git rm -r "put folder name here"` command for folders, and the `git rm "put filename here"` command to remove files, both without quotes. This will delete the folders and files from your Git repository, but it will also delete them from your computer. If you don't want that, move the files or folders before you run the commands, then move them back. Now we're going to commit and push our changes using exactly the same commands as before. I like to run `git status` before I do anything just so I know exactly what it is I'm committing and pushing, but if you don't want to, you don't have to. It's easiest, as I said earlier, to just use the `git add --all` command to add all changed files to the git repository, and then `git commit -m "message here"` (with quotes) before finally pushing our changes with `git push origin master`.
  - If you've ever looked through a GitHub repository before, you might have noticed that below all the files listed there's often a little bit of text explaining the repository, and often how to use it. That's what `README.md` does. We don't really need it for our blog, but you can add it if you'd like.
  - If you plan on blogging in a more professional manner, or if you blog contains what you consider to be your intellectual property, you probably want to license it. I'm new to programming, and I'm even newer to Git, GitHub, and licensing, so I'm not going to lead you astray by telling you what to do here, instead you should research what, if any, license is best for you.


* **We now have a demo blog, let's make it our own!**
  The rest of the tutorial will be about how to configure and add content to our shiny new blog.

* **_config.yml**
  Let's go through some of the configuration options before we get to our site layout and how to add content.
  - When you ran `jekyll new .` it created your site, and it created some default config options for us. In `_config.yml` we see options like `title`, `email`, `description`, and some others. Some of these, like the various usernames, title, and description you can go ahead and fill right in.
  - I removed the `url` and `baseurl` lines. I had a few issues with layout, and while I'm pretty sure it was entirely my fault and not Jekyll's, removing those two lines fixed it. If you decide to host your blog on your own custom domain name instead of the one GitHub provides for you by default you're going to have to update the `url`  and `baseurl` options to reflect that.
  - I left the `markdown` and `permalink` options just the way Jekyll created them, I'm not quite sure what they do, but the way I understand it, to use some of the fancier LaTeX math typesetting I must use kramdown.
  - I added the lines

  - ```yaml
  kramdown:
      input: GFM
  ```
  to my `_config.yml`. This tells Jekyll to use GitHub's flavor of markdown rendering. Which means that you can use [this](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) guide to help you format your posts.
  - There are two other things I added in order to get Google Analytics to work, but I'll get to those later.


* **Markdown, HTML, and CSS Resources:**
  To understand the rest of the tutorial you're going to need to be familiar with at least basic HTML. If you'd like, you can be lazy like me and leave the default CSS the way it is. Anyways, if you don't feel you're up to snuff with HTML, here are some links that can help you either refresh or learn it for the first time.
  - [Codecademy](http://www.codecademy.com/en/tracks/web) is an excellent introduction to basic topics for the beginner.
  - [w3schools](http://www.w3schools.com/html/) is an excellent resource for beginning and intermediate skill levels.
  - You might check your local community college for web development courses, but this can be expensive depending on the school.


* **`_includes/` and `_layouts/`.**
  Now we're at the *really* fun part. We get to start deciding how we want our site to look and function. I opted to leave much of my blog the way Jekyll generated it, but absolutely feel free to mess around with these and look up more detailed tutorials on all the really neat things you can do with these. After you've made some changes, take a look at the writing process part below to see how to apply these changes and see them before you push them live to your new blog.
  - Wouldn't it be nice if all we had to do to write a blog post was simply write the content and not worry about all the code required to make it look nice? The HTML snippets in `_layouts/` define the basic structure of every page in our blog. Jekyll uses this information when it generates the static site when we view our web page, so what happens is, when you write a post, Jekyll takes your post content, and structures it like whatever you've put in `_layouts/`!
  - Let's take a closer look. Most HTML documents follow the same basic structure:

    ```html
    <!DOCTYPE html>
    <html>
    <head>
    <!-- Stuff that tells the browser about your page goes here. -->
    <!-- No content goes in the head. -->
    </head>

    <body>
      <header>
      <!-- This is where your navigation bar and website logo go. -->
      <!-- Note that a header is NOT the same as the head -->
      </header>

      <div>
      <!-- Page content goes in here -->
      </div>

      <footer>
      <!--This is where we put our twitter and github usernames, as well
          as anything else we want at the bottom of every page. -->
      </footer>
    </body>
    </html>
    ```
  - What `_layouts/` allows us to do is define this HTML structure in detail for every type of page we expect to have on our blog. On my blog those types would be a post, and a kind of generic page. However, I'm lazy and even posts and generic pages share a lot of code, so I make a default layout that every single page will be guaranteed to have, then we can say that each page and each post will use the default layout. The default layouts that Jekyll generated for us are pretty good, so I didn't change mine that I can remember. There are a lot of blogs and tutorials out there that can show you how to modify these if you're interested.
  - If you've tried to set up a blog before using just HTML and CSS, you've probably run into the fact that often there are times where you use the same snippet of code on *every. single. page.* Wouldn't it be nice if we could write these snippets once, then, oh I don't know, *include* them on each page? That's exactly what `_includes/` does for us!
  - I have four different snippets of HTML in my `_includes`. I have the footer, the header, the head, and some code that allows me to use Google Analytics to see if anyone actually reads this. I left the footer pretty much the same as Jekyll generated it, except I moved the order of the columns around with copy/paste.
  - In `_includes/footer.html` do you see where it says `{% raw %}{{site.description}}{% endraw %}`? That's the description you set in `_config.yml`! Using curly braces like this is how we'll include data from one place in lots of others.
  - The only change I made to `_includes/head.html` was that I included a script to enable some fancy math typesetting. If you're interested you can read more about that later.
  - If we look at `_layouts/default.html` we see how to include these snippets in our pages. All we do is add `{% raw %}{% include filename-we-want-to-include.html %} {% endraw %}`.


* **Let's go through a few pages.**
  We've seen a little bit about how Jekyll works, but now it's time to get on to actually customizing it and making it *our* site. Let's take a look at three different pages: `index.html`, `about.md`, and an example post. `index.html` is our homepage, it's the one we see when we visit [notgnoshi.githib.io](http://notgnoshi.github.io). `about.md` is where the reader can read about the author and the blog; it's responsible for the [About](http://notgnoshi.github.com/about/) link at the top of the page. And then I think you know what an post will do; it's what you've been itching to get at this whole time!
  - **Let's look at the simplest page `index.html`.**
  This page, as I've mentioned, is our 'home' page, the page that first loads when we open up our site. Many blogs have the most recent post as their home page, but I've decided to leave mine the way Jekyll first generated it with a list of posts on my home page. Let's take a look and see how it ticks!
  - The first thing we notice is the lines at the top encapsulated in `---`.

  - ```yaml
  layout: default
  title: posts
  ```

    The `layout:` part defines what layout we want to use for the page, and the `title:` part in this case defines the text that shows up in your browser tab.
  - The next part we see is `<div class="home">`, this tells Jekyll some information on how to style the page. For our purposes we can leave this the way it is and move on.
  - Next up is `<h1 style="margin-bottom:0; font-size:20pt">Posts</h1>`. This is our page heading. Instead of screwing around with the CSS in `css/main.css` I opted to do some inline styling because it will only ever be implemented once.
  - Next we have an unordered list (`<ul class="posts"></ul>`) of posts. Jekyll supports some control flow statements like `for post in site.posts` that allow us to make a list of posts on our site without knowing their title or how many there are. This is powerful. For each `post` in `site.posts` we're going to make a list item that has the `post.date` specially formated appear right before the link to each post. Each link has the url of `post.url` and the link text of `post.title`. We could talk about Object Oriented Programming and what's going on when we have `post."something here"`, but simplistically what's happening is that `site.posts` is a list of posts, and each post has three properties, `date`, `url`, and `title` which we access with `post.property`. We then close the `for` loop with `endfor` (real creative, I know) and then close out our list with `</ul>`.
  - The only thing left is a paragraph tag that has an RSS link in it. You can remove this if you'd like, but I left mine alone.
  - **Now let's look at `about.md`.**
  This is a *markdown* file, hence the `.md` file extension. Markdown is a text file format that allows simple text to be rendered fancily in a browser. Markdown lets us worry about our content rather than specifically how to make our post look fancy. Jekyll will allow us to use either `.html` or `.md` files for our posts and pages. It's up to you, but I find markdown simpler and easier to use.
  - Just like `index.html` we find that `about.md` begins with a small block of text wrapped in `---` at the top of the file. It turns out that all Jekyll pages have this, and it's called "Front-Matter". We specify our page layout, our page title, and oooh, what's this? a permalink for our file that will be displayed at the top of every page on our site.
  - After the Front-Matter we find a blank line and then a bunch of text. The purpose of an 'About' page is to tell your readers about yourself, so get to writing!
  - **Let's look at an example blog post.**
  At the top of the page I gave you a link to the GitHub repository my blog's content lives. [Here](https://github.com/Notgnoshi/notgnoshi.github.io) it is again. Our posts live in the `_posts/` directory, so open up my `_posts/` directory and select a post at random. On GitHub, markdown files are rendered, so you'll have to select the 'raw' button at the top of the file content. You'll notice they're all named with a date and then the post name, more on that later.
  - The first thing we see, as always, is our page's Front-Matter. Depending on the post you picked at random, you could see a few different things. The most basic requirements is a layout and a title. This title can be different that what you named your file. Your filename determines what your post URL will be, and the `title:` in the Front-Matter will tell Jekyll what our post's title is if it's different than our filename. You can put several other things in your page's Front-Matter. [Here's](http://jekyllrb.com/docs/frontmatter/) a link to a description of what you can put up there.
  - As with `about.md` we now get a blank line and then our post's content. [Here's](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) a nice cheat sheet to help you with how to format your posts using GitHub Flavored markdown. You can also mix in some HTML in your markdown file if there's something you need that for.

* **The writing process:**
  - Every time you make a change, you have to follow the same Git commands as above in order to see your changes live on your website. Wouldn't it be nice if we were able to see our changes on a local copy of our blog before we push them out to the public? Well see, the guys and gals over at Jekyll are pretty smart and gave us that ability.
  - The command to see a local version of your blog is `jekyll serve --drafts --watch`. Let's break this down so you can understand what's going on a little better. If we just did `jekyll serve` we would still be able to see our site at [http://0.0.0.0:4000](localhost:4000), but every time we make a change we would have to press `ctrl+c` to stop our local server then start it back up again to see the changes we made. I'm too lazy for that. What I really want is for Jekyll to have the ability to *watch* the files, and if I change them, automatically update the blog to show the changes I made. That's exactly what adding `--watch` to the command does.
  - Earlier I mentioned using drafts in order to work on writing a post before you make it public. That's what using the `--drafts` flag does. If we have any markdown or HTML files in our `_drafts/` folder, Jekyll will show us these drafts as if they were posts in our `_posts/` folder.
  - If you're like me, and are constantly running out of room on your monitor to see things (a second monitor is on my wish-list) you can forward port `4000` from your local network to the outside world. That way you can view your blog on a second device (for me it's a chromebook) to view your changes while you work on your posts on your main computer. I'm not going to tell you *how* to port forward because it varies so dramatically from router to router. I consider myself lucky to have a router that's so darned easy to port forward. If that's something you're interested in, there are a lot of different tutorials out there to help you. Once you've managed to forward port `4000` to the outside world, you can Google "what's my ip" to find your external IP address and then put it in your browser addressbar like this: `xxx.xxx.xxx.xxx:4000` and viola!
  - Now that we've written a post and we know it looks all fancy and polished from running it locally, we want to let everyone else see it. To do this, we move our `post.md` file from `_drafts/` into `_posts/`. Now remember what I said about the dates in the post filenames? Yeah. Those. We name our posts `yyyy-mm-dd-title-without-spaces-here.md`.
  - After we've moved our draft to its new home, we commit and push, and anywhere from a few seconds to a few minutes later our new post is live. We follow the process detailed earlier to commit and push:
    1. `git status` if you're interested in what changes we made that we're going to commit.
    2. `git add --all` to add the changes we've made so that we can commit them.
    3. `git commit -m "some message describing the changes we've made here, with quotes"`
    4. `git push origin master` and input our GitHub username and password when prompted.


* **MathJax/LaTeX**
  If we want to have pretty looking math like $$ \int\int\int f(r,\theta,\phi)\,rdrd\theta d\phi $$, we can include MathJax in `_includes/head.html` so we can use inline LaTeX rendering. This isn't quite as powerful as just plain LaTeX because we can't include any packages, but it does allow some powerful math formatting.
  - All we do is include

  - ```html
  <script type="text/javascript"
        src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
  </script>
  ```
  somewhere in `_includes/head.html`.


* **Google Analytics**
  This was one of the more frustrating parts of setting up my blog, but after I got it working is seems quite simple. What we do is include the following in our `_config.yml`, and after a few hours it should take effect.

  ```yaml
  analytics:
      provider: google
      google:
          tracking_id: 'UA-xxxxxxxx-x'
  safe: true
  ```

  where `tracking_id:` is the tracking ID you were given by Google when you set up your Google Analytics account. There are a few other ways to do this if this doesn't seem to work, but I'm by no means an expert. This is just how I got it to work.

So there you have it, a not-so-short basic tutorial on how to install, set up, and run a Jekyll blog using GitHub User Pages. I apologize for the wordiness.  There are lots of things I didn't show, there are lots of things you could add or remove, but I hope this helped. If you have questions, Google is definitely your friend, as are some of the more experienced bloggers out there.
