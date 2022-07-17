import argparse
import os
import src.tools
import src.manager


class Starter():
    def __init__(self):

        logger = src.tools.ServicesClass.get_logger()
        try:
            parser = argparse.ArgumentParser()
            parser.add_argument(
                "--incorrect-emails",
                "-ic",
                help="Print the number of invalid emails, then one invalid email per line.",
                action=argparse.BooleanOptionalAction,
                default=False)
            parser.add_argument(
                "--search",
                "-s",
                type=str,
                help="The Program should take a string argument and print the number of found emails, then one found email per line.")
            parser.add_argument(
                "--group-by-domain",
                "-gbd",
                help="Group emails by one domain and order domains and emails alphabetically",
                action=argparse.BooleanOptionalAction,
                default=False)
            parser.add_argument(
                "--find-emails-not-in-logs",
                "-f",
                type=str,
                help="Find emails that are not in the provided logs file. Print the numbers of found emails, then one found email per line sorted alphabetically.")

            args = parser.parse_args()
            run = src.manager.Manager()
            run.manage(args)
        except SystemExit as error:
            logger.log_message("Argument -s or -f need path to log file", 3)

    def dir_path(self, string):
        if os.path.isdir(string):
            return string
        else:
            raise NotADirectoryError(string)


if __name__ == "__main__":
    start = Starter()
