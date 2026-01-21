# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
medium_articles = dataiku.Dataset("medium_articles")
medium_articles_df = medium_articles.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

r_df = medium_articles_df # For this sample code, simply copy input to output


# Write recipe outputs
r = dataiku.Dataset("r")
r.write_with_schema(r_df)
