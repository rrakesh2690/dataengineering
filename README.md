
Usage :

1. Main Script is in util directory
2. Update config file with proper values.
3. Arguments to the python script
 --config "config.properties" --productconfig "cts.properties" --env "dev" --targettable <BigQuery Table Name to be loaded> --sqlquery <Full path to .sql file with query to Pull data from on-prem DB> --connectionprefix "d3" --incrementaldate <Historical Parameter , can be removed or ignored>