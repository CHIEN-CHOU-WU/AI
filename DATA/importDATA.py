import psycopg2
import pandas as pd

source = 'studentperformance'
conn = psycopg2.connect("host=localhost dbname=ai user=postgres password=musicgood123")
cur = conn.cursor()

data = pd.read_csv('StudentPerformanceData\student-mat.csv', sep=';')

print(data.columns)
	