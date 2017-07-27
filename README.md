# NewsReports

Generates reports based upon a database of news articles.

## Download

Download the [zip file](https://github.com/kinnamonb/NewsReports/archive/master.zip)

## Requirements

* [Python 2.7.12](https://www.python.org/downloads/release/python-2712/)
* A PostgreSQL database populated with data from [newsdata.sql](https://github.com/kinnamonb/NewsReports/blob/master/newsdata.zip)

## Usage

After extracting the files, run `python gen_reports.py`

## Database Views

* *total_visits* - Gets the total number of website visits grouped by day
  `create view total_visits as select time::date as day, count(*) total from log group by day;`

* *errors* - Gets the total number of 404 errors grouped by the day
  `create view errors as select time::date as day, status, count(*) as num from log where status like '404%' group by day, status;`

## License

Copyright 2017 Brett Kinnamon

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
