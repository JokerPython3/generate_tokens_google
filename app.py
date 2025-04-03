import http.client
import re
import requests
import random
import time
import os
from user_agent import generate_user_agent
class S1:
    def __init__(self):
        self.tim=time.time()
        self.ua=str(generate_user_agent())
        self.sex='موط'
    def gen(self):
        conn = http.client.HTTPSConnection('accounts.google.com')
        while True:
            try:
               headers = {
            'authority': 'accounts.google.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',

            'referer': 'https://accounts.google.com/',

            'user-agent': self.ua,
        }
               conn.request(
            'GET',
            '/lifecycle/flows/signup?biz=false&continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Diwjjwwj%26oq%3Diwjjwwj%26gs_lcrp%3DEgZjaHJvbWUyBggAEEUYOTIKCAEQABiABBiiBDIKCAIQABiABBiiBDIHCAMQABjvBTIKCAQQABiABBiiBDIKCAUQABiABBiiBNIBBzc1OWowajGoAgCwAgA%26sourceid%3Dchrome-mobile%26ie%3DUTF-8&flowEntry=SignUp&flowName=GlifWebSignIn&hl=ar',
            headers=headers
        )
               response = conn.getresponse().info()
        #print(response)
               __Host_GAPS=str(response).split('Set-Cookie: __Host-GAPS=')[1].split(';')[0]

    #		   print(host)
               tl=str(response).split('TL=')[1].split('\n')[0]
    #		   print(tl)
               break
            except Exception as r:
    #			print(r)
                pass
        while True:
            try:
                cookies = {

            '__Host-GAPS':__Host_GAPS,
        }

                headers = {
            'authority': 'accounts.google.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',

            'referer': 'https://accounts.google.com/',

            'user-agent': self.ua,

        }

                response = requests.get(
            f'https://accounts.google.com/lifecycle/steps/signup/name?continue=https://www.google.com/search?q%3Diwjjwwj%26oq%3Diwjjwwj%26gs_lcrp%3DEgZjaHJvbWUyBggAEEUYOTIKCAEQABiABBiiBDIKCAIQABiABBiiBDIHCAMQABjvBTIKCAQQABiABBiiBDIKCAUQABiABBiiBNIBBzc1OWowajGoAgCwAgA%26sourceid%3Dchrome-mobile%26ie%3DUTF-8&flowEntry=SignUp&flowName=GlifWebSignIn&hl=ar&TL='+tl,
            cookies=cookies,
            headers=headers,
        )
                tok=re.findall(r'"(.*?)"',str(response.text).split('<!doctype html')[1].split('/lifecycle/_/AccountLifecyclePlatformSignupUi/')[0])
                hl=tok[0]
                s1=tok[31]
                at=tok[38]		
    #			print(hl)
    #			print(at)
    #			print(s1)
                break
            except Exception as r:
    #			print(r)
                pass
        while True:
            try:
                cookies = {

            '__Host-GAPS': __Host_GAPS,
        }

                headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',

            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/',

            'user-agent': self.ua,

            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-goog-ext-391502476-jspb': '["'+s1+'"]',
            'x-same-domain': '1',
        }

                params = {
            'rpcids': 'E815hb',
            'source-path': '/lifecycle/steps/signup/name',

            'hl':hl,
            'TL': tl,
        }
                name=''.join(random.choice('azertyuiopmlkjhgfdsqwxcvbn') for i in range(random.randrange(5,13)))
                data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(name,at)

                response = requests.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
    #			print(response.text)
                break
            except Exception as r:
    #			print(r)
                pass
        while True:
            try:
                cookies = {

            '__Host-GAPS': __Host_GAPS,
        }
                headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',

            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/',

            'user-agent': self.ua,

            'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
            'x-goog-ext-391502476-jspb': '["'+s1+'"]',
            'x-same-domain': '1',
        }

                params = {
            'rpcids': 'eOY7Bb',
            'source-path': '/lifecycle/steps/signup/birthdaygender',

            'hl': hl,
            'TL': tl,
        }
                year=str(random.randrange(1980,2007))
                month=str(random.randrange(1,12))
                day=str(random.randrange(1,28))
                data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3C2hZqFk4CAAbWyV7d9smNg70z-2-0ld_0ADQBEArZ1Mb_GVIu_8MvlY6bsxkk-EWy0SLBedT2h84tyT1Y4XzmcWzXSNfQDh4LFNof_3IOzQAAA3WdAAAAcKcBB7EATfi0C_NDA8ZUcUVZmSl3e70mI470oEDtBVkhJ4fIFmBB_O3A9tvNt0PQF7mRM7rb8idUsWtl29rUWmCvalzfsb7PpIE3-FpjciM6uQBoVgbGLOW4IN7DnEn0hL4bZDsZ3gfH6L-sainvCD_V8RFiYyJ-nrZxKGdv4QXEC93XtGkS_APjEXgc1URQgsk0YQGC_lPYXCgx3N9SQuDldSv7anc3_6WYAzFpoGcMhW4cniWEevuf4lQEYZYslD0JYKKiyIGmv36UbhqJzyUAEsM5GQ7oFcPlRDAwmBaMry8BKfmKRGcadgZ8cwK69Rpf5YcVmRWkCd7gxRarVfw3XTvrDbmcS9_MXPsSeJy1_weZ5wTBP0xOmnL7ViUqFuYSWL0Yge_7whfk-a7_0-Nnoh4KwGCulEgrSUpLxrdQDZlSZ5vYNoDvvdaackVc0OATKMMcobS5RSGm_NvJ46XhjuKODtO4x8NSH2lKv88OD0TWYvBUf0xeoBON9IXKF9hGn87ECgw6ghk-L-as4fXwh_YPIg2-MmcNRHXueKkRuMakNLjZz4JfTGyAWicpxlv2hsY9YAg30y4PAHL9Fw53hxyNmLqWNo66Ku5Bhty0AU_C8NHWQkSb2Pe7R8u1lIky32DNAcK7MiBUAhTMvTEfCi3ThA0PB2hG5uuhemPgwumEMotVHjupKNgWQTkFNKinC9FwyVpjy7QZh2ouHooPTFuJKUcVqXcm-igtWpADp9Vc4BPd1l8hw6Dmioz7cxfT9U2qsdm72rFRXzxT_nOUNpBsxwHPajVQufCxZM3u9quGfqZLMrvxOUta3iyQgTX7ITTdcP8ydBjkgzfcajFERGSwPWdNOQcFRJNbBU30lgI4Uwq7c63IpXFAPE7sRIBpeBjb9SxSlI5XCd_Mx6bfs0AxQ5HJafNFDpN61lkeVoKQzSXZj1ezqoC4v7m336t8z-_m_-OeE96wVCs-YvwfGnlamD1ZyZpPGiUNgP7Zxq-dWvn_Ja9eqkyqZydCUwBWN_dTtFHPBeR2Rz8Cabe8FIY2fiSU4o-Wb10sXwtguMsuzxdp8YJMacDUT7sxRP1t8lmJIbCnH0qCLq1kU_Dvdf83ICBVD-WM6pgRZte8d0c4nbHSgsqfQK2F30lTToow0F5pvjzd12-6XCeS5ev1rmeogvrBDBwUkEnjrkqUqN7sARiSLReuc4eIGOe_rA6Bid8lnylAJuCGnMaYsOYi1erUoXwAFgPfnaPA382h_LzLJOfgbyjOpL06h14m03ZzZcesszw4tVP2N816-KhzxdmP2WHzcmVyuwvyTUNzKgo9tlzHTcfaxh1OBOJM0RYg3qtfOrFbHt9o6g9CHfl8Y89LqXcRE-CjFAgvSyvTfTmh1DADMwiucrifzKY5Yquj8L2v7aIdelWWPb4Wx1uoWhd4rL7PBCX4ii9ES-h0YXaaYEeOAqrkM82W2wckr7ZawEGsmttXZ56EYVg_-tVhIiZ2GwSAjGhcPDZsq9WeDW9FkuCL7ZBJjS6OzF_6L4Y0zB2HsupjAo3113RCG0BzNjJpFasFDWE4kQaje9gT-sPNwL8CqPSpJN4plTTzQpqShoklzzpQnZYLNBxqiHTLBL5yGwWXiiZegZmjojd_dap3WabvJbPX4uFlyCJbSHta9UMksXWWcre822mJ_A_PokpnHs1skAXjfMN1jqnSVFXTCYlp80stIfNz9_EruB5LQwz1ySYM7glq_q6iryP77-fvitmDex7T2yGjpjRKsoiWGphTaQzvaBM-lrJrR35_28J4lavx8gRm-btIrmkQHHm-t_x1yXy0nXiuovmVZklBjDYj_PowCQzV_0PK3fwoOgjbT-O3bCe7kE1fmkayMV5lg-u2aIxEXrP6GNnm2aaVys7omKFA-hcDgXRLnbXo8od0GGtKvBly-Hc9j1GVn3jCeBJuiobe0t14sydrqBLakjY8QA7U-ombg5L0MQtStFrYDa-0XBmRsMVlaowS_j9gpE3Vgt2A_ViK3u_7GRlcUOKlINWO9z0rHLlVccVNUjcT8VJNTF816YFKR-cTo9ZWZ0P_-SbdK19GlFFyHruA-OSfxwJUKoRFrFQhMPHizNq26629U1vEdH1tyck_GbxAK7Y67i43nLux1TI1cHk3PdItQaAa6wYHAf1gHjq3a9yorUmjdOFzAvwX3-PsTpVPDOT048WnLv8hdGWHBhmIqqTbqfzM1i_5BIm2PQHzvX2T5R5nhgVymY0XB_l8TTERv_HviyMw4yZKmaV21IdPbY4elubj_-mYTOKiqq4-shnUx8eNxhawqimdS9G54ZHcsJ2STUHIIU4u9_NU7xVUUcTZTG05YOgSINBpWLaa37VL-YoRajkEc-mf3HpB9tnH1iZCWEolsdoIu3TEq6Y435fbQjpfqTD4%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Diwjjwwj%26oq%3Diwjjwwj%26gs_lcrp%3DEgZjaHJvbWUyBggAEEUYOTIKCAEQABiABBiiBDIKCAIQABiABBiiBDIHCAMQABjvBTIKCAQQABiABBiiBDIKCAUQABiABBiiBNIBBzc1OWowajGoAgCwAgA%26sourceid%3Dchrome-mobile%26ie%3DUTF-8%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(year,month,day,at)

                response = requests.post(
            'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
    #			print(response.text)
                break
            except Exception as r:
    #			print(r)
                pass
        ts=time.time()-self.tim
        return {
                        'tokens':{
                            '__Host-GAPS':__Host_GAPS,
                            'TL':tl,
                            'hl':hl,
                            'at':at,
                            's1':s1,
                        },
                        'info':{
                            'name':name,
                            'birthday':{
                                'day:month:year':day+':'+month+':'+year,
                                'day':day,
                                'month':month,
                                'year':year,
                                'by':'@jokerpython3',
                                'message':'ني خماط',
                                'hhhh':'ههه',
                                'MyChannel':'موط',
                                'many_thank_to':'@Nate_D_Qredes/عثمان',
                                'ILove':'@d_dwu / زجاد',
                                #حبج

                            },
                            'time_get_tokens':ts,
                            'time':time.time(),               
                                },
                        'errors':[],
                    }




from flask import Flask,jsonify

app = Flask(__name__)


@app.route('/get_tokens')
def index():
    z=S1().gen()
    return jsonify({"Def":"JokerPython3","tokens":z})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
#S1/حلمي قسمبلاه
