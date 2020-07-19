import wx
import wx.xrc
from skimage import io, transform
import tensorflow as tf
import numpy as np
import cv2

class Module:
    def __init__(self):
        self.fruit_dict = {0: '苹果', 1: '香蕉', 2: '橙子'}
        self.w = 100
        self.h = 100
        self.c = 3

    # 读取图片
    def read_image(self, path):
        img = io.imread(path)
        img = transform.resize(img, (self.w, self.h))
        return np.asarray(img)

    # 识别图片
    def classification(self, path):
        with tf.compat.v1.Session() as sess:
            data = list()
            data1 = self.read_image(path) #read message 读取图片  这里是主要的接口代码 
            data.append(data1)
            saver = tf.compat.v1.train.import_meta_graph('./module//model.meta')
            saver.restore(sess, tf.train.latest_checkpoint('./module/'))
            graph = tf.compat.v1.get_default_graph()
            x = graph.get_tensor_by_name("x:0")
            feed_dict = {x: data}
            logits = graph.get_tensor_by_name("logits_tag:0")
            classification_result = sess.run(logits, feed_dict)
            # 预测矩阵
            print(classification_result)
            # 预测矩阵每一行最大值的索引
            print(tf.argmax(classification_result, 1).eval())
            # 得到索引对应水果的分类
            output = tf.argmax(classification_result, 1).eval()
            result = self.fruit_dict[output[0]]
        return result



if __name__ == '__main__':
    test = Module()
    Theresult = test.classification("./init.jpg")
    print(Theresult)

