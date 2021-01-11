# goldsmiths-search-engine
CLI utility used to search for occurrences of strings across all indexed pages on gold.ac.uk

## Installation

### Clone repo
### Create python virtual environment
### Install dependencies using pip
### Optionally change permissions on scrape.py

## Usage

This is the most basic use of the tool:

    ./scrape.py "search term"
This will crawl every page specified in the hardcoded sitemap, and return a list of matches in the terminal.
## Flags
CLI arguments are defined in parsing_definitions.py, then imported into scrape.py.
Currently available are:

- **-s, --Sitemap (currently broken)**: Lets you specify a different sitemap file
- **-u, --Url-Filters** Lets you specify plaintext patterns to filter sitemap urls by (e.g. /ug/, /pg/, /careers/.) This isn't very sofisticated – it only checks whether the specified strings are present in the url, then parses it if they are.
- **-d, --Debug** Used for debugging. Will print out all arguments you set, without running a search (kind of like a dry run).
- **-v, --Verbose (currently broken)** Used for debugging. Prints out verbose output. Useful for checking what's happening behind the scenes.
- **-po, --printoutput** Prints real-time output to terminal as well as writing it to csv. This replaces the .'s that usually track progress.

## To Do

 ### Sitemap improvements

- [ ] Autoregenerate sitemap if enough time has passed since last search.
- [ ] Add flag to regenerate sitemap before runtime.
- [ ] Allow users to specify custom sitemap path at runtime.
