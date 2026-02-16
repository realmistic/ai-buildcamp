# Capstone project
---

## Question 1. What would you like to work on? Describe your idea in a few sentences. (2 points)

**Investment assistant**

I typically have approximately 20–30 stocks in my portfolio, and I need to understand day-to-day sentiment, analyst estimates, stock price movements, relevant news, and overall portfolio risks.

I also need the ability to dig deeper into a specific stock if it becomes particularly interesting or experiences sudden market volatility.

Additionally, I would like to identify similar stocks within the same sectors and with comparable characteristics, such as EPS growth, revenue growth, P/E ratio, and other key financial metrics.

---

## Question 2. What should your AI system do? How do you envision it? (2 points)

The system should collect and process most of the available data on one or more stocks and synthesize meaningful insights. It should help identify risks in my portfolio, highlight positions that are performing well, and suggest potential adjustments or expansion opportunities, particularly for attractive companies.

The system should track earnings announcement dates, as these periods are often associated with increased volatility. It should help analyze whether it may be more advantageous to buy before or after earnings, especially when high-quality stocks experience price declines following earnings announcements.

Additionally, the system should read and analyze relevant news related to the selected stocks and the broader market, and perform deeper analysis to extract meaningful insights. It should distinguish between major market trends and short-term fluctuations or isolated events.

The system should also be capable of retrieving additional information from external sources when necessary to better understand emerging trends, validate signals, and provide more informed context.

---

## Question 3. Does it need any external data? If you answer "no", are you sure? Maybe it will benefit from it? (2 points)

Yes, the system will require multiple external data sources. This includes endpoints from the Yahoo Finance API, such as basic and extended company information, EPS trends, earnings dates with historical EPS estimates versus actual results, and historical OHLCV price data (daily, weekly, and monthly).

It will also use stock-specific news from sources such as Yahoo Finance and Polygon.io.

Additionally, the system will need broader market and macro-level data for thousands of stocks, including metrics such as market capitalization, EPS, revenue, profit margins, P/E ratio, dividend yield, and other key financial indicators. This data will allow the system to compare companies, identify peers, and detect broader market trends.