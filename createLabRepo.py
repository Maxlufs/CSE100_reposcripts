#!/usr/bin/python

# This script reads all the users from the CSV file created
# by the Google Form.

# If first checks for any duplicate first names.  If there are duplicate
# first names, it deambiguates the first names by adding first letters of
# the last name until the names are distinguished.

# It then:
#  (1) checks if the github user exists (bails, if not)
#  (2) creates the Student_FirstName team (if not already there)
#  (3) adds the github user to the Student_FirstName team and AllStudents team

from __future__ import print_function
from github_acadwf import createLabRepo

import getpass
import sys
import os
import argparse

#check if config file exists
if not os.path.exists("config.py"):
	print("Unable to find config file, please see sample_config.py")
	sys.exit(1)

import config


from disambiguateFunctions import makeUserDict
from disambiguateFunctions import disambiguateAllFirstNames
from disambiguateFunctions import getUserList

sys.path.append("./PyGithub");

from github import Github
from github import GithubException
                      
defaultInputFilename =  config.getStudentsFile()

parser = argparse.ArgumentParser(description='Disambiguate First Names.')
parser.add_argument('lab',metavar='labxx',  
                    help="which lab (e.g. lab00, lab01, etc.)")
parser.add_argument('-i','--infileName',
                    help='input file (default: ' + defaultInputFilename+"'",
                    default=defaultInputFilename)
parser.add_argument('-u','--githubUsername', 
                    help="github username, default is current OS user",
                    default=getpass.getuser())

args = parser.parse_args()

pw = getpass.getpass()
g = Github(args.githubUsername, pw, user_agent="PyGithub")
org= g.get_organization(config.getOrgName())

createLabRepo(g,org,args.infileName,args.lab)

sys.exit(0)







