#!/usr/bin/env python
# coding: utf-8

# In[60]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[61]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[27]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[28]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[29]:


slide_elem.find('div', class_='content_title')


# In[30]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[31]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[32]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[33]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[34]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[35]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[36]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[37]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[38]:


df.to_html()


# In[58]:


browser.quit()


# In[ ]:





# In[55]:


import requests


# In[62]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)


# In[63]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# In[64]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
#print(content)
hemis_soup = soup(html, 'html.parser')
images = hemis_soup.find_all('a', class_='itemLink product-item')
images_set =list(set([image['href'] for image in images if image['href'].find('#')== -1]))
print(images_set)

for image_url in images_set:
    base_image_urls = f'{url}{image_url}'
    browser.visit(base_image_urls)
    html = browser.html
    img_temp = soup(html, 'html.parser')
    title = img_temp.find('h2').text
    
    try:
        full_image=browser.find_by_css('#wide-image > div > ul > li:nth-child(1) > a').first
        hemisphere_image_urls.append({"image_url": full_image['href'], "title":title})
        print(full_image['href'])
        browser.back()
        
    except Exception as e :
        print(e)


# In[65]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[66]:


# 5. Quit the browser
browser.quit()


# In[ ]:




