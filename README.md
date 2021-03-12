# A Web Scrapping Challenge: The Red Planet
In this activity, I built a web application that scraped several websites for data on the topic of the "Mission to Mars". The results of this activities were placed in a singlt HTML page. 

The general overview of the work entailed: I used Jupyter Notebook, Pandas, Beautiful Soup and Splinter to write the web scraping code. Then in VS Code, I created two .py files (scrape_mars.py and app.py). The code from Jupyter Notebook was placed in the scrape_mars.py as functions. The app.py uses Flask and MongoDB for extract the data endpoints and store them. Finally, I created a html.index page for the data to be presented using Bootstrap and Bootswatch. Details of the work are described below.

## Step 1 - Scraping

NASA Mars News
https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest
1. Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later ("news_title" and "news_p")

JPL Mars Space Images - Featured Image
https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html
1. From the url, use splinter to navigate the site and find the image url for the current Feature Mars Image and assign the url string to a variable called "featured_image_url"
2. Make sure to find the image url to the "full size" .jpg image.
3. Make sure to save a complete url string for this image.

Mars Facts
https://space-facts.com/mars/
1. Vist the webpage and use Pandas to scrape the table containing facts about the plent including Diameter, Mass, etc.
2. Use Pandas to convert the data to a HTML table string. 

Mars Hemispheres (USGS Astrogeology site)
https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
1. Obtain high resolution images for each of Mar's hemispheres
2. Need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
3. Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
4. Apprend the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

## Step 2 - MongoDB and Flask Application
Use MongoDB with Flask templating to create a new HTML page tha tdisplays all of the informaiton taht was scraped from the URLS above.

1. Start by converting the Jupyter Notebook into Python script called "scrape_mars.py" with a funcion called "scrape" that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data. 
2. Next, create a route called "/scrape" that will import the "scrape_mars.py" script and call my scrape function.
3. Store the return value in Mongo as a Python dictionary
4. Create a root route "/" that will query your Mongo database and pass the mars data into an HTML template to display the data.
5. Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 

## After thoughts
This activity was a challenging one because it was three projects placed in one - web scrape, create API, and display in HTML. While familiary with API and HTML because of past challenges, the web scrapping was another layer to get a quick understanding of. I learned that reading Beautiful Soup and Splinter documentation greatly helped. But I would have liked a little more time to play around with their code. This activity was a good introduction to web scraping and its possibilities. I think if I delve into this work more, I should check out Selenium with Python.
