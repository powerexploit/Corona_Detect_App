import requests as req
from os import system
import json
system('tput setaf 11')
print(
		"""
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
		"""
		)

put = int(input(">>> "))
if put == 1:
	urls = 'https://covid19.nhp.gov.in/corona_data/GenderWise_StateWise'
	response = req.get(urls)
	data = json.loads(response.text)

	with open ('GenderWise_StateWise.json','w')	as outfile:
		json.dump(data,outfile,indent=4)
    
elif put == 2:
	urls = 'https://covid19.nhp.gov.in/corona_data/DistrictCases'
	response = req.get(urls)
	data = json.loads(response.text)

	with open ('DistrictCases.json','w') as outfile:
		json.dump(data,outfile,indent=4)
