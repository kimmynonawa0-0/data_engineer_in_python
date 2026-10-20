import pandas as pd

students = pd.DataFrame({
    'student': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'math':    [85, 92, 78, 88, 95, 70, 82, 90],
    'science': [88, 85, 80, 92, 90, 75, 85, 88],
    'english': [80, 88, 85, 82, 92, 78, 88, 85]
})

#Define a custom function score_range(column) that returns column.max() - column.min() — the range of scores.
#Print the range of the math column.
#Print the range of all three subject columns (math, science, english).
#Print the range and the median of all three subject columns, in that order.
#Then tell me: what shape will the output of #4 be — a scalar, a Series, or a DataFrame? And why?

def score_range(col):
    return col.max() - col.min()

print(f"score range for math: {students['math'].agg(score_range)}")
print("range of all subjects:\n", students[['math','science','english']].agg(score_range))
print("range and median of all subjects:\n", students[['math','science','english']].agg([score_range, 'median']))

