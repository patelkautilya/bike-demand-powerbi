"""Prepare and reconcile the UCI Bike Sharing source at observed-hour grain."""
from pathlib import Path
import hashlib
import json
import sqlite3
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
h = pd.read_csv(ROOT / 'data/hour.csv', parse_dates=['dteday'])
d = pd.read_csv(ROOT / 'data/day.csv', parse_dates=['dteday'])
assert len(h) == 17379 and len(d) == 731
assert not h.isna().any().any()
assert h[['dteday','hr']].duplicated().sum() == 0
assert h.instant.is_unique and h.cnt.eq(h.casual + h.registered).all()
pd.testing.assert_series_equal(h.groupby('dteday').cnt.sum(), d.set_index('dteday').cnt, check_names=False)
weekdays = {0:'07 Sun',1:'01 Mon',2:'02 Tue',3:'03 Wed',4:'04 Thu',5:'05 Fri',6:'06 Sat'}
weather = {1:'1 Clear / partly cloudy',2:'2 Mist / cloudy',3:'3 Light rain / snow',4:'4 Heavy rain / snow'}
clean = pd.DataFrame({'RecordID':h.instant,'Date':h.dteday.dt.strftime('%Y-%m-%d'),'Year':h.dteday.dt.year.astype(str),'Month':h.dteday.dt.strftime('%m %b'),'YearMonth':h.dteday.dt.strftime('%Y-%m'),'Hour':h.hr.map(lambda x:f'{x:02d}:00'),'Weekday':h.weekday.map(weekdays),'DayType':h.workingday.map({0:'Non-working day',1:'Working day'}),'Weather':h.weathersit.map(weather),'TotalRentals':h.cnt,'CasualRentals':h.casual,'RegisteredRentals':h.registered,'ObservedHours':1,'TemperatureC':(h.temp*47-8).round(2),'HumidityPct':(h.hum*100).round(2)})
clean.to_csv(ROOT / 'data/rentals.csv',index=False)
con=sqlite3.connect(':memory:')
clean.to_sql('rentals',con,index=False)
sql=con.execute('SELECT SUM(TotalRentals),SUM(CasualRentals),SUM(RegisteredRentals),COUNT(*),COUNT(DISTINCT Date) FROM rentals').fetchone()
assert sql==(int(h.cnt.sum()),int(h.casual.sum()),int(h.registered.sum()),len(h),731)
metrics={'observed_hours':len(h),'observed_days':len(d),'missing_date_hour_combinations':731*24-len(h),'total_rentals':int(h.cnt.sum()),'casual_rentals':int(h.casual.sum()),'registered_rentals':int(h.registered.sum()),'registered_share':float(h.registered.sum()/h.cnt.sum()),'rentals_per_observed_hour':float(h.cnt.mean()),'rentals_per_day':float(d.cnt.mean()),'source_hour_sha256':hashlib.sha256((ROOT/'data/hour.csv').read_bytes()).hexdigest()}
for dim in ['Year','YearMonth','Hour','DayType','Weather']:
    s=clean.groupby(dim).agg(total_rentals=('TotalRentals','sum'),observed_hours=('ObservedHours','sum'),registered_rentals=('RegisteredRentals','sum'),casual_rentals=('CasualRentals','sum'))
    s['rentals_per_observed_hour']=s.total_rentals/s.observed_hours
    s.to_csv(ROOT/'reports'/f'{dim}.csv')
clean.groupby(['DayType','Hour']).agg(total_rentals=('TotalRentals','sum'),observed_hours=('ObservedHours','sum'),rentals_per_observed_hour=('TotalRentals','mean')).to_csv(ROOT/'reports/daytype_hour.csv')
(ROOT/'reports/metrics.json').write_text(json.dumps(metrics,indent=2)+'\n')
print(json.dumps(metrics,indent=2))
print(pd.read_csv(ROOT/'reports/Year.csv').to_string(index=False))
print(pd.read_csv(ROOT/'reports/daytype_hour.csv').sort_values('rentals_per_observed_hour',ascending=False).head(6).to_string(index=False))
