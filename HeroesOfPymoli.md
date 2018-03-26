

```python
import pandas as pd
import numpy as np
```


```python
# read data file into dataframe
filepath = "../resources/purchase_data.json"
purch_df = pd.read_json(filepath)
```


```python
# get unique number
player_count = purch_df["SN"].nunique()

# create data frame for player_count series
player_count_df = pd.DataFrame({'Total Players':[player_count]})
player_count_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>




```python
# count number of unique items
num_unique_items = purch_df['Item Name'].nunique()

# average purchase price
avg_price = purch_df["Price"].mean()

# total number of purchases
tot_purch = len(purch_df)

# total revenue
tot_revenue = purch_df["Price"].sum()

```


```python
# create dataframe with above series
purch_analysis_df = pd.DataFrame({'Total Revenue':[tot_revenue], 
                                  'Number of Purchases':[tot_purch], 
                                  'Average Price': [avg_price], 
                                  'Number of Unique Items':[num_unique_items]})

# organize the dataframe by rearranging the columns
purch_analysis_df = purch_analysis_df.round(2)[['Number of Unique Items', 
                                                'Average Price', 
                                                'Number of Purchases', 
                                                'Total Revenue']]
# display dataframe
purch_analysis_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>179</td>
      <td>2.93</td>
      <td>780</td>
      <td>2286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Gender Demographics

# create dataframe without duplicates
gender_df = purch_df.drop_duplicates(subset='SN')

# create total counts per gender
gender_group = gender_df['Gender'].value_counts()

# calculate percentage
gender_pct = gender_group / player_count * 100

# create df with above data
gender_grp_df = pd.DataFrame({'Total Count': gender_group, 'Percentage of Players': gender_pct}).round(2)
gender_grp_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>81.15</td>
      <td>465</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.45</td>
      <td>100</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.40</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Purchasing Analysis (Gender) 

# create variables to calculate values
purchCount = purch_df.groupby(["Gender"]).count()["Price"]
avgPurchPrice = purch_df.groupby(["Gender"]).mean()["Price"].round(2)
totPurchVal = purch_df.groupby(["Gender"]).sum()["Price"]
normTot = (totPurchVal / gender_grp_df["Total Count"]).round(2)

#create dataframe to hold all the values
genderAnalysis_df = pd.DataFrame({'Purchase Count':purchCount, 
                                  'Average Purchase Price':avgPurchPrice, 
                                  'Total Purchase Value': totPurchVal, 
                                  'Normalized Totals':normTot})

# organize dataframe
genderAnalysis_df = genderAnalysis_df[['Purchase Count', 
                                       'Average Purchase Price', 
                                       'Total Purchase Value', 
                                       'Normalized Totals']]

# display dataframe
genderAnalysis_df


```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>2.82</td>
      <td>382.91</td>
      <td>3.83</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>2.95</td>
      <td>1867.68</td>
      <td>4.02</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>3.25</td>
      <td>35.74</td>
      <td>4.47</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Age Demographics

# create unique users df
unique_users_df = purch_df.drop_duplicates("SN")

# create age groups and Label names
age_grps = [0.0, 9.9, 14.9, 19.9, 24.9, 29.9, 34.9, 39.9, 99.9]
grp_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

# assign the age range to each record/user
unique_users_df['Age Range'] = pd.cut(unique_users_df.Age, age_grps, include_lowest=True, labels=grp_names)

# get the counts of each age range
age_counts = unique_users_df['Age Range'].value_counts().sort_index()

# get the percentage of age counts of the total
age_pcts = (age_counts / player_count * 100).round(2)

# create dataframe with the specific data
age_demographics_df = pd.DataFrame({"Percentage of Players": age_pcts, "Total Count": age_counts})

# display dataframe
age_demographics_df


```

    C:\Users\Mike\Anaconda3\lib\site-packages\ipykernel_launcher.py:11: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      # This is added back by InteractiveShellApp.init_path()
    




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>3.32</td>
      <td>19</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>4.01</td>
      <td>23</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>17.45</td>
      <td>100</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>45.20</td>
      <td>259</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>15.18</td>
      <td>87</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>8.20</td>
      <td>47</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>4.71</td>
      <td>27</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>1.92</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Purchasing Analysis (Age)
purch_df['Age Range'] = pd.cut(purch_df.Age, age_grps, include_lowest=True, labels=grp_names)


# purchase count by age group
purchCount_age = purch_df.groupby(["Age Range"]).count()["Price"]

# average purchase price by age group
avgPurchPrice_age = purch_df.groupby(["Age Range"]).mean()["Price"].round(2)

# total purchase value by age group
totPurchVal_age = purch_df.groupby(["Age Range"]).sum()["Price"]

# Normalized totals by age group
normTot_age = (totPurchVal_age / age_demographics_df["Total Count"]).round(2)

# create dataframe to hold the data
ageAnalysis_df = pd.DataFrame({'Purchase Count':purchCount_age, 
                                  'Average Purchase Price':avgPurchPrice_age, 
                                  'Total Purchase Value': totPurchVal_age, 
                                  'Normalized Totals':normTot_age})

# organize dataframe
ageAnalysis_df = ageAnalysis_df[['Purchase Count', 
                                       'Average Purchase Price', 
                                       'Total Purchase Value', 
                                       'Normalized Totals']]

# display dataframe
ageAnalysis_df



```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Age Range</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>28</td>
      <td>2.98</td>
      <td>83.46</td>
      <td>4.39</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>35</td>
      <td>2.77</td>
      <td>96.95</td>
      <td>4.22</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>133</td>
      <td>2.91</td>
      <td>386.42</td>
      <td>3.86</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>336</td>
      <td>2.91</td>
      <td>978.77</td>
      <td>3.78</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>125</td>
      <td>2.96</td>
      <td>370.33</td>
      <td>4.26</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>64</td>
      <td>3.08</td>
      <td>197.25</td>
      <td>4.20</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>42</td>
      <td>2.84</td>
      <td>119.40</td>
      <td>4.42</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>17</td>
      <td>3.16</td>
      <td>53.75</td>
      <td>4.89</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Top Spenders
purchCount_SN = purch_df.groupby(["SN"]).count()["Price"]
avgPurchPrice_SN = purch_df.groupby(["SN"]).mean()["Price"].round(2)
totPurchVal_SN = purch_df.groupby(["SN"]).sum()["Price"]

topSpenders_df = pd.DataFrame({'Purchase Count':purchCount_SN, 
                                  'Average Purchase Price':avgPurchPrice_SN, 
                                  'Total Purchase Value': totPurchVal_SN})

topSpenders_df = topSpenders_df[['Purchase Count', 
                                 'Average Purchase Price', 
                                 'Total Purchase Value']]

topSpenders_df.sort_values("Total Purchase Value", ascending=False).head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>5</td>
      <td>3.41</td>
      <td>17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>4</td>
      <td>3.39</td>
      <td>13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>4</td>
      <td>3.18</td>
      <td>12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>3</td>
      <td>4.24</td>
      <td>12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3</td>
      <td>3.86</td>
      <td>11.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Most popular items
purchCount_Item = purch_df.groupby(["Item ID"]).count()["Price"]
avgPurchPrice_Item = purch_df.groupby(["Item ID"]).mean()["Price"].round(2)
totPurchVal_Item = purch_df.groupby(["Item ID"]).sum()["Price"]

topItems_df = pd.DataFrame({'Item Name': purch_df['Item Name'],
                            'Purchase Count':purchCount_Item, 
                            'Average Purchase Price':avgPurchPrice_Item, 
                            'Total Purchase Value': totPurchVal_Item})

topItems_df = topItems_df[['Item Name',
                           'Purchase Count',
                           'Average Purchase Price', 
                           'Total Purchase Value']]

topItems_df.sort_values("Purchase Count", ascending=False).head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>Stormfury Mace</td>
      <td>11.0</td>
      <td>2.35</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Thorn, Satchel of Dark Souls</td>
      <td>11.0</td>
      <td>2.23</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Shadow Strike, Glory of Ending Hope</td>
      <td>9.0</td>
      <td>2.07</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <td>Retribution Axe</td>
      <td>9.0</td>
      <td>1.24</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Piety, Guardian of Riddles</td>
      <td>9.0</td>
      <td>1.49</td>
      <td>13.41</td>
    </tr>
  </tbody>
</table>
</div>




```python
# most profitable
profit_df = pd.DataFrame({'Item Name': purch_df['Item Name'],
                          'Purchase Count':purchCount_Item,
                          'Item Price':purch_df['Price'],
                          'Total Purchase Value': totPurchVal_Item})

profit_df = profit_df[['Item Name',
                         'Purchase Count',
                         'Item Price', 
                         'Total Purchase Value']]

profit_df.sort_values("Total Purchase Value", ascending=False).head()

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>Alpha, Reach of Ending Hope</td>
      <td>9.0</td>
      <td>1.55</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Thorn, Conqueror of the Corrupted</td>
      <td>7.0</td>
      <td>2.04</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Rage, Legacy of the Lone Victor</td>
      <td>6.0</td>
      <td>4.32</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <td>Mercy, Katana of Dismay</td>
      <td>6.0</td>
      <td>4.37</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Spectral Diamond Doomblade</td>
      <td>8.0</td>
      <td>4.25</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>


