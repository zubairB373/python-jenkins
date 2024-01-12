import jenkins
import time
# It comes with pip module python-jenkins
# use pip to install python-jenkins

# Jenkins Authentication URL
JENKINS_URL = "https://xxxx"
JENKINS_USERNAME = "xxxxx"
JENKINS_PASSWORD = "xxxxxxx"


class DevOpsJenkins:
    def __init__(self):
        self.jenkins_server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)
        user = self.jenkins_server.get_whoami()
        version = self.jenkins_server.get_version()
        print ("Jenkins Version: {}".format(version))
        print ("Jenkins User: {}".format(user['id']))
