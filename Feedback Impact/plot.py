import matplotlib.pyplot as plt

# Sample data for the bar graph
categories = ['Satisfied', 'Not Satisfied']
values = [satisfaction.count(1),satisfaction.count(-1)]

# Creating the bar graph
plt.figure(figsize=(8, 4))
plt.bar(categories, values, color=['blue', 'green'])

# Adding titles and labels
plt.title('Sample Bar Graph')
plt.xlabel('Categories')
plt.ylabel('Values')

# Showing the bar graph
plt.show()
