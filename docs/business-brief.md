# Operations reporting brief

**Audience:** service operations and capacity-planning analysts.

**Decisions supported:** investigate when demand is concentrated; compare working and non-working day profiles; inspect historical monthly volumes and weather associations. The source has no stations, fleet inventory, stockouts, revenue, service costs or measured capacity. It cannot determine exact bike redistribution or staffing requirements.

**Grain:** one observed date-hour, with rental counts split into casual and registered categories. Rentals are transactions/counts, not unique people.

**KPIs:** total rentals sums TotalRentals; rentals per observed hour divides that sum by ObservedHours in the same current filter context; registered share divides RegisteredRentals by TotalRentals. The two rider categories reconcile to the total. Use total volume for monthly trends and observed-hour averages for comparisons across hour, day type and weather.

**Calendar:** 2011-01-01 through 2012-12-31. Full-year totals are comparable historical periods, though leap-year and recorded-hour coverage differ. 2012 total rentals grew 64.88% versus 2011; observed-hour demand grew 63.20%. These changes are descriptive and may reflect service expansion, adoption, weather or other factors.

**Quality:** 17,379 unique date-hour records; no source nulls. All 731 daily totals independently reconcile against day.csv. There are 165 absent date-hour combinations out of 17,544 possible; they are not imputed as zero. Heavy rain/snow has only three observations, so its average is not a stable operational benchmark. Weather effects are associative and confounded by season, hour and calendar mix.

**Source transformations:** labeled ordered month/hour/weekday categories; working-day and weather labels; source counts retained. Date is an ISO text key for explicit Year > YearMonth > Date drill levels. TemperatureC follows the current UCI hourly metadata formula (normalized × 47 − 8), while the archived Readme describes a different scale; temperature is not used in the report's findings or visuals because of that documentation discrepancy. HumidityPct multiplies the normalized source by 100.

**Attribution:** H. Fanaee-T (2013), Bike Sharing, UCI Machine Learning Repository, DOI 10.24432/C5W894, CC BY 4.0. See data/SOURCE.md and the original Readme.txt. This independent portfolio case study does not claim client work, operational deployment or measured business impact.
