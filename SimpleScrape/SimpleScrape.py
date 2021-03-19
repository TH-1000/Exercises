import pandas as pd                   #for dictionaries and visual tables
from selenium.webdriver import Chrome #for webdriver
from instascrape import Profile, scrape_posts
import matplotlib.pyplot as plt       #for plots

#get session id from (inspect page source, application, session id) and paste in sessionid=''
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
    "cookie": "sessionid=sessionid"
}

address = input('Enter Profile Name: ')         #input target instagram account name
webdriver = Chrome("PATH/chromedriver.exe")     #guide selenium to chromedriver's path
profile = Profile(address)                      #use Profile() from instascrape
profile.scrape(headers=headers)                 #use session id
posts = profile.get_posts(webdriver=webdriver, login_first=False) #pops up intagram browser

#If pause is set to a lowe value, instagram might redirect you.
scraped_posts, unscraped_posts = scrape_posts(posts, headers=headers, pause=10, silent=False)

posts_data = [post.to_dict() for post in scraped_posts]#or recent_posts// make a dict out of it
posts_df = pd.DataFrame(posts_data)                    #Create a pandas DataFrame
posts_df.to_csv(address+'.csv', index = False)         #write data to csv file
print(posts_df[['upload_date', 'comments']])

webdriver.quit()

plt.style.use('fivethirtyeight')                            # Stylistic change

fig = plt.scatter(posts_df.upload_date, posts_df.comments)  # Plot the data
plt.xlabel('Upload Date')                                   # Write labels
plt.ylabel('Comments')
plt.title(f'{address} comments per Post', fontsize=18, color = 'r', fontfamily='sans-serif')
#plt.legend() - use if you want to include a legend
plt.savefig(address+'.jpeg')                                #write graph to an external file
plt.show()                                                  # Show graph
