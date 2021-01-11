# goldsmiths-search-engine
CLI utility used to search for occurrences of strings across all indexed pages on gold.ac.uk

## Installation

### Clone repo

Clone this repo into your porject directory.

    git clone https://github.com/antoni-devlin/goldsmiths-search-engine.git

### Create python virtual environment

cd into the project directory, and create a python virtual environment. Below is a simple example, but do it however you like.

    cd goldsmiths-search-engine
    python3 -m venv venv

Activate the venv

    source venv/bin/activate

### Install dependencies using pip

    pip install -r requirements.txt

### Optionally change permissions on scrape.py

If you would like to be able to run the script using

    ./scrape.py

instead of

    python scrape.py

you'll need to make the script executable

    chmod +x scrape.py

## Usage

All commands need to be run from within the project directory. This is the most basic use of the tool:

    ./scrape.py "search term"

This will crawl every page specified in the hardcoded sitemap, and write a list of  a list of matches in the terminal.
## Flags
CLI arguments are defined in parsing_definitions.py, then imported into scrape.py.
Currently available are:

- **-u, --Url-Filters** Lets you specify plaintext patterns to filter sitemap urls by (e.g. /ug/, /pg/, /careers/.) This isn't very sofisticated – it only checks whether the specified strings are present in the url, then parses it if they are.
- **-d, --Debug** Used for debugging. Will print out all arguments you set, without running a search (kind of like a dry run).
- **-po, --printoutput** Prints real-time output to terminal as well as writing it to csv. This replaces the .'s that usually track progress.
- **-n, --outputname** Give a custom filename for the results csv (wrapped in quotes.) The .csv file extension is added automatically.

## To Do

- [ ] Autoregenerate sitemap if enough time has passed since last search.
- [ ] Add flag to regenerate sitemap before runtime.
- [ ] Allow users to specify custom sitemap path at runtime.
- [x] Add writing results to csv automatically.
