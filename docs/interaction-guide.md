# Power BI walkthrough and verification

The PBIX retains interactive behavior; PDF and GitHub images are static previews. Open the service report with the relevant account or download reports/bike-demand.pbix for Power BI Desktop.

## Demand overview

- Year tiles filter the KPI strip and monthly volume chart. Baseline across both years: 3,292,679 rentals, 189.46 per observed hour and 81.17% registered share.
- Select 2012: the source result is 2,049,576 rentals, 234.67 per observed hour and 81.81% registered share. The card abbreviates volume as 2.05M.
- The chart has an explicit **Year > YearMonth > Date** hierarchy. The default expands both years to monthly detail. Enable Drill down and select September 2012 to see daily counts: 218,573 rentals, 303.57 per observed hour and 79.97% registered share.
- Drill up to Year to clear the remaining branch context, then Expand all down one level to restore all-year monthly detail. Clear the year slicer using its clear-selection control. Clearing a slicer alone does not remove a chart drill context.

## Peak-hour operations

The hourly profile is sorted chronologically from 00:00 to 23:00. Working and non-working days use separate series. The weekday-by-year matrix uses a white-to-indigo background scale based on rentals per observed hour. Totals recalculate from rental volume and observed hours; they are not averages of the displayed row averages. Select a matrix cell or line point to explore its linked context.

## Weather and rider mix

The weather bars show rentals per observed hour with two-decimal labels. The rider-mix donut shows registered and casual transaction volume, not distinct people. The footer flags that heavy rain/snow has only three observed hours. A page navigator on this page opens the other report pages; the standard page pane also works throughout the report.

## Completed validation

Validated in the Power BI service reading view: baseline KPIs; the 2012 tile; September 2012 monthly-to-daily drill; drill-up and all-year restoration. The live dashboard was reopened and showed the baseline values. The source hourly file reconciles against every daily source total and an independent SQLite aggregation. All three PDF pages were rendered and reviewed, and all 18 visual containers fit within 1280×720 pages. Default exports include both years.
