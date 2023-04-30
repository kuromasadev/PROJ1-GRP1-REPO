## Yelp Dataset Extraction

Metadata

> A trove of reviews, businesses, users, tips, and check-in data!

#### About Dataset 

***\*Context\****

> This dataset is a subset of Yelp's businesses, reviews, and user data. It was originally put together for the Yelp Dataset Challenge which is a chance for students to conduct research or analysis on Yelp's data and share their discoveries. In the most recent dataset you'll find information about businesses across 8 metropolitan areas in the USA and Canada.

**Content**

This dataset contains five JSON files and the user agreement.

More information about those files can be found here: https://www.yelp.com/dataset

Downloaded from: https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset 

Note that for this repo, the contents were:

1. Downloaded from Kaggle
2. Extracted as-is
3. Run the 

## Import Dependencies

``` python
import pandas as pd
import json 
import chardet
```

#### Testing the Encoding

``` python
# Open a file in binary mode and read the first megabyte
with open("../YELP/archive/yelp_academic_dataset_business.json", "rb") as f:
    data = f.read(1000000)

encoding = chardet.detect(data)['encoding']

print("The encoding of the file set is "+encoding +".")
```

The encoding of the file set is utf-8.

#### Extracting the desired cities (Pittsburg) and (Charlotte) from set

```python
# Setup definition to read through all the files

def filter_by_city(input_file):
    # Open the input file and read the data
    with open(input_file, 'r', encoding='utf-8') as f:
        # Read the contents of the file into a string
        contents = f.read()

    # Split the contents by newlines, as each JSON object should be on a separate line
    contents = contents.strip().split('\n')

    # Load each JSON object from the string
    data = [json.loads(obj) for obj in contents]

    # Filter the data to include only entries where the 'city' field is 'Philadelphia' or 'Charlotte'
    filtered_data = [entry for entry in data if entry.get('city') in ['Philadelphia', 'Charlotte']]

    return filtered_data
```

Per the kaggle download: 

![](/images/yelp_zipformat.PNG)

```python
input_files = ['./archive/yelp_academic_dataset_business.json',
               './archive/yelp_academic_dataset_checkin.json',
               './archive/yelp_academic_dataset_review.json',
               './archive/yelp_academic_dataset_tip.json',
               './archive/yelp_academic_dataset_user.json']

# Iterate over the list of input files and filter each file
for input_file in input_files:
    filtered_data = filter_by_city(input_file)

    # Write the filtered data to a new JSON file
    output_file = input_file.replace('.json', '_proj1filtered.json')
    with open(output_file, 'w', encoding='ascii') as f:
        json.dump(filtered_data, f, ensure_ascii=True, indent=4)
```







