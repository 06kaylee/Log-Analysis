#!/usr/bin/env python3
import sys
import re
import operator
import csv

log_file = sys.argv[1]

# error message: # of times it occurred
error = {}
# username: #info, #error
per_user = {}

with open(log_file) as f:
    regex_info = r"ticky:\s+INFO\s+([^([)]+)\s+"
    regex_error = r"ticky:\s+ERROR\s+([^([)]+)\s+"
    regex_user = r"\(([^)]+)\)"

    for line in f:
        result_info = re.search(regex_info, line)
        result_error = re.search(regex_error, line)
        result_user = re.search(regex_user, line)

        if result_user != None:
            user = result_user.group(1)
            per_user[user] = per_user.get(user, [0, 0])

            if result_info != None:
                per_user[user][0] += 1

            elif result_error != None:
                error_message = result_error.group(1)
                error[error_message] = error.get(error_message, 0) + 1
                per_user[user][1] += 1

# the most frequent error is first
error = sorted(error.items(), key = operator.itemgetter(1), reverse = True)

# insert headers at the 0th position
error.insert(0, ("Error", "Count"))

# sort users alphabetically
per_user = sorted(per_user.items())

# insert headers at the 0th position
per_user.insert(0, ("Username", "INFO", "ERROR"))


with open("error_messages.csv", "a+") as f:
    writer = csv.writer(f)
    writer.writerows(error)

with open("user_statistics.csv", "a+") as f:
    writer = csv.writer(f)
    for item in per_user:
        if isinstance(item[1], list):
            row = (item[0], item[1][0], item[1][1])
        else:
            row = (item[0], item[1], item[2])
        writer.writerow(row)

