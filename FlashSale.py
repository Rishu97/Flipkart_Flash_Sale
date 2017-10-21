import time
from selenium import webdriver
b = webdriver.Firefox() # To open the firefox browser
Not_found = True
while Not_found:#If the flash sale has not been started yet!!!!
	try:  # Has the flash sale started????
		b.get('https://www.flipkart.com/lenovo-phab-2-plus-gunmetal-grey-32-gb/p/itmeqcpncnvyfzdk?pid=MOBEQCPNG8KGCBQP&srno=s_1_2&otracker=search&lid=LSTMOBEQCPNG8KGCBQPLFSWNZ&qH=c4e0ba5422383082')
		time.sleep(1)#go directly to the product you want

		b.find_element_by_class_name('_2AkmmA._3Plo8Q._16LyaZ._7UHT_c').click()#clicking the buy now button of the product
		time.sleep(1)
		Not_found = False #The product is available for sale now!
	except:
		print 'Product not found!'

b.find_element_by_class_name('_2zrpKA._14H79F').send_keys('9109288986')#Enter the username

b.find_element_by_class_name('_2AkmmA._1poQZq._7UHT_c').click()#to click the next button

time.sleep(1)
b.find_element_by_class_name('_39M2dM._2ZvOfP').send_keys('16118062')#Enter the password
time.sleep(1)
b.find_element_by_class_name('_2AkmmA._1poQZq._7UHT_c').click()#to click the login button
time.sleep(2)
b.find_element_by_class_name('_2AkmmA._2Q4i61._7UHT_c').click()#to click continue and make the payment!!

#Enter the captcha and click place order

time.sleep(30)

b.quit()# you just bought a product! Good Bye......
