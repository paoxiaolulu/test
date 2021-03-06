import requests
import unittest
url = "http://integration-api.gongyuanhezi.cn/wechat/order/order_detail"

headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'IAMICHE-AGENT': "{\"os\":\"WECHAT-MP\",\"identification\":\"parkbox\",\"p_version\":\"3.0.0\",\"token\":\"UFZUBghQF1UDVltVDAcCBF0BUFA=\",\"deviceInfo\":\"mini_pro\"}",
    'Cache-Control': "no-cache"
    }
# -------POST------------
class testcase06(unittest.TestCase):
    '''订单详情 order_detail'''
    #def test_case01(self):
        #'''1.必传参为空'''
        #response = requests.request("POST", url, headers=headers)
        #dic = response.json()
        #self.assertEqual(response.status_code, 200, '返回接口失败')
        #self.assertEqual(dic.get('msg'), "*不能为空", '返回接口失败')
        #print("必传参未输入参数，与预期一致")

    def test_case02(self):
        '''正向获取'''
        #payload = "idcard=321322199301254065&truename=liulu"
        response = requests.request("POST", url, data=payload, headers=headers)
        dic = response.json()
        self.assertEqual(response.status_code, 200, '返回接口失败')
        self.assertEqual(dic.get('msg'), "OK", '返回接口预期失败，实际成功')
        print("与预期一致")
    def test_case01(self):
        '''破坏性获取:传不存在的订单号'''
        payload = "ordercode"
        response = requests.request("POST", url, data=payload, headers=headers)
        dic = response.json()
        self.assertEqual(response.status_code, 400, '返回接口预期失败，实际成功')
        self.assertEqual(dic.get('error'), "Bad Request", '返回接口预期失败，实际成功')
        print("破坏性获取订单列表与预期一致")
    #def test_case04(self):
        #'''4.破坏性获取:传错误姓名'''
        #payload = "idcard=321311199301254065&truename=liulu"
        #response = requests.request("POST", url, data=payload, headers=headers)
        #dic = response.json()
        #self.assertEqual(response.status_code, 400, '返回接口预期失败，实际成功')
        #self.assertEqual(dic.get('error'), "Bad Request", '返回接口预期失败，实际成功')
        #print("破坏性获取订单列表与预期一致")
    def test_case02(self):
        '''5.破坏性获取：输入特殊符号'''
        payload = "idcard=@&truename=liulu"
        response = requests.request("POST", url, data=payload, headers=headers)
        dic = response.json()
        self.assertEqual(response.status_code, 400, '返回接口预期失败，实际成功')
        self.assertEqual(dic.get('error'), "Bad Request", '返回接口预期失败，实际成功')
        print("破坏性获取订单列表与预期一致")



if __name__ == '__main__':
    unittest.main()