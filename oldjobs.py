import jenkins
import time
# It comes with pip module python-jenkins
# use pip to install python-jenkins

# Jenkins Authentication URL
JENKINS_URL = "https://care-jenkins.qa.care.usw2.khorostech.com/"
JENKINS_USERNAME = "zubair.bhat"
JENKINS_PASSWORD = "Python@12345"

class DevOpsJenkins:
    def __init__(self):
        try:
            self.jenkins_server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)
            user = self.jenkins_server.get_whoami()
            version = self.jenkins_server.get_version()
            print ("Jenkins Version: {}".format(version))
            
            print ("Jenkins User: {}".format(user['id']))
        except JenkinsException as e:
        print(f"Error: {e}")

    def build_job(self, name, token):
        next_build_number = self.jenkins_server.get_job_info(name)['nextBuildNumber']
        self.jenkins_server.build_job(name, token=token)
        time.sleep(10)
        build_info = self.jenkins_server.get_build_info(name, next_build_number)
        return build_info


if __name__ == "__main__":
    NAME_OF_JOB = "oldjobs"
    TOKEN_NAME = "testtoken"
    # Example Parameter
    #PARAMETERS = {'project': 'devops'}
    jenkins_obj = DevOpsJenkins()
    output = jenkins_obj.build_job(NAME_OF_JOB, TOKEN_NAME)
    print ("Jenkins Build URL: {}".format(output['url']))

