# Corona_Detect_App
Corona_Detect_App is a command line based app with json scraping code to detect current covid effected patients in all over the world.Corona_Detect_App is a simple project initiative from me in **Hackerearth : Covid19 Hackathon** which is dedicated to the covid crisis.

# Installation
```python
pip3 install -r requirements.txt 
```
# Extracted Data
**CovidScraper** is a **Spider inside the Corona_Detect_App**, which will show table data. You can run it using **scrapy runspider CovidScraper.py** : 
```shell
>> scrapy runspider CovidScraper.py

2020-04-12 19:19:09 [protego] DEBUG: Rule at line 16 without any user agent to enforce it on.
2020-04-12 19:19:10 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.worldometers.info/coronavirus/#countries> (referer: None)
[              Country,Other  TotalCases NewCases  TotalDeaths NewDeaths  TotalRecovered  ActiveCases  Serious,Critical  Tot Cases/1M pop  Deaths/1M pop  TotalTests  Tests/ 1M pop
0                     World     1796414  +16,671     110030.0    +1,251        412102.0      1274282           50533.0            230.00           14.1         NaN            NaN
1                       USA      533470     +591      20595.0       +18         30523.0       482352           11471.0           1612.00           62.0   2696143.0         8145.0
2                     Spain      166019   +2,992      16972.0      +366         62391.0        86656            7371.0           3551.00          363.0    355000.0         7593.0
3                     Italy      152271      NaN      19468.0       NaN         32534.0       100269            3381.0           2518.00          322.0    963473.0        15935.0
4                    France      129654      NaN      13832.0       NaN         26391.0        89431            6883.0           1986.00          212.0    333807.0         5114.0
5                   Germany      125452      NaN       2871.0       NaN         57400.0        65181            4895.0           1497.00           34.0   1317887.0        
```

**CovidjsonScraper** is a full command line based script inside **Corona_Detect_App** , which will show data in json format , You can run it using **python3 CovidjsonScraper.py** :

```shell
>> python3 CovidjsonScraper.py

╔
      ::::::::   ::::::::  :::     ::: ::::::::::: :::::::::      :::     ::::    :::     :::     :::     :::   ::: ::::::::: :::::::::: ::::::::: 
    :+:    :+: :+:    :+: :+:     :+:     :+:     :+:    :+:   :+: :+:   :+:+:   :+:   :+: :+:   :+:     :+:   :+:      :+:  :+:        :+:    :+: 
   +:+        +:+    +:+ +:+     +:+     +:+     +:+    +:+  +:+   +:+  :+:+:+  +:+  +:+   +:+  +:+      +:+ +:+      +:+   +:+        +:+    +:+  
  +#+        +#+    +:+ +#+     +:+     +#+     +#+    +:+ +#++:++#++: +#+ +:+ +#+ +#++:++#++: +#+       +#++:      +#+    +#++:++#   +#++:++#:    
 +#+        +#+    +#+  +#+   +#+      +#+     +#+    +#+ +#+     +#+ +#+  +#+#+# +#+     +#+ +#+        +#+      +#+     +#+        +#+    +#+    
#+#    #+# #+#    #+#   #+#+#+#       #+#     #+#    #+# #+#     #+# #+#   #+#+# #+#     #+# #+#        #+#     #+#      #+#        #+#    #+#     
########   ########      ###     ########### #########  ###     ### ###    #### ###     ### ########## ###    ######### ########## ###    ###   v1.0
		
		>>> Press 1 : Covid Data According Gender In json file
		>>> Press 2 : Covid Data FRom District of India IN json File
		
>>> 1
```
File will be saved as **GenderWise_StateWise.json** in current **Corona_Detect_App** , You can see it by using **cat GenderWise_StateWise.json** :
```shell
{
    "State_ID": "1",
    "NIC_State_ID": "1",
    "male": "79",
    "total": "118",
    "female": "32",
    "State_Name": "Jammu & Kashmir"
},
{
    "State_ID": "2",
    "NIC_State_ID": "2",
    "male": "2",
    "total": "13",
    "female": "1",
    "State_Name": "Himachal Pradesh"
},
```
