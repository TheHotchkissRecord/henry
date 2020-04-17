#!/usr/bin/env python
# coding: utf-8
# Copyright The Hotchkiss Record & Jiahua Chen

import re
import os
from os import path
import datetime
import calendar
import htmlmin


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')
    print(color.BOLD +
          "██╗  ██╗███████╗███╗   ██╗██████╗ ██╗   ██╗ TM\n" +
          "██║  ██║██╔════╝████╗  ██║██╔══██╗╚██╗ ██╔╝\n" +
          "███████║█████╗  ██╔██╗ ██║██████╔╝ ╚████╔╝ \n" +
          "██╔══██║██╔══╝  ██║╚██╗██║██╔══██╗  ╚██╔╝  \n" +
          "██║  ██║███████╗██║ ╚████║██║  ██║   ██║   \n" +
          "╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   " + color.END)
    print(color.BOLD + "- The Hotchkiss Record\'s Newsletter Wizard -" + color.END)
    print("────────────────────────────────────────────\n")


print("\x1b[8;80;80t")

clear()
dir = ""
while True:
    dir = input(
        color.BOLD + color.UNDERLINE + "Config\n" + color.END + "Henry needs some information about the directory you want to work in, please drag and drop the folder that Henry is located in here: ")
    dir = dir.replace(" ", "") + "/"
    if not (os.path.exists(dir + "templates/main.mjml") and os.path.exists(dir + "templates/article.mjml")):
        print(
                "\nError! Henry did not find the necessary template files in your directory. Please ensure that " + color.DARKCYAN + "templates/main.mjml" + color.END + " and " + color.DARKCYAN + "templates/article.mjml" + color.END + " are in your directory. \n")
    else:
        break

f = open(dir + "templates/main.mjml")
content = f.read()
f.close()

clear()
print(
        color.BOLD + "Henry" + color.END + " is named after " + color.BOLD + "Henry Luce" + color.END + "(if you don't know who he is, search him up!). \nIt is a small Python script that helps create \'Off the Record\' Newsletters.\n")

print("Let's start with the basics, Henry needs to know the day that this will be sent out. ")

while True:
    yyyy = input(
        "What is the" + color.BOLD + " year " + color.END + "of the newsletter" + color.DARKCYAN + " (YYYY)" + color.END + ": ")
    if not re.match("^\d{4}$", yyyy):
        print("Error! Please enter a valid year! ")
    else:
        break

while True:
    mm = input(
        "What is the" + color.BOLD + " month " + color.END + "of the newsletter" + color.DARKCYAN + " (MM)" + color.END + ": ")
    if not re.match("^(0?[1-9]|1[012])$", mm):
        print("Error! Please enter a valid month in format" + color.DARKCYAN + " (MM)" + color.END + "! ")
    else:
        break
mm = str(int(mm))

while True:
    dd = input(
        "What is the" + color.BOLD + " day " + color.END + "of the newsletter" + color.DARKCYAN + " (DD)" + color.END + ": ")
    if not re.match("^(0?[1-9]|[12]\d|3[01])$", dd):
        print("Error! Please enter a valid day in format" + color.DARKCYAN + " (DD)" + color.END + "! ")
    else:
        break
dd = str(int(dd))

date = datetime.date(int(yyyy), int(mm), int(dd))
weekday = datetime.date(int(yyyy), int(mm), int(dd)).weekday()
weekday_text = calendar.day_name[weekday]
month_text = calendar.month_name[int(mm)]
print(
        "\nGreat! I've got the date down as " + color.BOLD + weekday_text + ", " + month_text + " " + dd + ", " + yyyy + color.END + ". ")
input("Press" + color.BOLD + " enter " + color.END + "to continue")

clear()

mmddyyyy = "{0:0=2d}".format(int(mm)) + "{0:0=2d}".format(int(dd)) + yyyy
yyyymmdd =  yyyy + "{0:0=2d}".format(int(mm)) + "{0:0=2d}".format(int(dd))

if not os.path.exists(dir + mmddyyyy):
    print(
            "It doesn't look like a folder for articles exists yet, Henry will create them for you. You will find a folder titled \"" + mmddyyyy +
            "\".")
    os.makedirs(dir + mmddyyyy)
else:
    print("It looks like you already have a folder for the articles, great! ")

if not os.path.exists(dir + mmddyyyy + '/info.txt'):
    info = open(dir + mmddyyyy + "/info.txt", "x")
    info.write(
        "Give a description of the newsletter, this will be used as the email preview. Begin on the next line: \n")
    info.close()

if not os.path.exists(dir + mmddyyyy + '/editorial.txt'):
    editorial = open(dir + mmddyyyy + "/editorial.txt", "x")
    editorial.write("Input the editorial message on the next line: \n")
    editorial.close()

if not os.path.exists(dir + mmddyyyy + '/articles'):
    os.makedirs(dir + mmddyyyy + '/articles')
    temp_art = open(dir + mmddyyyy + "/articles/1.txt", "x")
    temp_art.write("Article title (on next line): \n\n\n")
    temp_art.write("What is the link of the article (next line): \n\n\n")
    temp_art.write("Byline (FirstName LastName \'19): \n\n\n")
    temp_art.write("Content preview: \n\n\n")
    temp_art.write("If there is a thumbnail image, give it a caption. Otherwise, leave it blank: \n\n\n")
    temp_art.write("If there is a thumbnail image, put the link on the next line. Otherwise, leave it blank. \n")
    temp_art.close()

print("\nKeep in mind that Henry expects the files to be in the following format: \n" + color.DARKCYAN +
      " ├── " + mmddyyyy + "/" + color.BOLD + "info.txt\n" + color.END + color.DARKCYAN +
      " ├── " + mmddyyyy + "/" + color.BOLD + "editorial.txt\n" + color.END + color.DARKCYAN +
      " └── " + mmddyyyy + "/" + color.BOLD + "articles" + color.END + color.DARKCYAN + "/ (this is a folder of articles)\n" +
      "    ├── " + mmddyyyy + "/articles/" + color.BOLD + "1.txt\n" + color.END + color.DARKCYAN +
      "    ├── " + mmddyyyy + "/articles/" + color.BOLD + "2.txt\n" + color.END + color.DARKCYAN +
      "    └── " + "... for however many articles are in the newsletter, in order\n" + color.END)
print(
    "Any additional files have been created by Henry. If you need to regenerate a file, delete that file and run Henry again. \n\nFill in the required blanks in the created files. For articles, copy the format for as many articles as there are and number them in order.\n")

input("Press" + color.BOLD + " enter " + color.END + "to continue")

clear()

print(
        "Off the Record for " + color.BOLD + weekday_text + ", " + month_text + " " + dd + ", " + yyyy + color.END + ".\n")
content = content.replace("%YYYYMMDD", yyyymmdd)
content = content.replace("%Month", month_text)
content = content.replace("%DD", dd)
content = content.replace("%YYYY", yyyy)
content = content.replace("%Weekday", weekday_text)

try:
    info = open(dir + mmddyyyy + "/info.txt")
    description_text = info.readlines()[1]
    info.close()
except IndexError:
    print("It seems like your description is empty. ")
    description_text = ""

print(color.BOLD + color.UNDERLINE + "Description" + color.END + ": " + description_text)
content = content.replace("%Description", description_text)

try:
    editorial = open(dir + mmddyyyy + "/editorial.txt")
    editorial_text = editorial.readlines()[1]
    editorial.close()
except IndexError:
    print("It seems like your editorial is empty. ")
    editorial_text = ""

print(color.BOLD + color.UNDERLINE + "Editorial" + color.END + ": " + editorial_text)
content = content.replace("%Editorial", editorial_text)

article_num = 1
all_articles_text = ""
link_regex = "https?:\\/\\/(www\\.)?[-a-zA-Z0-9@:%._\\+~\#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b([-a-zA-Z0-9()@:%_\\+.~\#?&//=]*)"

while os.path.exists(dir + mmddyyyy + '/articles/' + str(article_num) + ".txt"):
    article = open(dir + mmddyyyy + '/articles/' + str(article_num) + ".txt")
    lines = article.readlines()
    title = lines[1]
    print(color.BOLD + color.UNDERLINE + "Article " + str(article_num) + color.END + ": " + title)
    link = lines[4]
    if not re.match(link_regex, link):
        print("The link for " + color.BOLD + color.UNDERLINE + "article " + str(
            article_num) + color.END + " is not properly formatted, Henry will continue the build, but please ensure the link is in the proper format. ")
    byline = lines[7]
    preview = lines[10]
    caption = lines[13]
    is_thumbnail = True
    thumbnail = ""
    try:
        thumbnail = lines[16]
    except IndexError:
        caption = ""

    if not re.match(link_regex, thumbnail):
        is_thumbnail = False
        print(
                color.BOLD + "*" + color.END + " No proper thumbnail image detected for " + color.BOLD + color.UNDERLINE + "article " + str(
            article_num) + color.END + ", Henry will not include an image for it. ")
    article.close()
    article_f = open(dir + "templates/article.mjml")
    article_text = article_f.read()
    article_f.close()

    # Does replacing:
    if is_thumbnail:
        article_text = article_text.replace("<!-- Thumbnail -->",
                                            "<mj-image src=\"%Thumbnail\" width=\"600px\" alt=\"\" padding=\"0\" href=\"%Link\" />")
        article_text = article_text.replace("%Thumbnail", thumbnail)
    article_text = article_text.replace("%Caption", caption)
    article_text = article_text.replace("%Title", title)
    article_text = article_text.replace("%Author", byline)
    article_text = article_text.replace("%Preview", preview)
    article_text = article_text.replace("%Link", link)
    all_articles_text += article_text
    article_num += 1

content = content.replace("%Articles", all_articles_text)
content = content.replace("\n", "")
outfile = open(dir + mmddyyyy + '/index.mjml', 'w+')
content = htmlmin.minify(content, remove_empty_space=True)
outfile.write(content)
outfile.close()
print(
            "\nHenry has written (or overwritten) the newsletter at " + color.BOLD + mmddyyyy + '/index.mjml' + color.END + '. You may use mjml.io/try-it-live to compile it or compile it using npm from the command line. \n\n\n')
