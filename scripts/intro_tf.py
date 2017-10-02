# se carga TF
import tensorflow as tf
# Creamos el grafo mas simple, siendo este 
graph = tf.get_default_graph()

sess = tf.Session()

x = tf.constant(1.0, name='entrada')
w = tf.Variable(0.8, name='peso')
y = tf.multiply(w, x, name='salida')