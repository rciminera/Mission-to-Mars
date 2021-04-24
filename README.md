# Mission-to-Mars

## Overview

In this project an application was created to scrape the web for information about Mars and then present it on a webpage.

### Tools Used

 Following are the tools used to scrape, parse, store, and present the information.

**Chrome Web Driver:** Chrome Web-Driver Manager was used to scrape the Mars websites.

**Beautiful Soup:** BeautifulSoup is a tool that parses the HTML code behind the web pages for use by Python scripts to create lists and dictionaries.

**Splinter:** Splinter automates browser navigation to open a browser, visit a webpage, and then interact with it.

**Mongo DB:** Mongo is a document database that is useful for storing images and documents as well as other objects for presentation on a web page.

**Flask:** Flask is a python web framework used to develop the web app.

**CSS Bootstrap:** CSS Boostrap was used to style the presentation of content of the webpage to make it more readable.

## Project Deliverables

I. Scrape Mars Data

The first deliverable for the project was a script to scrape various Mars related websites to create a series of python data sets storing text, links to key sites, as well as image urls.

Chrome Webdriver, Splinter, Beautiful Soup, and Python were integrated into the following Jupyter notebook script

[Mission-to-Mars_Challenge.ipynb](https://github.com/rciminera/Mission-to-Mars/blob/main/Mission_to_Mars_Challenge.ipynb)

The script culminates in a list of dictionaries with url links to the full-resolution images of the four Mars hemispheres.  

![GitHubLogo](https://github.com/rciminera/Mission-to-Mars/blob/main/Screenshots/hemi_url_title.png)

II. Create a "Mission to Mars" Web App

The second deliverable was to create an app to drive a web page to present the data scraped in the first deliverable.

The Jupyter notebook created earlier was converted to a Python script with functions to create a dictionary to be loaded into a Mongo Database.

[scraping.py](https://github.com/rciminera/Mission-to-Mars/blob/main/scraping.py)

An python app script was then created using Flask to set up routes to create the home page as well as the scraping button. This app will also perform the critical function of connecting to Mongo where the Mars data will be stored for presentation on the web page.

[app.py](https://github.com/rciminera/Mission-to-Mars/blob/main/app.py)

To present the web page, Index HTML was created 

[index.html](https://github.com/rciminera/Mission-to-Mars/blob/main/templates/index.html)

![GitHubLogo](https://github.com/rciminera/Mission-to-Mars/blob/main/Screenshots/hemi2x2_jpg.png)

III. Format the Web Page

For the third and final deliverable, Bootstrap was used to make three modifications to the webpage to make it more readable.

![GitHubLogo](https://github.com/rciminera/Mission-to-Mars/blob/main/Screenshots/final_webpage.png)

The first was to aling the hemisphere images from 2 per row to 4 per row and the second was to shrink the font size of the captions in conjuntion with the images.

![GitHubLogo](https://github.com/rciminera/Mission-to-Mars/blob/main/Screenshots/css_hemi.png)

The third change was to change the color of the scraping button to green as in "go" versus the default blue color.

![GitHubLogo](https://github.com/rciminera/Mission-to-Mars/blob/main/Screenshots/css_btn.png)

Finally, the CSS Bootstrap code adapts the size of the web page to the device it is being presented on including mobile phones.

![GitHubLogo](https://github.com/rciminera/Mission-to-Mars/blob/main/Screenshots/mobile.png)


## Conclusion

The Mission to Mars webpage is a concise and readable web page that provides a quick recap of the latest Mars news as well as images and key facts about Earth's next door planetary neighbor.  

If you plan to visit don't forget the O2 and warm socks!






