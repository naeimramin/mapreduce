#!/usr/bin/env python
import sys
from collections import defaultdict

# دیکشنری برای گروه‌بندی داده‌ها
grouped_data = defaultdict(list)

# خواندن خروجی Mapper از STDIN
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    hashtag, metrics = line.split('\t', 1)
    grouped_data[hashtag].append(metrics)

# مرتب‌سازی و خروجی
for hashtag in sorted(grouped_data.keys()):  # مرتب‌سازی بر اساس هشتگ
    metrics_list = grouped_data[hashtag]
    print(f"{hashtag}\t{'|'.join(metrics_list)}")