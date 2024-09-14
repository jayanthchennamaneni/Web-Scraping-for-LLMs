import os
import json
from bs4 import BeautifulSoup
import markdownify
import html

# Ensure the output directory exists
output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load the JSON output from the crawling process
with open('output.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

def clean_html(html_content):
    """
    Clean up the HTML by removing unnecessary tags and decoding special characters.
    Removes tags like <script>, <style>, <nav>, <footer>, <form>, and <input>.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove <script>, <style> tags, navigation menus and footers, Remove forms and input elements
    for tag in soup(['script', 'style', 'nav', 'footer', 'form', 'input']):
        tag.extract()

    # Decode HTML entities (like &lt; to <)
    cleaned_html = html.unescape(str(soup))
    
    return cleaned_html

def html_to_markdown(html_content):
    """
    Convert cleaned HTML content into Markdown format using markdownify.
    """
    # Clean the HTML content (removing scripts, navigation, etc.)
    cleaned_html = clean_html(html_content)

    # Convert remaining HTML to Markdown using markdownify
    markdown_content = markdownify.markdownify(
        cleaned_html,
        heading_style="ATX",  # Use ATX-style headings (#, ##, ###)
        bullets="-",  # Use '-' for unordered lists
        code_language="python"  # Default code language if applicable
    )

    return markdown_content

def remove_empty_lines(content):
    """
    Remove empty lines and lines with only whitespace from the content.
    """
    # Split the content into lines
    lines = content.splitlines()

    # Remove lines that are empty or only contain whitespace
    cleaned_lines = [line for line in lines if line.strip()]

    # Join the cleaned lines back into a single string
    cleaned_content = '\n'.join(cleaned_lines)
    return cleaned_content

# Loop through each page in the JSON and convert HTML to Markdown
for page in pages:
    url = page['url']
    html_content = page['html']
    markdown_content = html_to_markdown(html_content)

    # Remove empty lines from the Markdown content
    markdown_content = remove_empty_lines(markdown_content)

    # Generate a valid filename from the URL (replace slashes with underscores)
    filename = url.replace('https://', '').replace('/', '_') + '.md'

    # Save the Markdown content to the output directory
    with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as md_file:
        md_file.write(markdown_content)

    print(f"Saved {url} as {filename}")
