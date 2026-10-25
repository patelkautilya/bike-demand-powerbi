# Bike-sharing demand: findings and proposed actions

The retained UCI Bike Sharing source describes historical Capital Bikeshare rental counts during 2011–2012. This portfolio exercise supports demand investigation, not a present-day operating forecast.

## Executive readout

- Total recorded rentals: **3,292,679** over **731 days** and **17,379 observed hours**. This is an average of **189.46 rentals per observed hour** and **4,504.35 per day**.
- Registered rentals account for **81.17%** of rental volume (2,672,662), with 620,017 casual rentals. These are rental counts, not unique customers.
- Total rentals increased from **1,243,103 in 2011** to **2,049,576 in 2012**, a **64.88%** increase. Rentals per observed hour increased from **143.79 to 234.67** (+63.20%), accounting for different recorded-hour coverage. This is not a causal growth attribution.
- Working-day demand peaks at **17:00**, averaging **525.29 rentals** across 499 observed hours. At 18:00 it averages 492.23, and at 08:00 it averages 477.01.
- On non-working days, the highest observed-hour average is at **13:00** (372.73), followed by 12:00 (366.26) and 14:00 (364.65). Working-day and non-working-day profiles suggest different demand-management windows.
- Clear/partly cloudy hours average **204.87 rentals**, mist/cloudy hours **175.17**, and light rain/snow **111.58**. Heavy rain/snow averages 74.33 but has only **three observations**; do not use it as a stable benchmark or infer a weather effect from these unadjusted comparisons.

## Proposed next steps

Investigate commuter-period service readiness on working days and midday readiness on non-working days. Add station-level availability, dock capacity, fleet movement and staffing data before deciding how many bikes or workers are needed. Compare weather within matching hour, season and year before testing any weather-related operating policy. Monitor volume and recorded-hour averages together so calendar coverage does not masquerade as performance.

## Validation and limitations

The hourly counts reconcile exactly to the independent daily file, and casual plus registered equals total on every record. Python totals also reconcile with SQLite. Missing date-hour combinations remain absent; they are not zero-demand observations. Weather mix, service coverage, adoption, holidays and other unobserved factors may influence the findings. No inventory shortages, revenue losses, forecast accuracy or operational improvements are claimed. Original source attribution and adaptation notes are in data/SOURCE.md.
