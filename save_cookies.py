from selenium import webdriver
import pickle

d = webdriver.Chrome()
d.get("https://www.booking.com/login.html")

input("Uloguj se pa pritisni Enter...")

pickle.dump(d.get_cookies(), open("cookies.pkl", "wb"))
print("Cookies sačuvani.")
d.quit()
