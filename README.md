# Snotel Data Download
A simple python function to get csv of stotel data drom multiple sites in timeseries format. 

You will need:
-site number and state for each site you want to download
-feature code for the data you want. they are:
                    
		
| Element                    | Unit | Ecode |
|----------------------------|------|-------|
|                            |      |       |
| Snow Water Equivalent      | In   | WTEQ  |
|                            |      |       |
| Precipitation Accumulation | In   | PREC  |
| Air Temperature Observed   | Degc | TOBS  |
| Air Temperature Maximum    | Degc | TMAX  |
| Air Temperature Minimum    | Degc | TMIN  |
| Air Temperature Average    | Degc | TAVG  |
| Snow Depth                 | In   | SNWD  |
| Battery Maximum            | Volt | BATX  |
| Battery                    | Volt | BATT  |
| Battery Minimum            | Volt | BATN  |



Debugging: 
The size of the header on the csv depends on the number of features you export, so you may need to tweak it for the csv to read propoerly.
