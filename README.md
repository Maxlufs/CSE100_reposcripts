scripts_ucsd_acadwf_fork
=====================

Original scripts for github academic workflow created by [Phillip Conrad](https://github.com/pconrad), current project forked by UCSD CSE Department

Getting Started
=====================
Add an SSH key to account if not yet done. See [here](https://help.github.com/articles/generating-ssh-keys#platform-all). 

All steps from here on out will assume that a valid SSH-RSA key is associated with this account and that the user is working off of ieng6.

Initializing the Repo
=====================
1. Create the directory for the repository (such as deploy_scripts)
2. run the following commands:

            cd <DIRECTORY>
            git init
            git remote add --track master origin git@github.com:UCSD-CSE-100/scripts_ucsd_acadwf_fork.git
            git pull
            ./initRepo.sh
            
3. Optional: You may configure your config.py as needed. Default values for your particular username will have been filled in and created if they do not already exist.

Creating Repos for Students and Pairs
=====================
      NOTE: Github Password or OAuth token will need to be entered for each individual command in a script
            Script may take up to 1 hour to run depending on API calls reaching the rate limit

1. run 

            ./addStudentsCreateRepos.sh <github username> <Project #>

2. Check your scripts log directory for command status, the script itself will tell you if it thinks it succeeded in executing all scripts, but it never hurts to double check.

Pulling Repos for Grading
=====================

Acknowledgements
=====================

Portions of this project were adapted from materials from [Phill Conrad at UC Santa Barbara](http://www.cs.ucsb.edu/~pconrad/)

This project is a fork of [Phill Conrad's](https://github.com/pconrad) project: github-acadwf-scripts (https://github.com/UCSB-CS-Using-GitHub-In-Courses/github-acadwf-scripts)

This repository uses [PyGithub](https://github.com/jacquev6/PyGithub) to utilize GitHub's API through python scripts.

