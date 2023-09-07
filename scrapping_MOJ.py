from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv
from bs4 import BeautifulSoup


# reading files
with open("saved_urls.txt", "r") as file:
    all_links = file.read().split("\n")

# List of links
links = all_links
workings_links = []
# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)

# Create a Chrome webdriver instance
driver = webdriver.Chrome(options=chrome_options)

# Open the output files
with open('output2.txt', 'w', encoding='utf-8') as txt_file, open('output2.csv', 'w', encoding='utf-8', newline='') as csv_file:
    txt_writer = txt_file
    csv_writer = csv.writer(csv_file)

    # Loop through the links and process each page
    for link in links:
        driver.get(link)

        # Check if the page contains the specified text
        if 'الصفحة المطلوبة غير موجودة' in driver.page_source:
            print(f"Skipping link: {link}")
            continue

        # Get the page source HTML
        page_source = driver.page_source
        workings_links.append(link)
        # Create BeautifulSoup object from the page source
        soup = BeautifulSoup(page_source, 'html.parser')

        # Find all <p> elements with class "justfy line-hi"
        paragraphs = soup.find_all('p', class_='justfy line-hi')

        # Save the text in .txt and .csv files
        for paragraph in paragraphs:
            text = paragraph.get_text(strip=True)
            txt_writer.write(text.replace("\n", " ") + '\n')
            csv_writer.writerow([text.replace("\n", " ")])

        print(f"Link processed: {link}")

# Close the Chrome webdriver
driver.quit()

# saving working links 
with open("working_links.txt","w") as file:
    file.write("\n".join(workings_links))
    
    
# some stats
### number of words in the file and characters

# with open('output2.txt', 'r', encoding="utf-8") as file:
#     contents = file.read()
#     words = contents.split()
#     num_words = len(words)
#     num_chars = len(contents)
#     unique_words = set(words)
#     num_unique_words = len(unique_words)

# print("Number of words:", num_words)
# print("Number of characters:", num_chars)
# print("Number of unique words:", num_unique_words)

### graph for 50 words in all cases

# import matplotlib.pyplot as plt
# from collections import Counter
# import arabic_reshaper
# from bidi.algorithm import get_display

# with open('output2.txt', 'r', encoding="utf-8") as file:
#     contents = file.read()
#     words = contents.split()
#     word_count = Counter(words)
#     total_words = len(words)
#     word_percentages = {word: count/total_words*100 for word, count in word_count.items()}
#     top_words = dict(sorted(word_percentages.items(), key=lambda item: item[1], reverse=True)[:50])

# plt.bar([get_display(arabic_reshaper.reshape(word)) for word in top_words.keys()], top_words.values())
# plt.xticks(rotation=90)
# plt.xlabel('Words')
# plt.ylabel('Percentage')
# plt.title('Top 50 Words in Text File')
# plt.show()


### clean the dataset then most 50 frequently
# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# import re
# from collections import Counter
# import matplotlib.pyplot as plt
# import arabic_reshaper
# from bidi.algorithm import get_display


# # Download the Arabic stopwords corpus
# nltk.download('stopwords')

# # Read the text file
# with open('output2.txt', 'r', encoding='utf-8') as file:
#     text = file.read()

# # Remove symbols and unimportant characters
# text = re.sub(r'[^\w\s]', '', text)
# text = re.sub(r'\d+', '', text)
# text = re.sub(r'\s+', ' ', text)

# # Tokenize the text into words
# words = word_tokenize(text)

# # Remove the stopwords
# stop_words = set(stopwords.words('arabic'))
# filtered_words = [word for word in words if word not in stop_words]

# # Count the frequency of each word
# word_counts = Counter(filtered_words)

# # Get the 30 most common words
# top_words = word_counts.most_common(30)

# # Plot a bar chart of the top 30 words
# #get_display(arabic_reshaper.reshape(word[0])
# plt.bar([get_display(arabic_reshaper.reshape(word[0])) for word in top_words], [word[1] for word in top_words])
# plt.xticks(rotation=90)
# plt.show()


### number of collected cases
# with open('output2.txt', 'r', encoding="utf-8") as file:
#     contents = file.read()
#     paragraphs = contents.split("\n")

# print("number of cases collected: ",len(paragraphs))

### saparated cases
# import pandas as pd

# df = pd.read_csv("output_modified.csv",encoding="utf-8")

# print(df.info())


