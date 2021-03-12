from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def scrape_all():
    # excutable path
    executable_path = {"executable_path": ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    news_title, news_paragraph = mars_news(browser)

    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres": hemispheres(browser)
    }

    browser.quit()
    return data


def mars_news(browser):
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    browser.is_element_not_present_by_css(
        'ul.item_list li.slide', wait_time=1)

    html = browser.html
    soup = bs(html, 'html.parser')

    try:
        slide_element = soup.select_one('ul.item_list li.slide')
        news_title = slide_element.find(
            "div", class_='content_title').get_text()
        news_p = slide_element.find(
            "div", class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p


def featured_image(browser):
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    browser.is_element_not_present_by_css("h2", wait_time=3)

    # use splinter code to click the second button for the full image
    full_image_element = browser.find_by_tag('button')[1]
    full_image_element.click()

    html = browser.html
    image_soup = bs(html, 'html.parser')

    try:
        target_img_url = image_soup.find(
            'img', class_='fancybox-image').get('src')

    except AttributeError:
        print(None)

    img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{target_img_url}'

    return img_url


def mars_facts():
    df = pd.read_html('https://space-facts.com/mars/')[0]
    df.columns = ['Description', 'Mars']
    df.set_index('Description', inplace=True)
    return df.to_html(classes="table table-striped")


def hemispheres(browser):
    url = (
        "https://astrogeology.usgs.gov/search/"
        "results?q=hemisphere+enhanced&k1=target&v1=Mars"
    )

    browser.vist(url)

    hemisphere_image_urls = []

    links = browser.find_by_css("a.product-item h3")

    for index in range(len(links)):
        hemisphere = {}

        browser.find_by_css("a.product-item h3")[index].click()

        try:
            sample_element = browser.links.find_by_text("Sample").first

            hemisphere["title"] = browser.find_by_css("h2.title").text
            hemisphere["link"] = sample_element["href"]

            hemisphere_image_urls.append(hemisphere)
            browser.back()
        except:
            return None

    return hemisphere_image_urls


if __name__ == "__main__":
    print(scrape_all())
