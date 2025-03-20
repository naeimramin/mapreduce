#!/usr/bin/env python
import sys
import csv
import ast

# خواندن ورودی از STDIN
for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith('content'):  # رد کردن هدر
        continue

    try:
        reader = csv.reader([line])
        row = next(reader)
        hashtags = ast.literal_eval(row[2])  # تبدیل رشته هشتگ‌ها به لیست
        like_count = float(row[3])
        retweet_count = float(row[6])
        reply_count = float(row[5])

        for hashtag in hashtags:
            print(f"{hashtag}\t{like_count},{retweet_count},{reply_count}")
    except Exception as e:
        continue