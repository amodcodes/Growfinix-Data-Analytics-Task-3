# Customer Demographic Analysis (Internship Task 3)

## Objective
Analyze Tour Enquiries to identify popular travel destinations and understand customers by age and annual income. Create basic charts using Python, Pandas, and Matplotlib.

## Important dataset note
The internship PDF describes a CSV containing thousands of Tour Enquiries but does not attach the original dataset. Therefore, `data/tour_enquiries.csv` is a **synthetic practice dataset** created for this runnable demonstration. Do not present its findings as actual company/customer findings. Replace it with the official dataset when provided.

## Project structure
```text
Customer_Demographic_Analysis/
├── data/
│   └── tour_enquiries.csv
├── outputs/
│   ├── popular_destinations.png
│   ├── age_distribution.png
│   ├── age_groups.png
│   ├── income_brackets.png
│   ├── cleaned_tour_enquiries.csv
│   └── summary CSV files
├── analysis.py
├── requirements.txt
└── README.md
```

## Requirements
- Python 3.9+
- pandas
- matplotlib
- numpy

## Run on Windows
1. Install Python from https://www.python.org/downloads/ and select **Add Python to PATH**.
2. Extract this ZIP.
3. Open the project folder in VS Code.
4. Open Terminal > New Terminal.
5. Run:
   ```bash
   python -m pip install -r requirements.txt
   python analysis.py
   ```
6. Charts and cleaned files are saved in the `outputs` folder.

## Analysis steps
1. Load CSV with Pandas.
2. Inspect rows, columns, data types, and missing values.
3. Remove duplicate enquiry IDs.
4. Fill missing age and income with their median; mark missing destination as Unknown.
5. Create age groups and income brackets.
6. Count popular destinations and demographic groups.
7. Plot destination bar chart, age histogram, age-group bar chart, and income-bracket bar chart.
8. Export cleaned data and summary tables.

## Sample run summary
These figures are based only on the included synthetic practice dataset:
- Raw rows: 1503
- Rows after duplicate removal: 1500
- Average customer age: 34.1 years
- Median annual income: INR 64,537
- Most frequent destination: Goa (280 enquiries)
- Largest age group: 26-35
- Largest income bracket: 60k-100k

## Limitations
The dataset is synthetic and randomly generated for learning. Results are illustrative, not representative of real customers. The original PDF does not specify the exact CSV schema, so column names here are a practical example.
