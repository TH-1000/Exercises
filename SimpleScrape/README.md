# Simplescrape

1. ## Introduction

   - What does it do:

    Simplescrape gets Instagram posts and uses object building tools to produce tables, sheets and graphs for further data analysis.
    This program puts together the pieces needed for a simple Instagram search and data collection.

  - Example:
    Enter Profile name: chickenway.lb

    output: (check out chickenway_lb.csv for the detailed csv output file.)

    ![test console](https://github.com/TH-1000/SimpleScrape/blob/main/Consolescreenshot.PNG)
    ![test graph](https://github.com/TH-1000/scrape_and_graph/blob/main/test.jpg?raw=true)

2. ## Dependencies:

  - Insta-scrape:
    This program uses InstaScrape (https://github.com/chris-greening/instascrape) to collect Instagram post data.
    You can install Instascrape using: `pip3 install insta-scrape`

    *WARNING*: make sure you install insta-scrape and not a package with a similar name!

  - Selenium.WebDriver:
    Selenium Will be used to operate the WebDriver(https://www.selenium.dev/documentation).

    You can install Selenium using: `pip install selenium`

  - Pandas (optional):
    Pandas can be utilized to create and manipulate dataframes. Any other similar proram can be used.Pandas docs: https://pandas.pydata.org/docs/

    `pip install pandas`

  - Matplotlib (optional):
    Matplot can be used to plot and customize graphs. Any other program can be used. Docs: https://matplotlib.org/stable/contents.html

    `pip install matplotlib`

3. ## How it works:

  - Scraping:

    - `Profile()`
      uses Selenium.WebDriver to open a new webdriver browser and go
      to instagram and fetch the profile.

    - `get_recent_posts()`

      gets the recent 12 posts.

    - `scrape(mapping=None, keys: Optional[List[str]] = None, exclude: O      ptional[List[str]] = None, headers={'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57'}, inplace=True, session=None, webdriver=None) → None`

    - Scrape data from the source.

        - mapping (Dict[str, deque]) – Dictionary of parsing queue’s that tell the JSON engine how to process the JSON data
        - keys (List[str]) – List of strings that correspond to desired attributes for scraping
        - exclude (List[str]) – List of strings that correspond to which attributes to exclude from being scraped
        - headers (Dict[str, str]) – Dictionary of request headers to be passed on the GET request
        - inplace (bool) – Determines if data modified inplace or return a new object with the scraped data
        - session (requests.Session) – Session for making the GET request
        - webdriver (selenium.webdriver.chrome.webdriver.WebDriver) –          Webdriver for scraping the page, overrides any default or passed session

    - `get_posts(webdriver, amount=None, login_first=False, login_pause=60, max_failed_scroll=300, scrape=False, scrape_pause=5)`

      - webdriver (selenium.webdriver.chrome.webdriver.WebDriver) – Selenium -webdriver for rendering JavaScript and loading dynamic content
      - amount (int) – Amount of posts to return, default is all of them
      - login_first (bool) – Start on login page to allow user to manually login to Instagram
      - login_pause (int) – Length of time in seconds to pause before starting scrape
      - max_failed_scroll (int) – Maximum amount of scroll attempts before stopping if scroll is stuck
      - scrape (bool) – Scrape posts with the webdriver prior to returning
      - scrape_pause (int) – Time in seconds between each scrape

 - DataFrame:

    You can manipulate, analyze and save the data acquired by using pandas DataFrame. Check out Pandas documentation for more info.

    - `pd.DataFrame(posts_data)` creates a panda DataFrame from pulled data.

    - `df.to_csv(path, index=False)` saves data to a csv file(without   including the index).

 - Plotting:

    By using the features of Matplotlib, you can visualize your data. Many style features are also available for different effects. (Bar Charts, Scatter, Heatmap, etc...)

    - `plt.style.use('fivethirtyeight')` creates a plot with a chosen style    theme. Check out https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html

    - `fig = plt.scatter(posts_df.upload_date, posts_df.comments)` plots the data using scatter, and assigns it to variable fig. After specifying your chosen metrics, axes and title you `plt.savefig(path)` and produce a file.

 4. ## Restrictions:

    - Session id: A session id might be required as Instagram does not like scrapers. You can get it by inspecting the page source of your Instagram session.

    - Likes: Since likes are not public and the number of likes is not accurate, your `posts_df.likes` returns -1.

    - Pause time: if you set pause time to a low value (10 is safe), your account might get temporarily blocked by Instagram.

Thank you.
