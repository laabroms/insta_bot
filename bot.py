from selenium import webdriver
import time
import sys
from selenium.webdriver.common.keys import Keys



class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('./chromedriver')

    def closeBrowser(self):
        self.driver.close()

    
    
    def login(self):
        driver = self.driver
        #go to instagram home page
        driver.get('https://www.instagram.com/')
        time.sleep(1)

        # enters username
        username = driver.find_element_by_name('username')
        username.send_keys(self.username)
    
        # enters password
        password = driver.find_element_by_name('password')
        password.send_keys(self.password)

        time.sleep(1)
        # login
        # driver.find_element_by_xpath('//button[text()="Log In"]').click()
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

        time.sleep(4)

        #dont save info
        driver.find_element_by_xpath("//button[text()='Not Now']").click()

        time.sleep(2)

        #turn off notifications
        driver.find_element_by_xpath("//button[text()='Not Now']").click()
        
        #reload page
        driver.get('https://www.instagram.com/')


    def navHashtag(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)
        for x in range(1, 6):                
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
       
       
    def first_picture(self):
        driver = self.driver 
        # finds the first picture  
        pic = driver.find_element_by_class_name("_9AhH0")    
        pic.click()   # clicks on the first picture 
            
    def like_pic(self): 
        driver = self.driver
        time.sleep(2) 
        # like = driver.find_element_by_class_name('wpO6b ')
        like = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
        like.click()
        time.sleep(1)   
        
        
    def next_pic(self):
        driver = self.driver
        next = driver.find_element_by_class_name('_65Bje')
        next.send_keys(Keys.ARROW_RIGHT)
        time.sleep(2)
   

    def make_comment(self, comment):
        driver = self.driver
        # comment_box = driver.find_element_by_class_name('X7cDz')
        comment_box = driver.find_element_by_css_selector('textarea.Ypffh')
        comment_box.click()
        time.sleep(1)
        type_comment = driver.find_element_by_css_selector('textarea')
        type_comment.send_keys(comment)
        time.sleep(2)
        type_comment.send_keys(u'\ue007')
        time.sleep(3)

    def follow_account(self):
        driver = self.driver
        follow_button = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')
        follow_button.click()
        time.sleep(2)


    def get_unfollower(self, username):
        driver = self.driver
        driver.get("https://www.instagram.com/" + username + "/")    
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        time.sleep(1)
        following = []
        following = self._get_names()
        time.sleep(1)
        driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        time.sleep(1)
        followers = []
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)
        print('Number of followers: ' + str(len(followers)))
        print('Number of followings: ' + str(len(following)))
        print('Number not following back: ' + str(len(not_following_back)))

        i = 0
        while i < len(not_following_back):
            driver.get("https://www.instagram.com/" + not_following_back[i] + "/") 
            time.sleep(3)
            unfollow_button = driver.find_element_by_css_selector('span.vBF20._1OSdk')
            unfollow_button.click()
            time.sleep(2)
            unfollow_confirm = driver.find_element_by_xpath('//button[text()="Unfollow"]')
            unfollow_confirm.click()
            time.sleep(1)
            del not_following_back[i]
            time.sleep(1)
            


    def check_all_unfollowed(self, username):
        driver = self.driver
        print('Checking all unfollows')
        driver.get("https://www.instagram.com/" + username + "/")    
        time.sleep(2)
        driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        time.sleep(1)
        following = []
        following = self._get_names()
        time.sleep(1)
        driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        time.sleep(1)
        followers = []
        followers = self._get_names()
        not_following_back = []
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)
        print('Number of followers: ' + str(len(followers)))
        print('Number of followings: ' + str(len(following)))
        print('Number not following back: ' + str(len(not_following_back)))
        print('Checking all unfollows done')


    
    
    def _get_names(self):
        driver = self.driver
        time.sleep(1)
        #finds popup of following list
        # names_box = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        # scroll_box = driver.find_element_by_xpath('/html/body/div[4]')
        scroll_box = driver.find_element_by_class_name('isgrP')
        time.sleep(1)
        last_ht, ht = 0, 1
        #scrolls through list
        while last_ht != ht:
            last_ht = ht
            time.sleep(2)
            ht = driver.execute_script(""" arguments[0].scrollTo(0, arguments[0].scrollHeight); return arguments[0].scrollHeight; """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']

        #close button
        # driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
        return(names)




if __name__ == "__main__":

    username = "edits.laa"
    password = "Luca$Abrom$28"
    hashtag = "milkyway"
    comment = "Amazing shot!! Check out my last post!"

    ig = InstagramBot(username, password)
    ig.login()

    # #unfollow code
    ig.get_unfollower(username)
    ig.check_all_unfollowed(username)
    



    # #like comment and follow code
    
    # ig.navHashtag(hashtag)
    # ig.first_picture()
    # time.sleep(5)
    # pic_count = 1
    # while pic_count < 25:
    #     ig.like_pic()
    #     ig.make_comment(comment)
    #     # ig.follow_account()
    #     print('Pictures liked:'+ str(pic_count))
    #     time.sleep(12)
    #     ig.next_pic()
    #     pic_count += 1

    ig.closeBrowser()






