#!/usr/bin/env python3
import emails
import os
import psutil
import socket
import time

no_issues = True


def check_cpu():
    info_cpu = psutil.cpu_percent(interval=1)
    if info_cpu > 80:
        no_issues = False
        info_error = "Error - CPU usage is over 80%"
        return info_error


def check_space():
    info_disk = psutil.disk_usage("/")
    if info_disk.percent > 80:
        no_issues = False
        info_error = "Error - Available disk space is less than 20%"
        return info_error


def check_memory():
    info_memory = psutil.virtual_memory()
    if info_memory.available < 500:
        no_issues = False
        info_error = "Error - Available memory is less than 500MB"
        return info_error


def check_host():
    info_host = socket.gethostname()
    if info_host != "127.0.0.1":
        no_issues = False
        info_error = "Error - localhost cannot be resolved to 127.0.0.1"
        return info_error


def check_errors():
    while no_issues:
        info_error = ""
        check_cpu()
        check_space()
        check_memory()
        check_host()
        time.sleep(60)
    else:
        sender = "automation@example.com"
        recipient = "student-00-856d18cffaf1@example.com"
        subject = info_error
        body = "Please check your system and resolve the issue as soon as possible."
        attachment_path = "/tmp/processed.pdf"
        emailgen = emails.generate_email(sender, recipient, subject,
                                         body, attachment_path)
        emails.send_email(emailgen)


def main():
    check_errors()
    no_issues = True


if __name__ == "__main__":
    main()
