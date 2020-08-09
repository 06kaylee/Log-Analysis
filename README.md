# Log-Analysis
Getting information from log files generated by a simulated internal ticketing system
Using regex to parse the log file into separate messages (INFO, ERROR) and different users, stores the results in two dictionaries, and outputs the result to two CSVs. 
The first CSV lists all the error messages logged in the system sorted by the most frequent error.
The second CSV lists the users that have used the ticketing system and how many INFO and ERROR messages they have generated. 
