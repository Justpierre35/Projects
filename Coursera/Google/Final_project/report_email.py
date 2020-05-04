#!/usr/bin/env python3
import emails
import os
import datetime
import reports

directory_file = "supplier-data/descriptions/"
dict_files = {}
summary = []


def list_files():
    for name_file in os.listdir(directory_file):
        if name_file.endswith(".txt"):
            with open(directory_file+name_file, "r") as file:
                file_reading = file.read().split("\n")
                dict_file = {}

                dict_file["name"] = file_reading[0]
                dict_file["weight"] = int(file_reading[1].strip("lbs"))
                dict_file["description"] = file_reading[2]
                dict_file["image_name"] = name_file.replace(".txt", ".jpeg")
                dict_files[name_file] = dict_file
                summary.append("name: {}".format(file_reading[0]))
                summary.append("weight: {}".format(file_reading[1]))
                summary.append(" ")
    return summary


def main():
    summury = list_files()
    str_summarybr = ""
    for elem in summary:
        str_summarybr += elem+"<br/>"
    date_sent = "Processed Update on "+datetime.date.today().strftime("%B %d, %Y")
    reports.generate_report("/tmp/processed.pdf", date_sent, str_summarybr)
    sender = "automation@example.com"
    recipient = "student-00-856d18cffaf1@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = "/tmp/processed.pdf"
    emailgen = emails.generate_email(sender, recipient, subject,
                                     body, attachment_path)
    emails.send_email(emailgen)


if __name__ == "__main__":
    main()
