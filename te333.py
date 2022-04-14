from pypasser.structs import Proxy
from pypasser import reCaptchaV3

url='https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LeQqWkfAAAAACpO9DVBCYse9HQ7JkLnWWwmb587&co=aHR0cHM6Ly9zYWxhZC5hY2FkZW15OjQ0Mw..&hl=zh-CN&v=6pQzWaE1NP-gB4FrqRViKjM-&size=invisible&cb=96h3ll1suwk7'


proxy = Proxy(Proxy.type.HTTPs,'https://127.0.0.1','7890')

reCaptcha_response = reCaptchaV3(url,proxy=proxy)
print(reCaptcha_response)