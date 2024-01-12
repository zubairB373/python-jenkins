import jenkins
import time
# It comes with pip module python-jenkins
# use pip to install python-jenkins

# Jenkins Authentication URL
JENKINS_URL = "https://care-jenkins.qa.care.usw2.khorostech.com/"
JENKINS_USERNAME = "zubair.bhat"
JENKINS_PASSWORD = "Python@12345"
server = jenkins.Jenkins('JENKINS_URL', username='JENKINS_USERNAME', password='JENKINS_PASSWORD')
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
