Source Files for Computational Linguistics Lab Website
======================================================

This is the repository for the website of the [Department of Linguistics'](http://linguistics.stonybrook.edu) research group in Computational Linguistics at [Stony Brook University](http://www.stonybrook.edu).
The Master branch holds the source files, the gh-pages branch is used for the output files.
The source files are simple markdown files that are automatically converted to HTML5 via the Python-based [Pelican](http://docs.getpelican.com/) and then uploaded to Github with [ghp-import](https://github.com/davisp/ghp-import).

The setup is fairly simple in that few plugins and extensions are used.

System Requirements
-------------------

If you're affiliated with Stony Brook University, you can download a [virtual machine image](https://drive.google.com/a/stonybrook.edu/file/d/0B09645QdWLiYUldGSGl5Tmx0Vm8/view?usp=sharing) that comes with all necessary packages pre-installed.

1.  Recent version of Python2.

1.  Pelican 3.6 or higher.
    On a recent Linux installation (2016 or later), this should already be in your repository.
    
    - In Debian Jessie you have to activate the backports repository to get a recent version.
    - In Ubuntu 14.04 (LTS) you'll need to find a ppa or use the Mac/Windows method.
    - On OSX and Windows (and Linux, if necessary) you can install Pelican via Python's package manager pip.

    ~~~~~
    pip install pelican
    ~~~~~

1.  The ghp-import script.
    Again you can install it via pip

    ~~~~~
    pip install ghp-import
    ~~~~~

    or use your package manager if you're on Linux.

1.  A recent-ish version of the `make` tool.
    This is usually already installed on Linux and OSX.
    If it isn't, make sure you have the basic tools for compiling software installed.
    On Debian and Ubuntu, the following should work:

    ~~~~
    sudo aptitutde install build-essential
    ~~~~

    On Windows, install [GnuWin32](http://gnuwin32.sourceforge.net/packages/make.htm) or [MinGW](http://www.mingw.org/).
    The `make` binary also has to be in your PATH, which happens automatically on Linux and OSX but not Windows.

1.  Python's `typogrify` library.
    As before, use pip or your package manager.

1.  Python's `beautifulsoup` library.
    As before, use pip or your package manager.

    ~~~~
    pip install beautifulsoup4
    ~~~~

File Structure
--------------

Once you've cloned the repository, you'll see a couple of files and folders.
The most important ones are:

- *content*: the markdown files for the website
- *output*: the actual website generated by Pelican
- *pelicanconf.py*: contains various settings for site creation;
  for your own site, you'll want to change all the variables at the top, plus `LINKS` and `SOCIAL` further down.
- *publishconf.py*: allows you to override certain settings in the final creation phase;
  for your own site, change at least the value for `SITEURL`.
- *Makefile*: set of instructions for building the website;
  you might want to change the value for `GITHUB_PAGES_BRANCH` depending on your Pelican workflow

Workflow
--------

1.  Add new files to the `content` folder as you see fit.
1.  Run `make devserver` to create a local version of the website.
    You can view it in your browser at the address `localhost:8000`.
1.  If everything looks fine, push the created website to github with `make github`.
    This only pushes the contents of the `output` folder to the `gh-pages` branch.
    See the next step for how to push the source files.
1.  Use `git add` and `git commit` as usual to commit the changes in the `content` folder.
    Then run `git push origin master`.
