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

Snotel sites: [here](https://www.nrcs.usda.gov/wps/portal/wcc/home/quicklinks/imap#version=143&elements=R&networks=!&states=!&counties=!&hucs=&minElevation=&maxElevation=&elementSelectType=all&activeOnly=true&activeForecastPointsOnly=false&hucLabels=false&hucIdLabels=false&hucParameterLabels=false&stationLabels=&overlays=&hucOverlays=&basinOpacity=100&basinNoDataOpacity=100&basemapOpacity=100&maskOpacity=0&mode=data&openSections=dataElement,parameter,date,basin,elements,location,networks&controlsOpen=true&popup=&popupMulti=&popupBasin=&base=esriNgwm&displayType=station&basinType=6&dataElement=WTEQ&depth=-8&parameter=PCTMED&frequency=DAILY&duration=I&customDuration=1&dayPart=E&monthPart=E&forecastPubDay=1&forecastExceedance=50&seqColor=1&divColor=3&scaleType=D&scaleMin=&scaleMax=&referencePeriodType=POR&referenceBegin=1981&referenceEnd=2010&minimumYears=20&hucAssociations=true&relativeDate=-1&lat=39.062&lon=-97.603&zoom=5.0)

Debugging: 
The size of the header on the csv depends on the number of features you export, so you may need to tweak it for the csv to read properly.

