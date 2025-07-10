#!/usr/bin/env python
# coding: utf-8

# # User Engagement Trends in Dognition
# 
# by Michelle Aguiar
# 
# ## Overview
# This case study uses SQL to analyze user engagement patterns within Dognition, a cognitive testing platform for dogs. The objective was to uncover when users are most active and identify the geographic regions with the
# highest engagement. Understanding these trends supports strategic decisions around communication timing, user segmentation, and regional outreach.
# 
# The analysis utilized data from the `complete_tests`, `dogs`, and `users` tables. 
# 
# **Key techniques included:**
# * Data cleaning and filtering to remove flagged users/dogs
# * Aggregation to track engagement by weekday and year
# * Timezone adjustments for accuracy in behavioral timing
# * Geographic segmentation to identify top markets

# In[1]:


get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('sql', 'mysql://studentuser:studentpw@localhost/dognitiondb')
get_ipython().run_line_magic('sql', 'USE dognitiondb')


# ## Engagement Peaks by Day of the Week
# 
# The analysis first explored test activity by day of the week to uncover behavioral trends. Using the `DAYOFWEEK()` function, weekday values were extracted, labeled, and aggregated to quantify completions by day. 
# 
# Results revealed **Sunday as the highest engagement day (~33,190 completions)** and Friday as the lowest.

# In[2]:


get_ipython().run_cell_magic('sql', '', "\n# Extract weekday from timestamp\nSELECT \n    created_at, \n    DAYOFWEEK(created_at) AS weekday_num\nFROM complete_tests\nLIMIT 49200;\n\n# Add weekday labels using CASE\nSELECT \n    created_at, \n    DAYOFWEEK(created_at) AS weekday_num,\n    CASE\n        WHEN DAYOFWEEK(created_at) = 1 THEN 'Su'\n        WHEN DAYOFWEEK(created_at) = 2 THEN 'Mo'\n        WHEN DAYOFWEEK(created_at) = 3 THEN 'Tu'\n        WHEN DAYOFWEEK(created_at) = 4 THEN 'We'\n        WHEN DAYOFWEEK(created_at) = 5 THEN 'Th'\n        WHEN DAYOFWEEK(created_at) = 6 THEN 'Fr'\n        WHEN DAYOFWEEK(created_at) = 7 THEN 'Sa'\n    END AS daylabel\nFROM complete_tests\nLIMIT 49200;\n\n# Aggregate test counts by daylabel\nSELECT \n    DAYOFWEEK(created_at) AS weekday_num,\n    COUNT(created_at) AS numtests,\n    CASE\n        WHEN DAYOFWEEK(created_at) = 1 THEN 'Su'\n        WHEN DAYOFWEEK(created_at) = 2 THEN 'Mo'\n        WHEN DAYOFWEEK(created_at) = 3 THEN 'Tu'\n        WHEN DAYOFWEEK(created_at) = 4 THEN 'We'\n        WHEN DAYOFWEEK(created_at) = 5 THEN 'Th'\n        WHEN DAYOFWEEK(created_at) = 6 THEN 'Fr'\n        WHEN DAYOFWEEK(created_at) = 7 THEN 'Sa'\n    END AS daylabel\nFROM complete_tests\nGROUP BY daylabel\nORDER BY numtests DESC;")


# Sunday had the highest number of test completions (~33,190), while Friday had the lowest.

# ## Data Cleansing to Improve Accuracy
# 
# To ensure data quality and relevance, records linked to users or dogs marked for exclusion were removed. After cleansing, only 34,121 out of 950,331 records met the quality threshold, creating a reliable baseline for subsequent analysis.

# In[3]:


get_ipython().run_cell_magic('sql', '', '\n# Total number of dogs linked to users before applying exclusion filters\nSELECT \n    COUNT(*) AS total_linked_dogs\nFROM dogs d\nINNER JOIN users u ON d.user_guid = u.user_guid;')


# In[4]:


get_ipython().run_cell_magic('sql', '', '\n# Count of unique dog_guid entries before cleaning\nSELECT \n    COUNT(DISTINCT dog_guid) AS unique_dogs\nFROM dogs d\nJOIN users u ON d.user_guid = u.user_guid;')


# In[5]:


get_ipython().run_cell_magic('sql', '', '\n# Count of valid unique dog_guid values (excluding flagged users and dogs)\nSELECT \n    COUNT(DISTINCT dog_guid) AS valid_unique_dogs\nFROM dogs d\nJOIN users u ON d.user_guid = u.user_guid\nWHERE (u.exclude IS NULL OR u.exclude = 0)\n  AND (d.exclude IS NULL OR d.exclude = 0);')


# Of the 950,331 dogs initially linked to users, 35,048 were unique, and 34,121 met the criteria for clean analysis. This refinement ensured that only unflagged and valid records were retained, improving the accuracy of downstream insights.

# ## Year-Over-Year Consistency in Engagement
# 
# The report evaluated whether weekly engagement trends remained stable across years. Cleaned test data was grouped by weekday and year, confirming that Sunday and Monday consistently showed the highest activity from 2013 to 2015.

# In[6]:


get_ipython().run_cell_magic('sql', '', "\n# Group cleaned test data by year and weekday to detect recurring patterns\nSELECT \n    DAYOFWEEK(c.created_at) AS dayasnum, \n    YEAR(c.created_at) AS year, \n    COUNT(c.created_at) AS numtests,\n    CASE \n        WHEN DAYOFWEEK(c.created_at) = 1 THEN 'Su'\n        WHEN DAYOFWEEK(c.created_at) = 2 THEN 'Mo'\n        WHEN DAYOFWEEK(c.created_at) = 3 THEN 'Tu'\n        WHEN DAYOFWEEK(c.created_at) = 4 THEN 'We'\n        WHEN DAYOFWEEK(c.created_at) = 5 THEN 'Th'\n        WHEN DAYOFWEEK(c.created_at) = 6 THEN 'Fr'\n        WHEN DAYOFWEEK(c.created_at) = 7 THEN 'Sa'\n    END AS daylabel\nFROM complete_tests c\nJOIN (\n    SELECT DISTINCT dog_guid\n    FROM dogs d\n    JOIN users u ON d.user_guid = u.user_guid\n    WHERE (u.exclude IS NULL OR u.exclude = 0)\n      AND (d.exclude IS NULL OR d.exclude = 0)\n) AS dogs_cleaned ON c.dog_guid = dogs_cleaned.dog_guid\nGROUP BY year, daylabel\nORDER BY year ASC, numtests DESC;")


# Consistent peaks on Sunday and Monday across 2013–2015.

# ## Adjusting Timestamps to Reflect Local Behavior
# 
# Because timestamps were recorded in UTC, a six-hour adjustment was applied to align activity to Central Time (UTC–6). This correction offered a more accurate reflection of user-local behavior. 
# 
# Alaska and Hawaii were excluded to maintain geographic consistency. 
# 
# The Sunday and Monday pattern remained consistent post-adjustment.

# In[7]:


get_ipython().run_cell_magic('sql', '', '\n# Convert UTC timestamps to Central Time (UTC-6)\nSELECT \n    created_at, \n    DATE_SUB(created_at, INTERVAL 6 HOUR) AS corrected_time\nFROM complete_tests\nLIMIT 100;')


# In[8]:


get_ipython().run_cell_magic('sql', '', "\n# Time-corrected engagement by weekday and year\nSELECT \n    DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL 6 HOUR)) AS dayasnum, \n    YEAR(c.created_at) AS year, \n    COUNT(c.created_at) AS numtests,\n    CASE\n        WHEN DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL 6 HOUR)) = 1 THEN 'Su'\n        WHEN DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL 6 HOUR)) = 2 THEN 'Mo'\n        WHEN DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL 6 HOUR)) = 3 THEN 'Tu'\n        WHEN DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL 6 HOUR)) = 4 THEN 'We'\n        WHEN DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL 6 HOUR)) = 5 THEN 'Th'\n        WHEN DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL 6 HOUR)) = 6 THEN 'Fr'\n        WHEN DAYOFWEEK(DATE_SUB(c.created_at, INTERVAL 6 HOUR)) = 7 THEN 'Sa'\n    END AS daylabel\nFROM complete_tests c\nJOIN (\n    SELECT DISTINCT dog_guid \n    FROM dogs d \n    JOIN users u ON d.user_guid = u.user_guid\n    WHERE (u.exclude IS NULL OR u.exclude = 0)\n      AND u.country = 'US'\n      AND u.state NOT IN ('HI', 'AK')\n      AND (d.exclude IS NULL OR d.exclude = 0)\n) AS dogs_cleaned ON c.dog_guid = dogs_cleaned.dog_guid\nGROUP BY year, daylabel\nORDER BY year ASC, FIELD(daylabel, 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su');")


# The Sunday/Monday engagement pattern holds even after time-zone adjustment.

# ## Identifying Top Performing Regions
# 
# The final phase segmented engagement by U.S. state and country to identify top-performing regions. California, New York, and Texas led U.S. activity. Internationally, the U.S., Canada, and the U.K. were the most engaged markets, suggesting opportunities for targeted outreach in English-speaking regions.

# In[9]:


get_ipython().run_cell_magic('sql', '', "\n# Top 5 U.S. states by unique users\nSELECT \n    dogs_cleaned.state AS state, \n    COUNT(DISTINCT dogs_cleaned.user_guid) AS numusers\nFROM complete_tests c\nJOIN (\n    SELECT DISTINCT dog_guid, u.user_guid, u.state\n    FROM dogs d\n    JOIN users u ON d.user_guid = u.user_guid\n    WHERE (u.exclude IS NULL OR u.exclude = 0)\n      AND u.country = 'US'\n      AND (d.exclude IS NULL OR d.exclude = 0)\n) AS dogs_cleaned ON c.dog_guid = dogs_cleaned.dog_guid\nGROUP BY state\nORDER BY numusers DESC\nLIMIT 5;")


# In[10]:


get_ipython().run_cell_magic('sql', '', '\n# Top 10 countries by engagement\nSELECT dogs_cleaned.country AS country, COUNT(DISTINCT dogs_cleaned.user_guid) AS numusers FROM complete_tests c \nJOIN(\n    SELECT DISTINCT dog_guid, u.user_guid, u.country \n    FROM dogs d JOIN users u ON d.user_guid=u.user_guid\n    WHERE ((u.exclude IS NULL OR u.exclude=0)\n           AND (d.exclude IS NULL OR d.exclude=0))) AS dogs_cleaned ON c.dog_guid=dogs_cleaned.dog_guid\nGROUP BY country\nORDER BY numusers DESC \nLIMIT 10;')


# California and New York lead U.S. engagement. Internationally, the U.S., Canada, and U.K. are top markets.

# ## Key Insights
# 
# * User activity consistently peaks on Sundays and Mondays.
# * Friday consistently shows the lowest engagement.
# * Weekly usage patterns are stable across years and time zones.
# * High engagement is concentrated in California, New York, and English-speaking countries.
# 
# ## Recommendations
# 
# To capitalize on peak engagement periods, it is recommended that Dognition schedule communications and campaigns for **Sundays** and **Mondays**, when user activity is at its highest. System maintenance and downtime should be carefully avoided on weekends, particularly Sundays, to prevent service disruptions during high-traffic periods.
# 
# Marketing resources should be concentrated in the platform’s top-performing regions: California, New York, and English-speaking countries such as the United States, Canada, the United Kingdom, and Australia. These areas consistently show higher levels of user engagement and present opportunities for deeper outreach.
# 
# Continuous monitoring of usage trends is advised to ensure alignment with user behavior over time. Lastly, geographic areas with low engagement should be investigated further, as they may reveal untapped markets or signal barriers to access that can be addressed strategically.
