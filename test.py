from src.util.Wechat import Wechat

w = Wechat()
id = w.addBook(categoryId='sdf',name="sdfd",author="23423",desc="4444",order=123)
print(id)