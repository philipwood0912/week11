import csv
import matplotlib.pyplot as plt

golds = []
silvers = []
bronzes = []

categories = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print('stripping out categories')
			categories.append(row)
			line_count += 1
		else:
			if row[7] == "Gold":
				print('gold')
				golds.append(row[7])
			elif row[7] == "Silver":
				print('silver')
				silvers.append(row[7])
			elif row[7] == "Bronze":
				print('bronze')
				bronzes.append(row[7])
			line_count += 1

print(len(golds), 'gold medals were won since \'24')
print(len(silvers), 'silver medals have been won since \'28')
print(len(bronzes), 'bronze medals have been won since \'28')

totalMedals = len(golds) + len(silvers) + len(bronzes)

gold_percent = len(golds) / totalMedals * 100
print(gold_percent)
silver_percent = len(silvers) / totalMedals * 100
print(silver_percent)
bronze_percent = len(bronzes) / totalMedals * 100
print(bronze_percent)

labels = "Gold", "Silver", "Bronze"
sizes = [gold_percent, silver_percent, bronze_percent]
colors = ["crimson", "cyan", "green"]

plt.pie(sizes, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("World: Gold, Silver, Bronze Medals")
plt.xlabel("")
plt.show()
