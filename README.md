# goldsmiths-search-engine
CLI utility used to search for occurrences of strings across all indexed pages on gold.ac.uk

## Installation

### Clone repo

Clone this repo into your project directory.

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

This will crawl every page specified in the hardcoded sitemap, and write a list of a list of matches in the terminal.
## Flags
CLI arguments are defined in parsing_definitions.py, then imported into scrape.py.
Currently available are:

- **-u, --Url-Filters** Lets you specify plaintext patterns to filter sitemap urls by (e.g. /ug/, /pg/, /careers/.) This isn't very sofisticated – it only checks whether the specified strings are present in the url, then parses it if they are. Use with caution.
- **-d, --Debug** Used for debugging. Will print out all arguments you set, without running a search (like a dry run).
- **-po, --printoutput** Prints real-time output to terminal as well as writing it to csv. This replaces the .'s that usually track progress.
- **-n, --outputname** Give a custom filename for the results csv (wrapped in quotes.) The .csv file extension is added automatically.

It's usually better to filter a given CSV file for URLs after running your search than relying on my janky filtering logic. You've been warned!

### Custom sitemap format

A custom sitemap.csv must be in the following format:

    url,
    https://www.domain.com,
    https://www.gold.ac.uk,

It can have more columns than just url to the right, but these aren't parsed by the script. The "url" column header is required.

## To Do

- [ ] Autoregenerate sitemap if enough time has passed since last search.
- [ ] Add flag to regenerate sitemap before execution.
- [ ] Allow users to specify custom sitemap path using command line flag.
- [x] Add writing results to csv automatically.
