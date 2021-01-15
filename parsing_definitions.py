import argparse


def create_parser():
    ## Setup command line arguments
    # Custom Types
    help_message = """Description: This commandline utility searches the entire Goldsmiths website (gold.ac.uk) for occurences of the specificed search term(s)."""
    parser = argparse.ArgumentParser(description=help_message)

    # Arguments
    parser.add_argument(
        dest="searchterms",
        nargs="+",
        help='Specify at least one word or phrase you would like to search for, wrapped in quotes (e.g. "apply through clearing" "clearing applications")',
    )

    # Flags
    parser.add_argument(
        "-s",
        "--sitemap",
        dest="custom_sitemap",
        default="sitemap.csv",
        help="Specify the path to a sitemap file. If left blank defaults to sitemap.csv",
    )

    parser.add_argument(
        "-u",
        "--url-filters",
        dest="url_filters",
        nargs="+",
        help="Specify plaintext patterns to filter search urls by (e.g. /ug/, /pg/, /careers/)",
    )

    parser.add_argument(
        "-d",
        "--debug",
        dest="debug",
        action="store_true",
        help="Used for debugging. Will print out all arguments you set, without running a search (kind of like a dry run).",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        help=f"Used for debugging. Prints out verbose output. Useful for checking what's happening behind the scenes.",
    )

    parser.add_argument(
        "-po",
        "--printoutput",
        dest="print_output",
        action="store_true",
        help=f"Print real-time output to terminal as well as writing to csv. This will replace all the .'s printed otherwise.",
    )

    parser.add_argument(
        "-n",
        "--outputname",
        dest="output_name",
        nargs="+",
        help=f"Give a custom filename for the results csv (wrapped in quotes.) The .csv file extension is added automatically.",
    )
    return parser
