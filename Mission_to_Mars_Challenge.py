
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# web driver manager driver to scrape websites
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# ### Visit the NASA Mars News Site
# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)
html = browser.html
news_soup = BeautifulSoup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# ### Featured Images
# Visit URL using splinter
url = 'https://spaceimages-mars.com'
browser.visit(url)
# Find and click the full image button using Splinter
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()
# Parse the resulting html with Beautiful Soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')
# Find the relative image url with Beautiful Soup
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# ### Mars Facts
# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url
df = pd.read_html('https://galaxyfacts-mars.com')[0] #0 tells pd to pull the 1st table it finds!
df.columns=['Description', 'Mars', 'Earth'] #add columns 
df.set_index('Description', inplace=True)
df.to_html()


# Scrape High-Resolution Mars’ Hemisphere Images and Titles
# ### Hemispheres

# Use browser to visit the URL 
hemispheres_url = 'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/index.html'
browser.visit(hemispheres_url)
# HTML Object
html_hemispheres = browser.html
# Parse HTML with Beautiful Soup
soup = BeautifulSoup(html_hemispheres, 'html.parser')
# Retreive all items that contain mars hemispheres information
# items = soup.find_by_all("div.collapsible").find_by_tag("a").find_by_tag("img")
items = soup.find_all('div', class_='item')
# Create empty list for hemisphere urls 
hemisphere_image_urls = []
# Store the main_ul 
hemispheres_main_url = 'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/'

for i in items: 

    # Store title
    title = i.find('h3').text
    
    # Store partial link that leads to full image website
    partial_img_url = i.find('a', class_='itemLink product-item')['href']
    
    # Store full link that leads to full image website
    img_url = hemispheres_main_url + partial_img_url
    
    # Visit the link that contains the full image website 
    browser.visit(img_url)
    
    # HTML Object of individual hemisphere information website 
    partial_img_html = browser.html
    
    # Parse HTML with Beautiful Soup for every individual hemisphere information website 
    soup = BeautifulSoup(partial_img_html, 'html.parser')
    
    # Retrieve full image source 
    img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
    
    # Append the retreived information into a list of dictionaries 
    hemisphere_image_urls.append({"title" : title, "img_url" : img_url})

hemisphere_image_urls

# 5. Quit the browser
# browser.quit()






