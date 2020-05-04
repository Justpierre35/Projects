#!/usr/bin/env python3

"""Part II Google coursera final test."""

import re
import sys
import csv
import operator

error = {}
per_user = {}


def convert_to_csv(logfile):
    """Main program to create two CSV files syslog.log."""
    with open(logfile) as logfile_reader:
        for logline in logfile_reader.readlines():
            # Errors research :
            errors = re.search(r"(ERROR) ([\w ']* )", logline)

            # Infos research :
            infos = re.search(r"(INFO)", logline)

            # users research
            user = re.search(r"\(([a-z.]*)\)", logline)

            if user is not None:

                if errors is not None:
                    if errors.group(2) not in error.keys():
                        error.update({errors.group(2): 1})
                    else:
                        error[errors.group(2)] += 1

                if user.group(1) not in per_user.keys():
                    per_user[user.group(1)] = {}
                    per_user[user.group(1)]["INFO"] = 0
                    per_user[user.group(1)]["ERROR"] = 0

                if (errors is not None and errors.group(1) == "ERROR"):
                    if per_user[user.group(1)]["ERROR"] not in per_user.keys():
                        per_user[user.group(1)]["ERROR"] += 1

                if (infos is not None and infos.group(1) == "INFO"):
                    if per_user[user.group(1)]["INFO"] not in per_user.keys():
                        per_user[user.group(1)]["INFO"] += 1

        logfile_reader.close()

    # Write the file error_message with information :
    with open('error_message.csv', 'w', encoding='utf8') as output_file:
        fieldnames = ['Error', 'Count']
        dict_writter = csv.writer(output_file)
        dict_writter.writerow(fieldnames)
        dict_writter.writerows(sorted(error.items(), key=operator.itemgetter(1), reverse=True))

    # Write the file user_statistics with information :
    with open('user_statistics.csv', 'w', encoding='utf8') as output_file:
        fieldnames = ['Username', 'INFO', 'ERROR']
        dict_writter = csv.writer(output_file)
        dict_writter.writerow(fieldnames)
        dict_writter.writerows(sorted(per_user.items(), key=operator.itemgetter(0)))


def main():
    convert_to_csv(sys.argv[1])


if __name__ == "__main__":
    main()
