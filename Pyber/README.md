

```python
# Three observable trends from the below data:
#     1) There are more rides in the urban city type
#     2) The fares are generally more expensive in the rural city type
#     3) As a company, it is best to work in the urban city type.  However, it is less profitable per ride, and 
#        potentially not as profitable for individual drivers due to significantly more drivers.
```


```python
# dependencies
#%matplotlib notebook
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
```


```python
filepathCity_Data = '../resources/city_data.csv'
filepathRide_Data = "../resources/ride_data.csv"

cityData_df = pd.read_csv(filepathCity_Data)
rideData_df = pd.read_csv(filepathRide_Data)
cityData_df.head(10)
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
      <th>city</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nguyenbury</td>
      <td>8</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>East Douglas</td>
      <td>12</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>West Dawnfurt</td>
      <td>34</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rodriguezburgh</td>
      <td>52</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>5</th>
      <td>South Josephville</td>
      <td>4</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>6</th>
      <td>West Sydneyhaven</td>
      <td>70</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Travisville</td>
      <td>37</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Torresshire</td>
      <td>70</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Lisaville</td>
      <td>66</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>




```python
rideData_df.head()
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
      <th>city</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sarabury</td>
      <td>2016-01-16 13:49:27</td>
      <td>38.35</td>
      <td>5403689035038</td>
    </tr>
    <tr>
      <th>1</th>
      <td>South Roy</td>
      <td>2016-01-02 18:42:34</td>
      <td>17.49</td>
      <td>4036272335942</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Wiseborough</td>
      <td>2016-01-21 17:35:29</td>
      <td>44.18</td>
      <td>3645042422587</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spencertown</td>
      <td>2016-07-31 14:53:22</td>
      <td>6.87</td>
      <td>2242596575892</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Nguyenbury</td>
      <td>2016-07-09 04:42:44</td>
      <td>6.28</td>
      <td>1543057793673</td>
    </tr>
  </tbody>
</table>
</div>




```python
# set variables for merging
avg_fare_city = rideData_df.groupby(["city"]).mean()["fare"].round(2)
tot_num_rides_city = rideData_df.groupby(['city']).count()["fare"]
tot_num_drivers_city = cityData_df.groupby(['city']).sum()['driver_count']
city_type_df = cityData_df[['city', 'type']]
#city_type = city_type.set_index('city')
city_type_df.sort_values('city', ascending=True).head()
#type(city_type)
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
      <th>city</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>65</th>
      <td>Alvarezhaven</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Alyssaberg</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>94</th>
      <td>Anitamouth</td>
      <td>Suburban</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Antoniomouth</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Aprilchester</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>




```python
# finds duplicate city rows
pd.concat(g for _, g in cityData_df.groupby("city") if len(g) > 1)

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
      <th>city</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>84</th>
      <td>Port James</td>
      <td>15</td>
      <td>Suburban</td>
    </tr>
    <tr>
      <th>100</th>
      <td>Port James</td>
      <td>3</td>
      <td>Suburban</td>
    </tr>
  </tbody>
</table>
</div>




```python
# adds the two rows together 
cityData_df = cityData_df.groupby(['city', 'type'])['driver_count'].sum().reset_index()

# verifies rows were combined as expected
cityData_df.loc[cityData_df['city'] == "Port James"]
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
      <th>city</th>
      <th>type</th>
      <th>driver_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>72</th>
      <td>Port James</td>
      <td>Suburban</td>
      <td>18</td>
    </tr>
  </tbody>
</table>
</div>




```python
# convert series into dataframes
avg_fare_city_df = pd.DataFrame(avg_fare_city)
tot_num_rides_city_df = pd.DataFrame(tot_num_rides_city)

```


```python
# merge city data with avg fare per city, and clean
cityData_merged = pd.merge(avg_fare_city_df,cityData_df, left_index = True, right_on='city', how='outer')
cityData_merged = cityData_merged.rename(index=str, columns={"fare": "Average Fare", 
                                                             "type":"City Type", 
                                                             "driver_count": "Total Driver Count", 
                                                             "city": "City"})

# merge clean city data with total number of rides per city, and clean
cityData_merged = pd.merge(tot_num_rides_city_df,cityData_merged, left_index = True, right_on='City', how='outer')
cityData_merged = cityData_merged.rename(index=str, columns={"fare": "Total Number of Rides", 
                                                             "type":"City Type", 
                                                             "driver_count": "Total Driver Count", 
                                                             "city": "City"})

# organizing
cityData_merged = cityData_merged[["City", "City Type", "Total Driver Count", 
                                   "Average Fare", "Total Number of Rides"]]

# set the city as the index
cityData_merged = cityData_merged.set_index('City')

# display merged table
cityData_merged.head()


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
      <th>City Type</th>
      <th>Total Driver Count</th>
      <th>Average Fare</th>
      <th>Total Number of Rides</th>
    </tr>
    <tr>
      <th>City</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alvarezhaven</th>
      <td>Urban</td>
      <td>21</td>
      <td>23.93</td>
      <td>31</td>
    </tr>
    <tr>
      <th>Alyssaberg</th>
      <td>Urban</td>
      <td>67</td>
      <td>20.61</td>
      <td>26</td>
    </tr>
    <tr>
      <th>Anitamouth</th>
      <td>Suburban</td>
      <td>16</td>
      <td>37.32</td>
      <td>9</td>
    </tr>
    <tr>
      <th>Antoniomouth</th>
      <td>Urban</td>
      <td>21</td>
      <td>23.62</td>
      <td>22</td>
    </tr>
    <tr>
      <th>Aprilchester</th>
      <td>Urban</td>
      <td>49</td>
      <td>21.98</td>
      <td>19</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.set()

# urban scatter
urbanData = cityData_merged.loc[cityData_merged['City Type'] == "Urban"]
plt.scatter(urbanData['Total Number of Rides'], 
            urbanData['Average Fare'], 
            s=urbanData['Total Driver Count']*10, 
            color='lightcoral', 
            edgecolor = 'black',
            alpha=.75,
            label="Urban");

# suburban scatter
suburbanData = cityData_merged.loc[cityData_merged['City Type'] == "Suburban"]
plt.scatter(suburbanData['Total Number of Rides'], 
            suburbanData['Average Fare'], 
            s=suburbanData['Total Driver Count']*10, 
            color='lightskyblue', 
            edgecolor = 'black',
            alpha=.75,
            label="Suburban");

# rural scatter
ruralData = cityData_merged.loc[cityData_merged['City Type'] == "Rural"]
plt.scatter(ruralData['Total Number of Rides'], 
            ruralData['Average Fare'], 
            s=ruralData['Total Driver Count']*10, 
            color='gold', 
            edgecolor = 'black',
            alpha=.75,
            label="Rural");

plt.title("Pyber: Ride Sharing Data (2016)")
plt.xlabel('Total Number of Rides')
plt.ylabel('Average Fare')
#plt.legend(loc= "upper right")
lgnd = plt.legend(loc="upper right", fontsize=10)
lgnd.legendHandles[0]._sizes = [30]
lgnd.legendHandles[1]._sizes = [30]
lgnd.legendHandles[2]._sizes = [30]

plt.show()

```


![png](output_9_0.png)



```python
cityData_merged.head()
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
      <th>City Type</th>
      <th>Total Driver Count</th>
      <th>Average Fare</th>
      <th>Total Number of Rides</th>
    </tr>
    <tr>
      <th>City</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alvarezhaven</th>
      <td>Urban</td>
      <td>21</td>
      <td>23.93</td>
      <td>31</td>
    </tr>
    <tr>
      <th>Alyssaberg</th>
      <td>Urban</td>
      <td>67</td>
      <td>20.61</td>
      <td>26</td>
    </tr>
    <tr>
      <th>Anitamouth</th>
      <td>Suburban</td>
      <td>16</td>
      <td>37.32</td>
      <td>9</td>
    </tr>
    <tr>
      <th>Antoniomouth</th>
      <td>Urban</td>
      <td>21</td>
      <td>23.62</td>
      <td>22</td>
    </tr>
    <tr>
      <th>Aprilchester</th>
      <td>Urban</td>
      <td>49</td>
      <td>21.98</td>
      <td>19</td>
    </tr>
  </tbody>
</table>
</div>




```python
# total fares by city
totFares_city = rideData_df.groupby(['city']).sum()['fare']
totFares_city_df = pd.DataFrame(totFares_city)

# merge with city type
cityData_merged = pd.merge(totFares_city_df,cityData_merged, left_index = True, right_index= True, how='outer')
cityData_merged = cityData_merged.rename(index=str, columns={"fare": "Total Fares"})
cityData_merged.head()

#totFares_city
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
      <th>Total Fares</th>
      <th>City Type</th>
      <th>Total Driver Count</th>
      <th>Average Fare</th>
      <th>Total Number of Rides</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alvarezhaven</th>
      <td>741.79</td>
      <td>Urban</td>
      <td>21</td>
      <td>23.93</td>
      <td>31</td>
    </tr>
    <tr>
      <th>Alyssaberg</th>
      <td>535.85</td>
      <td>Urban</td>
      <td>67</td>
      <td>20.61</td>
      <td>26</td>
    </tr>
    <tr>
      <th>Anitamouth</th>
      <td>335.84</td>
      <td>Suburban</td>
      <td>16</td>
      <td>37.32</td>
      <td>9</td>
    </tr>
    <tr>
      <th>Antoniomouth</th>
      <td>519.75</td>
      <td>Urban</td>
      <td>21</td>
      <td>23.62</td>
      <td>22</td>
    </tr>
    <tr>
      <th>Aprilchester</th>
      <td>417.65</td>
      <td>Urban</td>
      <td>49</td>
      <td>21.98</td>
      <td>19</td>
    </tr>
  </tbody>
</table>
</div>




```python
#total fares by city type
labels = ['Urban', 'Suburban', 'Rural']
#totalFares = rideData_df.groupby(["type"]).sum()["fare"]
#totalFares

```


```python
pctFaresType = pd.DataFrame(cityData_merged.groupby(['City Type']).sum()['Total Fares'])
pctFaresType
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
      <th>Total Fares</th>
    </tr>
    <tr>
      <th>City Type</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rural</th>
      <td>4255.09</td>
    </tr>
    <tr>
      <th>Suburban</th>
      <td>19317.88</td>
    </tr>
    <tr>
      <th>Urban</th>
      <td>40078.34</td>
    </tr>
  </tbody>
</table>
</div>




```python
type(pctFaresType)
```




    pandas.core.frame.DataFrame




```python
pctFaresType.index
```




    Index(['Rural', 'Suburban', 'Urban'], dtype='object', name='City Type')




```python
colors = ["gold", "lightskyblue", "lightcoral"]

explode = [0,0,0.1]

plt.pie(pctFaresType, labels=pctFaresType.index, autopct = "%1.2f%%", colors = colors, explode = explode, 
        shadow = True, startangle = 90)

plt.axis('equal')
plt.title("% of Total Fares by City Type")

plt.show()
```


![png](output_16_0.png)



```python
pctRidesType = pd.DataFrame(cityData_merged.groupby(['City Type']).sum()['Total Number of Rides'])
pctRidesType
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
      <th>Total Number of Rides</th>
    </tr>
    <tr>
      <th>City Type</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rural</th>
      <td>125</td>
    </tr>
    <tr>
      <th>Suburban</th>
      <td>625</td>
    </tr>
    <tr>
      <th>Urban</th>
      <td>1625</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.pie(pctRidesType, labels=pctRidesType.index, autopct = "%1.2f%%", colors = colors, explode = explode, 
        shadow = True, startangle = 90)

plt.axis('equal')
plt.title("% of Total Rides by City Type")

plt.show()
```


![png](output_18_0.png)



```python
pctDriversType = pd.DataFrame(cityData_merged.groupby(['City Type']).sum()['Total Driver Count'])
pctDriversType
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
      <th>Total Driver Count</th>
    </tr>
    <tr>
      <th>City Type</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rural</th>
      <td>104</td>
    </tr>
    <tr>
      <th>Suburban</th>
      <td>638</td>
    </tr>
    <tr>
      <th>Urban</th>
      <td>2607</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.pie(pctDriversType, labels=pctDriversType.index, autopct = "%1.2f%%", colors = colors, explode = explode, 
        shadow = True, startangle = 90)

plt.axis('equal')
plt.title("% of Total Drivers by City Type")

plt.show()
```


![png](output_20_0.png)

