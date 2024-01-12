import jenkins
# http://jenkins-webapi.readthedocs.org/en/latest/
#from jira.client import JIRA
import re
import xml.etree.ElementTree as ET
import sys
import time
import requests

JENKINS_URL = "https://care-jenkins.qa.care.usw2.khorostech.com"
JENKINS_USERNAME = "zubair.bhat"
JENKINS_PASSWORD = "Python@12345"


#Jenkins connection

j = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)
user = j.get_whoami()
version = self.jenkins_server.get_version()
print ("Jenkins Version: {}".format(version))
print ("Jenkins User: {}".format(user['id']))
