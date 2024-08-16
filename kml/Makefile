



all: state_data.js election_data_2016.js


state_data.js: extract_coordinates.py 
	extract_coordinates.py > state_data.js


election_data_2016.js: extract_election_data.py election_data_2016.txt
	extract_election_data.py > election_data_2016.js


clean:
	rm -f state_data.js election_data_2016.js

