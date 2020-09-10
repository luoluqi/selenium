from src.entity.Shi import Shi

shijing = 'https://so.gushiwen.cn/gushi/shijing.aspx'

chapter = 'https://so.gushiwen.cn/shiwenv_43bde058f758.aspx'

categoryId = 'b05d218a5ec9cabb001a96dd05a4c619'

shi = Shi(shijing, categoryId)
shi.start()
# shi.getChater()