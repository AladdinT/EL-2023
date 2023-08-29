import requests
from bs4 import BeautifulSoup

# Replace 'your_url_here' with the actual URL containing the HTML content
url = 'https://translate.google.com/?sl=ar&tl=en&text=%D9%85%D8%B3%D8%A7%D8%A1%20%D8%A7%D9%84%D8%AE%D9%8A%D8%B1%20%D9%8A%D8%A7%20%D8%A8%D9%88%D8%B5%20%D9%8A%D8%A7%20&op=translate'

# Send a GET request to the URL
response = requests.get(url)


# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Get the HTML content
html_content = response.text

# Define the filename to save the HTML content
filename = 'output.html'

# Write the HTML content to a file
with open(filename, 'w', encoding='utf-8') as file:
    file.write(html_content)
    
# Find all <textarea> tags
textarea_tags = soup.find_all('textarea')
mytag = soup.find_all("textarea",{"lang":"en"})
mytag1 = soup.find_all("span",{"class":"ryNqvb"})
print(mytag1)

# Extract and print text from each <textarea> tag
for textarea_tag in textarea_tags:
    textarea_text = textarea_tag.get_text()
    print("Text inside <textarea> tag:")
    print(textarea_text)
    print()  # Add an empty line between outputs

# # Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(response.content, 'lxml')

# # Find the <textarea> tag
# textarea_tag = soup.find_all('textarea')
# print(textarea_tag)
# # Extract the text from the <textarea> tag
# for tags in textarea_tag:
#     if tags:
#         textarea_text = tags.get_text()
#         print("Text inside <textarea> tag:")
#         print(textarea_text)
#     else:
#         print("No <textarea> tag found on the page.")
