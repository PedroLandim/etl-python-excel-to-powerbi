import pandas as pd
from data_profiling import ProfileReport

df = pd.read_csv("./data/data.csv")

profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
profile.to_file("report.html")