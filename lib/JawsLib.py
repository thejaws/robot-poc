from robot.api.deco import keyword
import subprocess

ROBOT_AUTO_KEYWORDS = False


@keyword
def read_url(url):
    print(url)
    return "asldkjfa;sldkjfa;lskdjfa;slkdjfa;lsdkjf"


@keyword
def get_username():
    print("getting user name")
    return "user"
