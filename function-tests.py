def filterSearch(url):
    if args.url_filters:
        for filter in args.url_filters:
            if filter in url:
                return True

def negateSearch():
    pass


def checkPages(url):
    page = requests.get(url)

    #'Soupify' the content of the page - parse it using an HTML parser
    soup = BeautifulSoup(page.text, "html.parser")
    content = soup.find(id="maincontent").text.lower()
    section = url.split("/")[3]
    if filterSearch(url)
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
