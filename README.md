# mapfile_data_pipeline

This data pipeline gets some machine file data from server A, cleans / transforms it, moves it to server B, and places it into it's correct path. 
Two python programs are connected by two shell script runners that should be on a cron to call the python code consecutively. 

The whole pipeline can easily be orchestrated with Airflow.
