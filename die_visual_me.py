from die_me import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

# create a d6

die_1 = Die()
die_2 = Die(num_sides=10)

# make some rolls and store results in a list

rolls = []

for num in range(50_000):
    roll = die_1.roll() + die_2.roll()
    rolls.append(roll)

# print(rolls)

# analyse the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

for value in range(2,max_result+1):
    frequency = rolls.count(value)
    frequencies.append(frequency)

print(frequencies)

# visualise the results
x_values = list(range(2, max_result+1))

data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of Result"}
my_layout = Layout(title="Results of rolling one D6 and one D10 50,000 times", xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({"data": data, "layout": my_layout}, filename="d6_d10.html")