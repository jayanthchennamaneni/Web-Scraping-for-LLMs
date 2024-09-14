# Web Scraping for LLMs

## Description

This project is a web scraping tool designed to extract and convert web content into Markdown format. It leverages Scrapy to crawl web pages and BeautifulSoup to clean up the HTML. The cleaned HTML is then converted into Markdown using the markdownify library. This tool is particularly useful for creating datasets from web content that can be used for training or fine-tuning Large Language Models (LLMs) or for other data analysis purposes.

## Features

- **Web Crawling**: Starts from a specified URL and follows links to gather more pages.
- **HTML Cleanup**: Removes unnecessary tags such as `<script>`, `<style>`, `<nav>`, `<footer>`, `<form>`, and `<input>`.
- **Markdown Conversion**: Converts cleaned HTML into Markdown format for easier readability and processing.

## Requirements

To run this project, you'll need to install the following Python packages:

- `scrapy`
- `requests`
- `beautifulsoup4`
- `markdownify`

You can install these dependencies using `pip` by running:

```bash
pip install -r requirements.txt

```
---
