
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres": hemispheres(browser),
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data

def mars_news(browser):

    # ### Visit the NASA Mars News Site
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)
    
    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)
    
    # Convert the browser html to a soup object
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')
    
    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()
        news_title
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
        news_p

    except AttributeError:
        return None, None

    return news_title, news_p

def featured_image(browser):
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

    #Add try/except for error handling
    try:
        # Find the relative image url with Beautiful Soup
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
        img_url_rel

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url


def mars_facts():
# Mars Facts
    try:
        df = pd.read_html('https://galaxyfacts-mars.com')[0] #0 tells pd to pull the 1st table it finds!
    
    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth'] #add columns 
    df.set_index('Description', inplace=True)

    # Convert datframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")


# Scrape High-Resolution Mars’ Hemisphere Images and Titles
# ### Hemispheres
def hemispheres(browser):

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

        hemispheres = {}
        
        # Store title
        title = i.find('h3').text
        # add title to hemispheres dict
        hemispheres['title'] = title
        
        # Store full link that leads to full image website
        img_url = hemispheres_main_url + i.find('a', class_='itemLink product-item')['href']
        # Visit the link that contains the full image website 
        browser.visit(img_url)
        # HTML Object of individual hemisphere information website 
        img_html = browser.html
        # Parse HTML with Beautiful Soup for every individual hemisphere information website 
        soup = BeautifulSoup(img_html, 'html.parser')
        # Retrieve full image source 
        img_url = hemispheres_main_url + soup.find('ul').li.a['href']
        # add image_url to hemispheres dict
        hemispheres['img_url'] = img_url
        
        # Append the retreived information into the list of dictionaries 
        # hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
        hemisphere_image_urls.append(hemispheres)

    return hemisphere_image_urls

if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())




