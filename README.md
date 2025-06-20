# Horse Racing Results Scraper & ML Dataset Builder

This project automates the extraction, cleaning, and structuring of historical horse racing results from [tab.com.au](https://tab.com.au) using custom scraping logic and machine learning-friendly formatting. It was built for predictive modeling and racing analytics using Python and custom APIs.

## Project Structure

```
.
├── extract-day.py       # API collector – fetches race result URLs
├── extract-data.py      # Data scraper – extracts structured data from URLs
├── comaine.py           # Combines monthly CSVs into one final dataset
├── racing-apis/         # Raw JSON files of race links per day
├── racing-data/         # Cleaned daily CSV files of race results
└── final_combined_racing_data.csv  # Final merged dataset (output)
```

## Features

- Automated Historical Scraping with retry logic and proxies  
- Date Range Support for fetching only required days
- JSON to CSV Parsing with structured formatting
- Ready for Machine Learning Training
- Handles:
  - Missing or malformed JSON
  - Failed API retries with logging
  - Previous runs resume without duplications

## How It Works

### 1. Collect Race URLs by Date
**`extract-day.py`**  
Fetches race metadata & result API links from each date in a defined range.

```bash
python extract-day.py
```

Outputs JSON files in `racing-apis/YYYY-MM/`.

### 2. Scrape and Clean Data
**`extract-data.py`**  
Loads the race result URLs from step 1, scrapes relevant race fields (horse, jockey, barrier, trainer, odds, finish), and saves daily structured CSVs.

```bash
python extract-data.py
```

Output: Cleaned daily CSVs in `racing-data/YYYY-MM/`.

### 3. Combine All Monthly Files
**`comaine.py`**  
Scans the `racing-data` directory and merges all daily CSVs into a single file.

```bash
python comaine.py
```

Final dataset: `final_combined_racing_data.csv`.

## Example Data Columns

- `Date`
- `Track`
- `Race Number`
- `Horse`
- `Jockey`
- `Trainer`
- `Barrier`
- `SP` (Starting Price / Odds)
- `Finish Position`
- `Race Distance`
- `Class`
- `Track Condition`
- `Weather`
- `Total Runners`

## Requirements

- Python 3.9+
- `pandas`
- `tls-client`  
  > Install using unofficial methods or custom wheels due to its non-standard distribution.

## Notes

- This script respects retry logic and error recovery.
- Proxy support is included and can be modified in `extract-day.py`.
- All scrapers are built with ethical scraping principles, targeting publicly available APIs.

## Model Note

Pretrained model files were not uploaded due to file size limitations.  
To use the full pipeline, please run the main notebook (`main.ipynb`) locally. It will automatically retrain the model from scratch using the combined dataset (`final_combined_racing_data.csv`).

## Author

**Mostafa Nasser**  
Specialist in scraping, automation, and ML pipelines  
[GitHub](https://github.com/xx36Mostafa)
