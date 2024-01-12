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

count = 0
six_months_ago = (time.time() - 15768000)
for jobname in j.jobnames:
	job = j.job(jobname)
	try:
		if j.job_exists(jobname):
			if job.last_build.info['timestamp']:
				# Jenkins appears to add microseconds to the timestamp.
				epoch_time = job.last_build.info['timestamp'] / 1000
				if epoch_time < six_months_ago:
					count += 1
					print '{}: {}'.format(count, jobname)
	except:
		continue
