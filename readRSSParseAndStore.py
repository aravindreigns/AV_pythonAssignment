# Project 7
# Read contents of an RSS feed, parse the content and store it in a text file
import concurrent.futures

import feedparser
import requests
from bs4 import BeautifulSoup


def download_url(url):
    try:
        response = requests.get(url)
        return response.content
    except Exception as e:
        print(f"Error downloading content from {url}: {e}")
        return None


def extract_content(html_content):
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        # Extract content based on your requirements
        # For example, let's extract the text inside all <p> tags
        paragraphs = soup.find_all('p')
        return '\n'.join([p.get_text() for p in paragraphs])
    return None


def process_link(link):
    try:
        # Download HTML content of the link
        html_content = download_url(link)

        # Extract content from the HTML
        extracted_content = extract_content(html_content)

        if extracted_content:
            return extracted_content

    except Exception as e:
        print(f"Error processing link {link}: {e}")

    return None


def process_rss(rss_url, output_filename):
    try:
        # Parse the RSS feed
        feed = feedparser.parse(rss_url)

        # Check if the feed is not empty
        if not feed.entries:
            print(f"Error: RSS feed is empty.")
            return

        # Create a list of links from the feed
        links = [entry.link for entry in feed.entries]
        print(links)

        # Use concurrent.futures to execute reading from multiple links in parallel
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(process_link, links))

        # Write the extracted content to output.txt
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            for result in results:
                if result:
                    output_file.write(result)
                    output_file.write('\n\n')

        print(f"Content successfully written to '{output_filename}'.")

    except Exception as e:
        print(f"Error processing RSS feed: {e}")


# Specify the RSS URL and output filename
rss_url = 'http://feeds.abcnews.com/abcnews/usheadlines'  # Replace with your RSS feed URL
output_filename = 'output.txt'

# Call the function to process the RSS feed
process_rss(rss_url, output_filename)
