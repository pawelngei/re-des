from bs4 import BeautifulSoup
import os
import re

def extract_manifesto_content(html_file):
    """Extract the manifesto content from WordPress HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find the main content div
    content_div = soup.find('div', class_='nv-content-wrap entry-content')
    
    if not content_div:
        print(f"Could not find content in {html_file}")
        return None
    
    # Extract title from the h1
    title_div = soup.find('div', class_='nv-page-title')
    title = title_div.find('h1').text.strip() if title_div else "A Solarpunk Manifesto"
    
    # Convert HTML to markdown-ish text
    # Remove script tags and other junk
    for tag in content_div(['script', 'style']):
        tag.decompose()
    
    # Get text content
    text = content_div.get_text(separator='\n', strip=True)
    
    # Clean up extra whitespace
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    
    return title, text

def process_all_files():
    """Process all .md files in current directory"""
    manifesto_files = [
        'a-solarpunk-manifesto.md',
        'a-solarpunk-manifesto-arabic.md',
        'a-solarpunk-manifesto-chinese.md',
        'a-solarpunk-manifesto-farsi.md',
        'a-solarpunk-manifesto-hebrew.md',
        'a-solarpunk-manifesto-japanese.md',
        'a-solarpunk-manifesto-russian.md',
        'ein-solarpunk-manifest-deutsch.md',
        'egy-solarpunk-manifeszto-magyar.md',
        'ett-solarpunkmanifest-svenska.md',
        'manifest-solarpunka-polski.md',
        'nu-manifestu-solarpunk-sicilianu.md',
        'solarpank-manifest-srpski.md',
        'solarpunk-manifestosu-turkce.md',
        'solarpunk-manifestu-bat-euskera.md',
        'solarpunkovy-manifest-slovensky.md',
        'um-manifesto-solarpunk-portugues.md',
        'un-manifest-solarpunk-catala.md',
        'un-manifest-solarpunk-francais.md',
        'un-manifesto-solarpunk-galego.md',
        'un-manifesto-solarpunk-italiano.md',
        'un-manifiesto-solarpunk-espanol.md'
    ]
    
    for filename in manifesto_files:
        if not os.path.exists(filename):
            print(f"Skipping {filename} - file not found")
            continue
            
        print(f"Processing {filename}...")
        result = extract_manifesto_content(filename)
        
        if result:
            title, text = result
            
            # Create new markdown file
            new_content = f"""---
layout: default
title: {title}
---

{text}
"""
            
            # Write to file
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ Updated {filename}")
        else:
            print(f"✗ Failed to process {filename}")

if __name__ == "__main__":
    print("Starting manifesto extraction...")
    process_all_files()
    print("\nDone!")