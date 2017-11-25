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

1.  A recent version of `pandoc-citeproc` (1.17 or newer) if you want to use the bibtex converter.
    

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

In addition, the *bib* folder contains a number of shell scripts (fully sh-compatible), and a subfolder with specific info on each bibtex entry.


Shell Scripts
-------------

All the shell scripts use mostly standard commands such as `cat`, `grep`, `sed`, and `awk`, and they do not use any bashisms.
The one exception is `bib2mdown`, which uses `pandoc-citeproc` to convert the bibtex file into a markdown file using the style sheet *mylanguage.cls*.
Since `bib2mdown` is called in one way or another by every other script, you absolutely need to have pandoc installed.

Here's a description of each script:

1. `bib2mdown` takes a bibtex file as input and returns a markdown file.
   The output produced by pandoc is pretty bad, so a major dose of sed magic is applied after the initial pandoc-conversion step.
   The following tweaks are applied:

     - add doi links
     - rip out all other links since doi is more reliable 
     - add link to pdf, if it exists
     - add link to detailed blog entry
     - list can be bulleted, numbered, or reverse numbered
     - remove remnants of Latex commands
     - fix some formatting errors

1. `bib2blog` produces a blog entry for a given entry in a bibtex file (with the help of `bib2mdown`).
   It automatically assigns it the right category (books, talks, or papers) and saves it to the corresponding subfolder (*talks* for talks, and *papers* for books and papers).
   It also checks whether there is a folder with the same bibkey in `auxfiles`, and loads the abstract, tags, and date from the files in this folder, if it exists.
   It also looks for an archive with the source code in `doc/talks` or `doc/papers` and adds the corresponding link.
   All of that is then put together into a nice entry

1. `create_bibliography` takes two bibtex files as input, one for publications and one for presentations.
   It then uses `bib2mdown` to produce the Output page of the website.

1. `create_bibkey` runs `bib2blog` for every bibtex key in a bibtex file.

1. `compile_references` runs `create_bibliography` and `create_bibkey` on my bibtex files.
   If everything is configured correctly, this is the only script that needs to be run, all others will be called as needed.

All scripts except `compile_references` take command line arguments and can be altered via various options.
Just run them with ``--help`` to learn more.
You can also change the variables at the top of each script to adapt it to your use case.
