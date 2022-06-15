import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "/Users/possumplows/PycharmProjects/crash course/pythonProject/2973066.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    for index, column_header in enumerate(header_row):
        print(index, column_header)

#     get high temperatures from this file
    dates, rains = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            rain = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}.")
        else:
            dates.append(current_date)
            rains.append(rain)


print(dates)

# plot the high temperatures
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, rains, c="red", alpha=1.0)
# ax.plot(dates, lows, c="blue", alpha=0.5)
# ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# format plot
ax.set_title("Daily Rainfall\nHollywood SC 2021", fontsize=20)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation (f)", fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=16)

plt.show()
