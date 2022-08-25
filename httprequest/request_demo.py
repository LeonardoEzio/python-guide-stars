import requests
import json


# http 请求示例
class RequestDemo:

    def __init__(self, host):
        self.host = host

    def do_post(self, url, param, headers):
        request_url = self.host + url
        result = requests.post(request_url, json.dumps(param), headers=headers)
        return result

    def do_get(self, url):
        request_url = self.host + url
        result = requests.get(request_url)
        return result


if __name__ == "__main__":
    host = "http://localhost:8300"
    api = "/scm/business/api/saveSourceQuota"
    param_dict = {"synchronousCode": "2022-08-25 12:06", "sing": "123456", "sourceQuotaReqList": []}
    child_param = {}
    child_params = []
    for i in range(0, 1000):
        child_param["operationCode"] = "operationCode"+str(i)
        child_param["orgCode"] = "orgCode"+str(i)
        child_param["orgName"] = "orgName"+str(i)
        child_param["sourcing"] = "sourcing"+str(i)
        child_param["sourcingCode"] = "sourcingCode"+str(i)
        child_param["buyer"] = "buyer"+str(i)
        child_param["buyerCode"] = "buyerCode"+str(i)
        child_param["planner"] = "planner"+str(i)
        child_param["plannerCode"] = "plannerCode"+str(i)
        child_param["substitutionGroup"] = i
        child_param["materialCode"] = "materialCode"+str(i)
        child_param["materialName"] = "materialName"+str(i)
        child_param["specificationModel"] = "specificationModel"+str(i)
        child_param["materialAttribute"] = "materialAttribute"+str(i)
        child_param["supplierCode"] = "supplierCode"+str(i)
        child_param["supplierName"] = "supplierName"+str(i)
        child_param["unitPrice"] = i
        child_param["passRate"] = i
        child_param["riskCoefficient"] = "riskCoefficient"+str(i)
        child_param["supplierScore"] = "supplierScore"+str(i)
        child_param["substitutionFactor"] = "substitutionFactor"+str(i)
        child_params.append(child_param)
    param_dict["sourceQuotaReqList"] = child_params
    json_param = json.dumps(param_dict)

    req = RequestDemo(host)
    request_headers = {"content-type": "application/json", "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjE0NDk2NzMsInBsYXRJZCI6IjAiLCJ1c2VyX25hbWUiOiJzeXNhZG1pbiIsImp0aSI6IjE5NWY3NjY2LTNmYWYtNGM3NC1iY2NmLWIzNWI0NjY2MjMwMSIsImNsaWVudF9pZCI6Im5waS1uYXJ3YWwtcHJvZHVjdGlvbiIsInNjb3BlIjpbImFsbCJdfQ.jX3oowgMLfXvZIVh53bYcE_wy4YKNdhQecrHZGI-XbI"}
    result = req.do_post(api, json_param, request_headers)
    print("request result ： {}".format(result.text))
