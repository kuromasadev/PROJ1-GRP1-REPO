## Yelp Dataset Extraction

**Metadata**

> A trove of reviews, businesses, users, tips, and check-in data!



#### About Dataset 

**Context**

> This dataset is a subset of Yelp's businesses, reviews, and user data. It was originally put together for the Yelp Dataset Challenge which is a chance for students to conduct research or analysis on Yelp's data and share their discoveries. In the most recent dataset you'll find information about businesses across 8 metropolitan areas in the USA and Canada.

**Content**

This dataset contains five JSON files and the user agreement.

More information about those files can be found here: https://www.yelp.com/dataset

Downloaded from: https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset 

Note that for this repo, the contents were:

1. Downloaded from Kaggle
2. Extracted as-is
3. Jupyter notebook in this folder goes over the steps to produce filtered data



Two methods were used to extract this data: 

#### Simplified

> Involves reading original large json into pandas and then exporting filtered content into csv

[Simplified Jupyter nb](/proj1_yelp_data_simplified.ipynb)

#### Complex 

> Involves extracting the same filter across the rest of the datasets provided by Yelp.

[Complex Jupyter nb](/proj1_yelp_data_complex.ipynb)





