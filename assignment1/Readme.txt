Plugins-
Environments: python 3.7.0


Dependencies-
Python Libraries: pandas 1.0.3, numpy 1.18.1, openpyxl, datetime


Programs-

.sh files:

assign1.sh 
top level script that runs the entire assignment

neighbor-districts-modifier.sh
runs neighbor-districts-modifier.py
Input: neighbor-districts.json, cowin_vaccine_data_districtwise.csv ,cleaned_file.json
Output: nieghbor-districts-modified.json

edge-generator.sh
runs edge-generator.py
Input: neighbor-districts-modified.json
Output: edge-graph.csv

case-generator.sh
runs case-generator.py
Input: districts.csv,neighbor-districts-modified.json
Output: cases-week.csv, cases-month.csv, cases-overall.csv

peaks-generator.sh
runs  peaks-generator.py
Input: districts.csv,neighbor-districts-modified.json
Output: district-peaks.csv ,state-peaks.csv ,overall-peaks.csv

vaccinated-count-generator.sh
runs vaccinated-count-generator.py
Input: cowin_vaccine_data_districtwise.csv
Output: district-vaccinated-count-week.csv, district-vaccinated-count-month.csv, district-vaccinated-count-overall.csv, state-vaccinated-count-week.csv, state-vaccinated-count-month.csv, state-vaccinated-count-overall.csv

vaccination-population-ratio-generator.sh
runs vaccination-population-ratio-generator.py
Input: DDW_PCA0000_2011_Indiastatedist.xlsx, cowin_vaccine_data_districtwise.csv
Output: district-vaccination-population-ratio.csv, state-vaccination-population-ratio.csv, overall-vaccination-population-ratio.csv

vaccine-type-ratio-generator.sh
runs vaccine-type-ratio-generator.py
Input: cowin_vaccine_data_districtwise.csv
Output: district-vaccine-type-ratio.csv, state-vaccine-type-ratio.csv, overall-vaccine-type-ratio.csv

vaccinated-ratio-generator.sh
runs vaccinated-ratio-generator.py
Input: DDW_PCA0000_2011_Indiastatedist.xlsx, cowin_vaccine_data_districtwise.csv
Output: district-vaccinated-dose-ratio.csv, state-vaccinated-dose-ratio.csv, overall-vaccinated-dose-ratio.csv

complete-vaccination-generator.sh
runs complete-vaccination-generator.py
Input: DDW_PCA0000_2011_Indiastatedist.xlsx, cowin_vaccine_data_districtwise.csv, state-vaccinated-count-week.csv, state-vaccinated-count-overall.csv
Output: complete-vaccination.csv


How to use:
In order to run all programs sequentially, run the following command from the terminal-
bash assign1.sh 

NOTE: 
1) The programs will run sequentially in the extact order of the .sh file mentioned above.
2) In Q7 where there is "0" value for Covaxin, I have taken that respective ratio as "0"
3) In Q1 I have used cleaned_file.json file which cleaned manually. 
