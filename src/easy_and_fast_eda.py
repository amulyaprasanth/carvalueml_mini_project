import os
import pandas as pd
import sweetviz as sv

# Read the training dataset
train = pd.read_csv("data/used_cars.csv")

# view the report 
report = sv.analyze(train)

# Create the directory if it doesn't exist
os.makedirs("dashboard", exist_ok=True)

# Create the whole report in the form of an html file inside the "dashboard" directory
report.show_html('dashboard/Report.html')
