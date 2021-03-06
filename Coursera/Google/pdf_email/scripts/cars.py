#!/usr/bin/env python3

import json
import locale
import sys
import operator
import reports
import emails


def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def format_car(car):
    """Given a car dictionary, returns a nicely formatted name."""
    return "{} {} ({})".format(
        car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
    """Analyzes the data, looking for maximums.

    Returns a list of lines that summarize the information.
    """
    locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
    max_revenue = {"revenue": 0}
    max_sales = {"sales": 0}
    date_min = 2020
    date_max = 0
    year_calculation = {}

    for item in data:
        # Calculate the revenue generated by this model (price * total_sales)
        # We need to convert the price from "$1234.56" to 1234.56
        item_price = locale.atof(item["price"].strip("$"))
        item_revenue = item["total_sales"] * item_price
        if item_revenue > max_revenue["revenue"]:
            item["revenue"] = item_revenue
            max_revenue = item

        # TODO: also handle max sales
        if item["total_sales"] > max_sales["sales"]:
            item["sales"] = item["total_sales"]
            max_sales = item

        # TODO: also handle most popular car_year
        # Calculate the min date :
        if item["car"]["car_year"] < date_min:
            date_min = item["car"]["car_year"]
            # Calculate the max date :
        if item["car"]["car_year"] > date_max:
            date_max = item["car"]["car_year"]

    i = date_min
    while i <= date_max:
        year_calculation[i] = 0
        i += 1

    for item in data:
        for keys in year_calculation.keys():
            if item["car"]["car_year"] == keys:
                year_calculation[keys] += item["total_sales"]

    # we find the best year and sales summary :
    year = max(year_calculation.items(), key=operator.itemgetter(1))[0]
    nb_of_sales = year_calculation[year]

    summary = [
        "The {} generated the most revenue: ${}".format(
            format_car(max_revenue["car"]), max_revenue["revenue"]),
        "The {} had the most sales: {}".format(
            format_car(max_sales["car"]), max_sales["sales"]),
        "The most popular year was {} with {} sales.".format(year, nb_of_sales)
    ]

    return summary


def cars_dict_to_table(car_data):
    """Turns the data in car_data into a list of lists."""
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for item in car_data:
        table_data.append([item["id"], format_car(item["car"]), item["price"],
                           item["total_sales"]])
    return table_data


def main(argv):
    """Process the JSON data and generate a full report out of it."""
    data = load_data("car_sales.json")
    summary = process_data(data)
    # TODO: turn this into a PDF report
    # we'll transform the list into a string ans add <br/> :
    str_summarybr = ""
    str_summaryn = ""
    for elem in summary:
        str_summarybr += elem+"<br/>"
        str_summaryn += elem+"\n"

    reports.generate("cars.pdf", "Sales summary for last month",
                     str_summarybr, cars_dict_to_table(data))
    # TODO: send the PDF report as an email attachment
    sender = "automation@example.com"
    recipient = "pjourdan35@example.com"
    subject = "Sales summary for last month"
    body = str_summaryn
    attachment_path = "cars.pdf"
    emails.send(emails.generate(sender, recipient,
                                subject, body, attachment_path))


if __name__ == "__main__":
    main(sys.argv)
