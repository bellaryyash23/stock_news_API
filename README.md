# 📈Stock Trading News Alert Program using Requests API of Python

🌟A program which fetches the closing price of mentioned stock from yesterday and day before yesterday to calculate the stock change in precentage. 

🌟If the stock change is greater than 5% then a alert message is sent to user with the percentage change mentioned and the top three articles related to that company 
formated with headline and a breif description.

👉In the 'main.py', first the stock price of the desired company is fetched by making a GET request to the API. Next this data is type casted to computable data type.

👉Now, the %change in stock value from yesterday and day before yesterday closing is calculated. If this difference is greater than 5% then a alert needs to be triggered.

👉Ater the difference/&change calculation, the appropriate condition for alert deliveris is verified and then the news related to the stock price is fetched by making 
a GET request to the API endpoint.

👉Now whenerever the % change is greater than 5% then, the condition for sending alert is verrifiec and the appropriate API calls are made and the relevant data is 
fetched. 

👉This, fetched data is used to format the alert message and sand the message to respective users registered numbers.

![Sample Messsge](https://github.com/bellaryyash23/stock_news_API/blob/master/sample.JPG?raw=true)

👆Sampled messagge how to be formated.👆
