import requests
import json

class Wechat():
    appId = 'wx5da44835dac1892e'
    appSecret = '6e75d11d9964510f2d86218839ffe1c9'
    env = 'book-e9sdz'
    access_token = ''

    def __init__(self):
        pass

    def clearStr(self, str):
        str = str.replace('\r', '')
        str = str.replace('\n', '')
        str = str.replace(' ', '')
        return str

    def getAccessToken(self):
        if self.access_token:
            return self.access_token
        
        url = "https://api.weixin.qq.com/cgi-bin/token"
        params = {
            'grant_type' : 'client_credential',
            'appid': self.appId,
            'secret': self.appSecret
        }
        res = requests.get(url=url, params=params)
        json = res.json()
        self.access_token = json['access_token']
        return self.access_token

    def databaseAdd(self, query):
        token = self.getAccessToken()
      
        data = json.dumps({
            'env': self.env,
            'query': query
        })
        url = 'https://api.weixin.qq.com/tcb/databaseadd?access_token={}'.format(token)
        headers = {'content-type': 'application/json'}
        res = requests.post(url, data=data, headers=headers)
        print(res.text)
        d = res.json()
        return d['id_list'][0]

    def addCategory(self):
        pass

    def addBook(self,*args, categoryId, name, author, desc, order):
        print(args)
        query = '''
        db.collection('book_test').add({{
            data: {{
                categoryId: "{categoryId}",

                name: "{name}",
                author: "{author}",

                desc: "{desc}",
                order: {order}
            }}
        }}) '''.format(categoryId=categoryId, name=name, author=author, desc=desc, order=order)
        query = self.clearStr(query)
        print(query)
        res = self.databaseAdd(query)
      
        return ''