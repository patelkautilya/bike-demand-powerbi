let
    Source = Csv.Document(Web.Contents("https://raw.githubusercontent.com/patelkautilya/bike-demand-powerbi/main/data/rentals.csv"), [Delimiter=",", Columns=15, Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Headers = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Types = Table.TransformColumnTypes(Headers, {{"RecordID", Int64.Type}, {"Date", type text}, {"Year", type text}, {"Month", type text}, {"YearMonth", type text}, {"Hour", type text}, {"Weekday", type text}, {"DayType", type text}, {"Weather", type text}, {"TotalRentals", Int64.Type}, {"CasualRentals", Int64.Type}, {"RegisteredRentals", Int64.Type}, {"ObservedHours", Int64.Type}, {"TemperatureC", type number}, {"HumidityPct", type number}})
in
    Types
