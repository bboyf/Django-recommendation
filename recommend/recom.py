import findspark
findspark.init()
import redis
from pyspark import SparkContext
from pyspark.mllib.recommendation import MatrixFactorizationModel
from . import train

def getRecommendByUserId(userid, rec_num):
    train.train()
    print("模型训练完毕并保存")
    """
    :param userid: 用户id
    :param rec_num: 推荐数量
    """
    try:
        pool = redis.ConnectionPool(host='localhost', port=6379)
        redis_client = redis.Redis(connection_pool=pool)
        sc = SparkContext()
        # 加载模型
        model = MatrixFactorizationModel.load(sc, './recommemdModel')
        # 预测
        result = model.recommendProducts(userid, rec_num)
        temp = ''
        for r in result:
            temp += str(r[0]) + ',' + str(r[1]) + ',' + str(r[2]) + '|'
        # 将结果保存到内存数据库
        print(temp)
        redis_client.set(userid, temp)
        print('load model success!\n')
    except Exception as e:
        print('load model failed!\n' + str(e))
        # print("模型调用并进行预测将结果保存到redis中")
    sc.stop()



# if __name__ == '__main__':
#     train.train()
#     print("模型训练完毕并保存")
#     getRecommendByUserId(2,4)
#     print("模型调用并进行预测将结果保存到redis中")

