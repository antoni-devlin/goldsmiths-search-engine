#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
from multiprocessing.pool import ThreadPool
import csv, time, os
from datetime import datetime
from parsing_definitions import create_parser
from colours import bcolours

# Initialise argument parser
parser = create_parser()

# Parse all arguments into a usable format
args = parser.parse_args()

# Debug loop. Will list arguments and exit while the -d/--Debug flag is used
while args.debug:
    print(
        f"""
Available output colors:
{bcolours.WARNING}Warning!{bcolours.ENDC}
{bcolours.HEADER}Header{bcolours.ENDC}
{bcolours.OKBLUE}Okay (Blue){bcolours.ENDC}
{bcolours.OKGREEN}Okay (Green){bcolours.ENDC}
{bcolours.FAIL}Fail!{bcolours.ENDC}
{bcolours.BOLD}Bold{bcolours.ENDC}
{bcolours.UNDERLINE}Underlined{bcolours.ENDC}
    """
    )
    for arg in vars(args):
        print(arg, getattr(args, arg))
    exit()

sitemap = "sitemap.csv"
urls = []
search_results = []
result_count = 0
search_terms = args.searchterms
awards = [
    "ba",
    "bmus",
    "bsc",
    "undergraduate",
    "foundation",
    "cert",
    "diploma",
    "grad",
    "integrated",
    "llb",
    "ma",
    "cpd",
    "mfa",
    "mmus",
    "mphil",
    "mres",
    "msc",
    "primary",
    "secondary",
    "pgcert",
    "phd",
    "pre",
]


def createSitemap(sitemap_filename):
    with open(sitemap_filename, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # row_count = sum(1 for row in csv_reader)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                pass
                line_count += 1
            urls.append(row["url"])
            line_count += 1
        print(f"Searching across {line_count} pages taken from sitemap.csv.")


if args.custom_sitemap:
    createSitemap(args.custom_sitemap)
    print(f"Using custom sitemap: {args.custom_sitemap}.")
else:
    createSitemap(sitemap)
    print("Using exisiting sitemap.")

if args.negate_search:
    print(
        f"Performing search for pages the {bcolours.WARNING}DO NOT CONTAIN{bcolours.ENDC} the search terms."
    )
else:
    print(
        f"Performing search for pages the {bcolours.OKGREEN}CONTAIN{bcolours.ENDC} the search terms."
    )

# Check if output folder exists. If not, create it.
if not os.path.exists("scraping_output"):
    print("scraping_output folder does not exist. Creating...")
    os.makedirs("scraping_output")


def checkPages(url):
    if args.url_filters:
        for filter in args.url_filters:
            if filter in url:
                page = requests.get(url)

                #'Soupify' the content of the page - parse it using an HTML parser
                soup = BeautifulSoup(page.text, "html.parser")
                content = soup.find(id="maincontent").text.lower()
                section = url.split("/")[3]
                for search_term in search_terms:
                    if search_term in content:
                        if args.print_output:
                            print(
                                f"{bcolours.OKGREEN}{url}, {search_term}, {section}{bcolours.ENDC}"
                            )
                        else:
                            print(
                                f"{bcolours.OKGREEN}. {bcolours.ENDC}",
                                end="",
                                flush=True,
                            )
                        search_results.append([url, search_term, section])
                        result_count += 1
    else:
        # Fetch the content of the url, and store it in a variable called page
        page = requests.get(url)

        #'Soupify' the content of the page - parse it using an HTML parser
        soup = BeautifulSoup(page.text, "html.parser")
        content = soup.find(id="maincontent").text.lower()
        section = url.split("/")[3]
        for search_term in search_terms:
            if search_term in content:
                if args.print_output:
                    print(
                        f"{bcolours.OKGREEN}{url}, {search_term}, {section}{bcolours.ENDC}"
                    )
                else:
                    print(f"{bcolours.OKGREEN}. {bcolours.ENDC}", end="", flush=True)
                search_results.append([url, search_term, section])
                result_count += 1


start_time = datetime.now()

# Run the search (uses multi processing, across as many threads as are specified in "threads".)
threads = 20
pool = ThreadPool(threads)  # However many you wish to run in parallel
for url in urls:
    pool.apply_async(checkPages, (url,))

pool.close()
pool.join()

if args.output_name:
    file_name = f"{args.output_name[0]}.csv"
else:
    file_name = str(int(time.time())) + ".csv"

print(f"Writing results to scraping_output/{file_name}.")
with open(f"scraping_output/{file_name}", mode="a") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",", quotechar='"')
    csv_writer.writerow(["Page", "Search Term", "Section"])

    for result in search_results:
        csv_writer.writerow([result[0], result[1], result[2]])

end_time = datetime.now()
print(f"\nYour search matched {len(search_results)} page on gold.ac.uk.")
print(f"Threads: {threads}")
runtime = end_time - start_time
print(f"Runtime: {str(runtime).split('.')[0]}")
