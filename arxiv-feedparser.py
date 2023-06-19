#!/usr/bin/env python3

# pip install feedparser
import feedparser


response = feedparser.parse('http://export.arxiv.org/api/query?search_query=cat:cs.CL&start=0&max_results=10')
[entry['title'] for entry in response['entries']]
