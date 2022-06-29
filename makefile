dashboard:
	streamlit run --browser.serverAddress localhost dashboard.py

dashboard-nowatch:
	streamlit run --browser.serverAddress localhost --server.fileWatcherType none dashboard.py

download-data-adult:
	mkdir -p datasets/adult
	curl -L http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.names -o datasets/adult/adult.names
	curl -LO http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data -o datasets/adult/adult.data
	curl -LO http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test -o datasets/adult/adult.test
