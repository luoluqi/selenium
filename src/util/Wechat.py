import requests
import json

class Wechat():
    appId = 'wx5da44835dac1892e'
    appSecret = '6e75d11d9964510f2d86218839ffe1c9'
    env = 'book-e9sdz'
    # env = 'test-bggil'
    access_token = ''

    def __init__(self):
        pass

    def clearStr(self, str):
        str = str.replace('\r', '')
        str = str.replace('\n', '')
        # str = str.replace('"', '\'')
        str = str.replace('"', '\\\\"')
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
       
        return res.json()

    def addCategory(self, *args, name, order):
        query = '''
        db.collection('category').add({{
            data: {{
                name: "{name}",
                order: {order}
            }}
        }})
        '''
        query = query.format(name=name, order=order)

        res = self.databaseAdd(query)
        return res['id_list'][0]

    def addBook(self,*args, categoryId, name, author, desc, order):
        desc = self.clearStr(desc)
        query = '''
        db.collection('book').add({{
            data: {{
                categoryId: "{categoryId}",
                name: "{name}",
                author: "{author}",
                desc: "{desc}",
                order: {order}
            }}
        }}) '''.format(categoryId=categoryId, name=name, author=author, desc=desc, order=order)
       
        res = self.databaseAdd(query)
        print('add book', res)
        return res['id_list'][0]

    def addChapter(self, *args, bookId, name, original, translation, order):
        original = self.clearStr(original)
        translation = self.clearStr(translation)

        query = '''
        db.collection('chapter').add({{
            data: {{
                bookId: "{bookId}",
                name: "{name}",
                original: "{original}",
                translation: "{translation}",
                order: {order}
            }}
        }})
        '''
        query = query.format(bookId=bookId, name=name, original=original, translation=translation\
            , order=order)
        res = self.databaseAdd(query)
        print(query)
        print('add chapter', res)
        # return res['id_list'][0]

    def removeBook(self,*args, bookId):
        token = self.getAccessToken()
        query = 'db.collection("book").doc("{bookId}").remove()'
        query = query.format(bookId=bookId)
        data = json.dumps({
            'env': self.env,
            'query': query
        })
        url = 'https://api.weixin.qq.com/tcb/databasedelete?access_token={}'.format(token)
        headers = {'content-type': 'application/json'}
        res = requests.post(url, data=data, headers=headers)

        query = 'db.collection("chapter").where({{bookId:"{bookId}"}}).remove()'
        query = query.format(bookId=bookId)
        data = json.dumps({
            'env': self.env,
            'query': query
        })
        url = 'https://api.weixin.qq.com/tcb/databasedelete?access_token={}'.format(token)
        headers = {'content-type': 'application/json'}
        res = requests.post(url, data=data, headers=headers)