import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = '<INSERT AMAZON PRODUCT URL>'

headers = {"<INSERT AGENT STRING>"}

def check_price():
	page = requests.get(url, headers=headers)

	soup = BeautifulSoup(page.content, 'html.parser')

	title = soup.find(id="productTitle").get_text()
	price = soup.find(id="priceblock_ourprice").get_text()
	converted_price = float(price[0:5])

	if(converted_price < <INSERT DESIRED BUY PRICE>:
		send_mail()
		
	print(title.strip()
	print(converted_price)
	
def send_mail():
	server = smtplib.SMTP('<INSERT SMTP SERVER>, <INSERT SERVER PORT>'
	server.ehlo()
	server.starttls()
	server.ehlo()
	
	server.login('<USERNAME>', '<PASSWORD>')
	subject = 'Buy price reached!'
	body = '<PRODUCT> has reached your buy price, click here <URL>.'
	
	msg = f"Subject: {subject} \n \n {body}"
	
	server.sendmail(
		'<FROM EMAIL>'
		'<TO EMAIL>'
		msg
	)
	print('Email sent.')
	server.quit()

while(True):
	check_price()
	time.sleep(<SECONDS TO DELAY>)
