import es_tensorflow as tf
tensor1 = tf.ones([1,2,3])
print(tensor1)
tensor2 = tf.reshape(tensor1, [2,3,1])
print(tensor2)
tensor3 = tf.reshape(tensor1, [3, -1])
print(tensor3)

with tf.Session() as sess:
    tensor1.eval()