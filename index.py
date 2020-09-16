from src.entity.Shi import Shi

shijing = 'https://so.gushiwen.cn/gushi/shijing.aspx'

chapter = 'https://so.gushiwen.cn/shiwenv_43bde058f758.aspx'

categoryId = 'b05d218a5ec9cabb001a96dd05a4c619'

tangshi = 'https://so.gushiwen.cn/gushi/tangshi.aspx'

shi = Shi('https://so.gushiwen.cn/gushi/tangshi.aspx', categoryId)
shi.start()

shi = Shi('https://so.gushiwen.cn/gushi/sanbai.aspx', categoryId)
shi.start()

shi = Shi('https://so.gushiwen.cn/gushi/songsan.aspx', categoryId)
shi.start()

shi = Shi('https://so.gushiwen.cn/gushi/songci.aspx', categoryId)
shi.start()

shi = Shi('https://so.gushiwen.cn/gushi/shijiu.aspx', categoryId)
shi.start()

shi = Shi('https://so.gushiwen.cn/gushi/shijing.aspx', categoryId)
shi.start()

shi = Shi('https://so.gushiwen.cn/gushi/chuci.aspx', categoryId)
shi.start()




# shi.getChater()