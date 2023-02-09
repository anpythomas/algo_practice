# import pandas as pd
# from datetime import datetime
# import seaborn as sns
# from matplotlib import pyplot as plt
# import mplcursors
#
#
# x = [datetime(2021,8,9)] + [datetime(2021,9,12)]*2 + [datetime(2021,10,9)]*2
# y = [100, 210, 180, 300, 320]
#
# d = {'sales_date': x, 'price_usd': y}
#
# print(d)
#
# df = pd.DataFrame(d, columns=['sales_date', 'price_usd'])
# print(df)
#
#
# # # Create chart and print to screen
# sns.set(rc={'figure.figsize': (12, 6)})
# sns.lineplot(data=df, x="sales_date", y="price_usd")
# sns.scatterplot(data=df, x="sales_date", y="price_usd")
# plt.xlabel('Date of Sale')
# plt.ylabel('Price (converted to USD)')
# # plt.xticks(rotation=295)
# mplcursors.cursor(hover=True)
# plt.show()
# # plt.savefig('books_read.png')

print("Hello World" [::-1])