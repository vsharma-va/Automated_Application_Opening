# What it does
You can create envs which will contain applications or websites which you frequently use together.
Then you can run that env using a single command, which in turn will execute all applications or websites which were added in that env.


# How To Use
1. Clone this git repository.
1. [Download and install Python](https://www.python.org/downloads/).
1. Make sure to tick the ADD TO PATH option when prompted by the installer.
1. Open Command Prompt and install argparse by typing *pip install argparse*.
1. To use the program from any directory add the folder containing all the scripts to the path variable. [Tutorial on how to add a directory to path](https://correlated.kayako.com/article/40-running-python-scripts-from-anywhere-under-windows) 
1. To run the program open windows powershell and type auto_open.py -h to receive all the available commands


# Commands
* **-aenv** - Create a new enviornment
* **-aenvweb** - Create a new enviornment with website links. Enter the websites links after the -aenvweb command. If there are multiple websites then put a space between each link
* **-dispenv** - Display all enviornments
* **-rex** - Run an existing enviornment. Type the name of the enviornment after the command
* **-delaenvs** - Delete all enviornments
* **-del** - Delete a specified enviornment. Type the name of the enviornment after the command