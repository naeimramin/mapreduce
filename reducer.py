#!/usr/bin/env python
import sys
from collections import defaultdict

# دیکشنری برای جمع‌بندی معیارها
hashtag_stats = defaultdict(lambda: {'likes': 0, 'posts': 0, 'retweets': 0, 'replies': 0})

# خواندن خروجی Shuffler/Sorter از STDIN
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    hashtag, metrics_str = line.split('\t', 1)
    metrics_list = metrics_str.split('|')

    for metrics in metrics_list:
        like_count, retweet_count, reply_count = map(float, metrics.split(','))
        hashtag_stats[hashtag]['likes'] += like_count
        hashtag_stats[hashtag]['posts'] += 1
        hashtag_stats[hashtag]['retweets'] += retweet_count
        hashtag_stats[hashtag]['replies'] += reply_count

# انتخاب 2 هشتگ برتر بر اساس مجموع لایک‌ها
top_hashtags = sorted(hashtag_stats.items(), key=lambda x: x[1]['likes'], reverse=True)[:2]

# خروجی نهایی
for hashtag, stats in top_hashtags:
    print(f"{hashtag}\t{stats['likes']},{stats['posts']},{stats['retweets']},{stats['replies']}")