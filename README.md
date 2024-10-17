# Research on Natural Disasters | Risk Control Organization- SafeHorizon🌪️

## Introduction 


I used this dataset, retrieved via the API Disaster SAFE, which can be found at https://dashboard.disastercheckin.app/documentation, to enhance my skills in data cleaning, analysis, and problem-solving. 
Throughout the process, I applied various techniques to ensure the data was accurate and meaningful for analysis. 

This project involved developing a business model based on the data insights, with a focus on practical applications and strategic decision-making. Working independently, I handled each stage, from research to technical execution, showcasing my ability to work with real-world data and draw actionable conclusions.

## Objective of the Analysis


My objective was to creatively and strategically approach the data cleaning process for a disorganized dataset. Focusing on the top natural disaster occurring worldwide on the past month, as well the top countries most affected by them. 
I developed a hypothesis focused on identifying countries vulnerable to natural disasters, aiming to help prevent them and protect communities. This hypothesis guided my data wrangling efforts. 

The overall goal of the analysis was to ensure data accuracy and integrity while identifying key trends and patterns in disaster occurrence and severity. By extracting actionable insights, I aimed to inform a risk management strategy that addresses these vulnerabilities, driving informed decision-making and supporting effective disaster prevention and community protection initiatives.

## Working Hypothesis


**Hypothesis 1**: *"The prevalence of certain disaster types, such as floods, is significantly associated with specific geographical and climatic conditions, particularly in warm and dry zones"* 

**Supporting Ideas**:
As the Southern Hemisphere enters its warmest seasons while the Northern Hemisphere moves into winter, we observe a predominance of fires due to extremely high temperatures in southern regions.
The rise in global temperatures, combined with less rainfall and increased dryness, creates ideal conditions for fires. 

This correlation suggests that the frequency of fires may be linked to climate change, as rising temperatures dry out vegetation and decrease humidity levels. (More information can be found at https://wmo.int/media/news/global-temperature-record-streak-continues-climate-change-makes-heatwaves-more-extreme, sources by World Meteorological Organization)


**Hypothesis 2**: *"The countries most frequently affected by natural disasters are not necessarily the same as those experiencing the highest severity of incidents, indicating a complex relationship between disaster occurrence and impact"*

**Supporting Ideas**:


•	**Difference Between Frequency and Severity**: Some countries may experience a high number of natural disasters (ex:. frequent storms or floods), but the severity and impact of these events can vary greatly. In contrast, other countries may face fewer disasters, but when they do occur, they result in more severe damage, higher death tolls, or greater economic disruption.


•	**Underlying Factors**: The relationship between disaster frequency and severity is influenced by various factors such as geographical location, infrastructure quality, economic preparedness, and response capacity. For example, countries with good and strong infrastructure and efficient disaster response systems may experience frequent disasters but can mitigate the impact, while others with limited resources may suffer significantly from fewer but more destructive incidents.


•	**Global Disparities**: Wealthier nations may experience fewer casualties and less severe damage due to better preparedness and resilience strategies, while developing nations might be hit harder by single events due to fragile infrastructure and limited resources.

## Risk Control Organization- What is?
A Risk Control Organization is an entity focused on identifying, assessing, and mitigating risks that threats people, infrastructure, and communities. 
In the context of natural disasters, its primary goal is to minimize the exposure of populations to these risks by implementing proactive strategies and enhancing disaster preparedness.

In summary, a Risk Control Organization plays a crucial role in disaster prevention and management by studying risks, improving infrastructure, enhancing community safety, and reducing overall vulnerability to natural disasters. With this project my company wants to implement better contingency planning to countries that need prevention like anti sismic houses, better forest cleaning in danger areas, coast protection for flooding, and more.

## Data Cleaning and Preparation
In order to get enough data to draw accurate and truthful insights I made 60 requests to the chosen API Disasters SAFE. Each request made concerns one page of information, ended up with an initial data set with 1500 rows × 12 columns. 
With big pieces of data comes also an intense process of cleaning so let’s break it down step by step.

1.	**Dropped Unnecessary columns**: I analysed the original data set regarding my hypotheses and dropped the columns that were unnecessary for my insights. Therefore, I chose to eliminate 'url', 'id', '_deletedAt', 'latlong', 'guid', 'description', 'updatedAt’, 'magnitudeUnit'.

2.	**Standardization of Columns**: I renamed the columns for better understanding of its meaning and the data that was being shown. I got this by doing the following: df.columns=["incident", "alert_level", "alert_score", "date_incident", "magnitude_value", "type", "country", "severity_score"].

   
3.	**Data Cleaning** 🧹


a.	**Incident**: Initially called ‘title’, I started by iterating over this column to get the name of the disaster that occurred in each row. To be able to do it I transformed the column title into a list.

I used a for loop to iterate to each row first, then impose conditions inside the loop. If the word I was looking for was present in that row, it would be added to the empty list I created before for this purpose called incidents.  So, after this I got a list with only the incidents presents in the data Frame. Lastly, I just assigned the new cleaned list to the title columns substituting the values for a better understanding of the data.

b.	**Alert_level**: To this column I started by checking the NaN’s, which was shown to not exist, so I proceed to the next column.

c.	**Alert_score & Severity_score**: Alert score was also standardized and well cleaned; however, I decide to create a new column based on this one. I wanted to make it as simple to read as possible as 0,1 and 2 didn’t specify what was the meaning behind it. So in the new column called “severity_score” I associate the values with rankings (0- minor, 1- moderate, 2-severe). To get this results I created a dictionary called mapping_severity= {0: “minor”, 1: “moderate”, 2: “severe”}, then replace the integers with this corresponding values by doing df[“severity_score”]= df[“severity_score”].replace(mapping_severity).

d.	**Date_incident**: Initially called “createdAt”, it had date and specific hour mixed for each incident. Since I only needed the specific date to be able to identify which period of time I was analysing I decided to use Regex. Started by importing the library with import re and defining the pattern I wanted to search. Similar to the incident column I used a for loop to iterate over each row of the column “createdAt”. So, resuming it, in each row I searched for the date pattern “yyyy/mm/dd”. If that pattern was found in the row, it would be added to the empty list I created prior called dates. 

Having my list with the dates, I replaced the cleaned values over the “createdAt” now called date_incident.

e.	**Magnitude_value & Type**: Similar to alert_level, I started by checking the NaN’s using the method isna().sum(), which was shown to not exist, so I proceed to the next column

f.	**Country**: Initially calls “landCountry”, I checked the NaN’s which were significantly high considering that in the biggening I started with 250 rows. However as stated before, I decided to get more data in order to deal with the NaN’s. After requesting the 60 pages I was able to drop the NaN values without missing big chunks of significant data since the countries column was my priority and was not possible to fill it with the fillna() method.


## EDA- Visualization 📊
After some research on possible libraries and graphics I could use to present my data. I came across plotly.express and geopandas which allows easy manipulation and analysis of geographic data in Python. 

I follow the steps to install this libraries, starting by using **“!pip install geopandas”** since I did not had this library installed previously and then I imported **plotly.express**. 


## Conclusion

This project highlighted the complex nature of natural disasters, showing how critical it is to consider both the frequency of these events and their severity. By analyzing the data, I was able to identify important trends that support the hypotheses and offer valuable insights for improving risk control strategies. These findings can help guide decisions aimed at reducing vulnerability and enhancing community resilience in high-risk regions.

For more detailed information please refer to the documentation also added in this repo :)
