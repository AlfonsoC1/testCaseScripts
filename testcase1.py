from selenium import webdriver

print('Input 16 digits')
userInput = raw_input()

browser = webdriver.Firefox()
browser.get('http://jeremydomasian.github.io/supercalc_v1-4/SuperCalc-v4.html')

inputElem = browser.find_element_by_name('one')
inputElem.click()

count = 0
while (count < 16):
	inputElem.click()
	count = count + 1

