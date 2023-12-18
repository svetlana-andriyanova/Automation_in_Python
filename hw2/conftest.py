import pytest
import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

@pytest.fixture()
def xpath_login():
    return """//*[@id="login"]/div[1]/label/input"""

@pytest.fixture()
def xpath_paswd():
    return """//*[@id="login"]/div[2]/label/input"""

@pytest.fixture()
def xpath_btn():
    return """//*[@id="login"]/div[3]/button"""

@pytest.fixture()
def bad_res():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""
@pytest.fixture()
def res_log():
    return """//*[@id="app"]/main/div/div[1]/h1"""

@pytest.fixture()
def add_post():
    return """//*[@id="create-btn"]"""

@pytest.fixture()
def add_title():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""

@pytest.fixture()
def add_discription():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""

@pytest.fixture()
def add_content():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""

@pytest.fixture()
def btn_save():
    return """//*[@id="create-item"]/div/div/div[7]/div/button/span"""

@pytest.fixture()
def res_post():
    return """//*[@id="app"]/main/div/div[1]/div/div[3]"""

@pytest.fixture()
def site():
    my_site = Site(testdata["address"])
    yield my_site
    my_site.close()



