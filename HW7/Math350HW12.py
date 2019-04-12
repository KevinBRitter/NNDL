import pandas as pd

pd.set_option('display.max_columns', None)
raw_data = pd.read_csv("hw12data.csv")
print(raw_data.head())

raw_data.info(), raw_data.shape
print()

x1_mean = raw_data['Exam1 Score'].mean()
x2_mean = raw_data['Exam2 Score'].mean()
x3_mean = raw_data['Exam3 Score'].mean()
final_mean = raw_data['Final Score'].mean()


x1_std_dev = raw_data['Exam1 Score'].std()
x2_std_dev = raw_data['Exam2 Score'].std()
x3_std_dev = raw_data['Exam3 Score'].std()
final_std_dev = raw_data['Final Score'].std()

print("Exam1 mean: %6.3f" % x1_mean)
print("Exam2 mean: %6.3f" % x2_mean)
print("Exam3 mean: %6.3f" % x3_mean)
print("Final mean: %6.3f" % final_mean)
print()
print("Exam1 stdDev: %6.3f" % x2_std_dev)
print("Exam2 stdDev: %6.3f" % x2_std_dev)
print("Exam3 stdDev: %6.3f" % x3_std_dev)
print("Final stdDev: %6.3f" % final_std_dev)
print()

x1_count = 0
for i in raw_data['Exam1 Score']:
    j = int(i)
    if j > 70:
        x1_count += 1
print("Exam1 num > 70: %6.3f" % x1_count)
x1_percentage_above = (x1_count / 57)*100
print("Exam1 %% > 70: %6.3f" % x1_percentage_above)
print()

x2_count = 0
for i in raw_data['Exam2 Score']:
    j = int(i)
    if j > 70:
        x2_count += 1
print("Exam2 num > 70: %6.3f" % x2_count)
x2_percentage_above = (x2_count / 57)*100
print("Exam2 %% > 70: %6.3f" % x2_percentage_above)
print()

x3_count = 0
for i in raw_data['Exam3 Score']:
    j = int(i)
    if j > 70:
        x3_count += 1
print("Exam3 num > 70: %6.3f" % x3_count)
x3_percentage_above = (x3_count / 57)*100
print("Exam3 %% > 70: %6.3f" % x3_percentage_above)
print()

final_count = 0
for i in raw_data['Final Score']:
    j = int(i)
    if j > 70:
        final_count += 1
print("Final num > 70: %6.3f" % final_count)
final_percentage_above = (final_count / 57)*100
print("Final %% > 70: %6.3f" % final_percentage_above)
print()