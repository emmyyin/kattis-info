# kattis-info

This script can be used to get your Kattis score and ranking from the command line. As of now only login through a Google-account is possible.

## How to use
#### Set up
This program uses

- `Python 2.6, 2.7 or 3.3+`
- `Selenium`
- `Chromedriver`

More information about Selenium can be found [HERE](https://selenium-python.readthedocs.io/installation.html) and about Chromedriver [HERE](https://sites.google.com/a/chromium.org/chromedriver/downloads). This needs to be installed in order to run the program.

#### Run program
Clone and navigate to repo from the command line and run:

``python3 kattis-scraper.py``

You will be prompted to enter your google-account credentials. After correct input your Kattis score and ranking will be printed.


## TODO
#### Future features
- [ ] Add error handling
- [ ] Ability to choose how to login
- [ ] Get all solved problems
