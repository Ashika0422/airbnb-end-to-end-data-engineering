import os
import sys

print("=" * 60)
print("AIRBNB DATA ENGINEERING PIPELINE")
print("=" * 60)

os.system(f'"{sys.executable}" src/ingestion.py')
os.system(f'"{sys.executable}" src/cleaning.py')
os.system(f'"{sys.executable}" src/transformation.py')
os.system(f'"{sys.executable}" src/validation.py')
os.system(f'"{sys.executable}" src/database.py')
os.system(f'"{sys.executable}" src/analysis.py')
os.system(f'"{sys.executable}" src/statistical_analysis.py')
os.system(f'"{sys.executable}" src/ml_model.py')

print("=" * 60)
print("PIPELINE COMPLETED")
print("=" * 60)
