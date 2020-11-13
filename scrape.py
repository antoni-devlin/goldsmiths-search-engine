#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
from multiprocessing.pool import ThreadPool
import csv, time
from datetime import datetime
from parsing_definitions import create_parser
from colours import bcolours

#Initialise argument parser
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
        print(f"Processed {line_count} lines.")


createSitemap(sitemap)


def checkPages(url):
    if args.url_filters:
        for filter in args.url_filters:
            if filter in url:
                # url_split = url.split("/")[4].split("-")[0] + "-"
                # for award in awards:
                    # if f"{award}-" == url_split:
                # Fetch the content of the url, and store it in a variable called page
                page = requests.get(url)

                #'Soupify' the content of the page - parse it using an HTML parser
                soup = BeautifulSoup(page.text, "html.parser")
                content = soup.find("article").text.lower()
                section = url.split("/")[3]
                for search_term in search_terms:
                    if search_term in content:
                        # print(url.strip() + "," + "santander" + "," + section)
                        print(f"{url}, {search_term}, {section}")
                        writeTxt(url, search_terms, section)
                        search_results.append(url)
                        result_count += 1
    else:
        # Fetch the content of the url, and store it in a variable called page
        page = requests.get(url)

        #'Soupify' the content of the page - parse it using an HTML parser
        soup = BeautifulSoup(page.text, "html.parser")
        content = soup.find("article").text.lower()
        section = url.split("/")[3]
        for search_term in search_terms:
            if search_term in content:
                # print(url.strip() + "," + "santander" + "," + section)
                print(f"{url}, {search_term}, {section}")
                writeTxt(url, search_terms, section)
                search_results.append(url)
                result_count += 1


start_time = datetime.now()

# Run the search (uses multi processing, across as many threads as are specified in "threads".)
threads = 20
pool = ThreadPool(threads)  # However many you wish to run in parallel
print("Page, Search terms, Section")
for url in urls:
    pool.apply_async(checkPages, (url,))

pool.close()
pool.join()

end_time = datetime.now()
print(f"Threads: {threads}")
print(f"Runtime: {end_time - start_time}")
