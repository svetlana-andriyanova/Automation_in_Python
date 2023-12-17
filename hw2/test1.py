import time
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

# def test_step1(site, xpath_login, xpath_paswd, xpath_btn, bad_res):
#     input1 = site.find_element("xpath", xpath_login)
#     input1.send_keys("test")
#     input2 = site.find_element("xpath", xpath_paswd)
#     input2.send_keys("test")
#     btn = site.find_element("xpath", xpath_btn)
#     btn.click()
#     err_lable = site.find_element("xpath", bad_res)
#     assert err_lable.text == "401"


def test_step2(site, xpath_login, xpath_paswd, xpath_btn, res_log, add_post, add_title, add_discription, add_content, btn_save, res_post):
    input1 = site.find_element("xpath", xpath_login)
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", xpath_paswd)
    input2.send_keys(testdata["password"])
    btn = site.find_element("xpath", xpath_btn)
    btn.click()
    login = site.find_element("xpath", res_log)
    assert login.text == "Blog"
    time.sleep(testdata["sleep_time"])

    # создание поста
    btn_post = site.find_element("xpath", add_post)
    btn_post.click()
    time.sleep(testdata["sleep_time"])
    title = site.find_element("xpath", add_title)
    title.send_keys(testdata["title"])
    discription = site.find_element("xpath", add_discription)
    discription.send_keys(testdata["discription"])
    content = site.find_element("xpath", add_content)
    content.send_keys(testdata["content"])
    save_post = site.find_element("xpath", btn_save)
    save_post.click()
    time.sleep(testdata["sleep_time"])

    # тест нового поста
    text_label = site.find_element("xpath", res_post)
    assert text_label.text == "content for NEW POST"

