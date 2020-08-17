seed_value = 0
import os, sys
os.environ['PYTHONHASHSEED']=str(seed_value)
#os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'
import numpy as np
np.random.seed(seed_value)
import tensorflow as tf
tf.compat.v1.set_random_seed(seed_value)
import random
random.seed(seed_value)

import logging
from tensorflow.keras import Model
from tensorflow.keras.callbacks import Callback
from tensorflow.keras.layers import (Conv2D, Dense, Dropout, Flatten, MaxPool2D)
from tensorflow.keras.optimizers import Adam,SGD,RMSprop
from dragonfly import load_config, multiobjective_maximise_functions,multiobjective_minimise_functions
from dragonfly import maximise_function,minimise_function
from dragonfly.utils.option_handler import get_option_specs, load_options
import time


_logger = logging.getLogger('cifar10_example')
_logger.setLevel(logging.INFO)


def my_init(shape, dtype=None):
    return tf.random.normal(shape, dtype=dtype)

class create_model(Model):
    """
    LeNet-5 Model with customizable hyper-parameters
    """
    def __init__(self, filter1,filter2,dense):
        """
        Initialize hyper-parameters.
        Parameters
        ----------
        conv_size : int
            Kernel size of convolutional layers.
        hidden_size : int
            Dimensionality of last hidden layer.
        dropout_rate : float
            Dropout rate between two fully connected (dense) layers, to prevent co-adaptation.
        """
        super().__init__()
        self.conv1 = Conv2D(filters=filter1, kernel_size=(9,9), kernel_initializer=my_init,activation='relu')
        self.pool1 = MaxPool2D(pool_size=2)
        self.conv2 = Conv2D(filters=filter2, kernel_size=(5,5), kernel_initializer=my_init,activation='relu')
        self.pool2 = MaxPool2D(pool_size=2)
        self.flatten = Flatten()
        self.fc1 = Dense(units=dense, activation='relu',kernel_initializer=my_init)
        self.fc2 = Dense(units=10, activation='softmax')

    def call(self, x):
        """Override ``Model.call`` to build LeNet-5 model."""
        x = self.conv1(x)
        x = self.pool1(x)
        x = self.conv2(x)
        x = self.pool2(x)
        x = self.flatten(x)
        x = self.fc1(x)
        return self.fc2(x)



def load_dataset():
    """Download and reformat MNIST dataset"""
    cifar10 = tf.keras.datasets.cifar10
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    return (x_train, y_train), (x_test, y_test)


def runtime_eval(x):
    print("dragonfly selected params!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(x)
    (x_train, y_train), (x_test, y_test) = load_dataset()

    model = create_model(filter1=x[0],filter2=x[1],dense=x[2])

    op_type = x[3]
    if op_type == 'adam':
        model.compile(loss='sparse_categorical_crossentropy',
                optimizer=Adam(lr=x[4]),
                metrics=['accuracy'])
    elif op_type == 'sgd':
        model.compile(loss='sparse_categorical_crossentropy',
                optimizer=SGD(learning_rate=x[4]),
                metrics=['accuracy'])
    else:
        model.compile(loss='sparse_categorical_crossentropy',
                optimizer=RMSprop(learning_rate=x[4]),
                metrics=['accuracy'])


    # optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate=x[0])


    # model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    
    sess =  tf.compat.v1.Session(config=tf.compat.v1.ConfigProto( 
		inter_op_parallelism_threads=x[7],
		intra_op_parallelism_threads=x[8],
		graph_options=tf.compat.v1.GraphOptions(
		    infer_shapes=x[9],
		    place_pruned_graph=x[10],
		    enable_bfloat16_sendrecv=x[11],
		    optimizer_options=tf.compat.v1.OptimizerOptions(
		        do_common_subexpression_elimination=x[12],
		        max_folded_constant_in_bytes=x[13],
		        do_function_inlining=x[14],
		        global_jit_level=x[15]))
	))
    tf.compat.v1.keras.backend.set_session(sess)

    start_time = time.time()
    history = model.fit(
        x_train,
        y_train,
        batch_size=x[5],
        epochs=x[6],
        verbose=2,
        validation_data=(x_test, y_test)
    )
    
    # print(history.history)
    end_time = time.time()

    global final_acc
    final_acc =  history.history['val_accuracy'][x[6] - 1]
    spent_time = (start_time - end_time) / 3600.0
    return float(spent_time)


def acc_eval(x):
    global final_acc
    return float(final_acc)


final_acc = 0.0


#model para
N1_list = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30]
N2_list = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 60]
dense_list = [16,32,64,128,256,512,1024]
optimizer_list = ['adam','sgd','rmsp']
LR_list = [5e-1,2.5e-1,1e-1,5e-2,2.5e-2,1e-2,5e-3,2.5e-3,1e-3,5e-4,2.5e-4,1e-4,5e-5,2.5e-5,1e-5]
# LR_list = [1e-4]
batch_list = [10,20,40,80,160,320,400,480,560,640,720,800]
epoch_list = [10,20,30,40,50,60,70,80,90,100]

#hardware para
inter_list = [1,2,3,4]
intra_list = [2,4,6,8,10,12]
infer_shapes_list = [True,False]
place_pruned_graph_list = [True,False]
enable_bfloat16_sendrecv_list = [True,False]
do_common_subexpression_elimination_list = [True,False]
max_folded_constant_list = [2,4,6,8,10]
do_function_inlining_list = [True,False]
global_jit_level_list = [0,1,2]


domain_vars = [{'type': 'discrete_numeric', 'items': N1_list},
                {'type': 'discrete_numeric', 'items': N2_list},
                {'type': 'discrete_numeric', 'items': dense_list},
                {'type': 'discrete', 'items': optimizer_list},
                {'type': 'discrete_numeric', 'items': LR_list},
                {'type': 'discrete_numeric', 'items': batch_list},
                {'type': 'discrete_numeric', 'items': epoch_list},
				{'type': 'discrete_numeric', 'items': inter_list},
                {'type': 'discrete_numeric', 'items': intra_list},
                {'type': 'discrete', 'items': infer_shapes_list},
                {'type': 'discrete', 'items': place_pruned_graph_list},
                {'type': 'discrete', 'items': enable_bfloat16_sendrecv_list},
                {'type': 'discrete', 'items': do_common_subexpression_elimination_list},
                {'type': 'discrete_numeric', 'items': max_folded_constant_list},
                {'type': 'discrete', 'items': do_function_inlining_list},
                {'type': 'discrete_numeric', 'items': global_jit_level_list},
                ]

dragonfly_args = [ 
	get_option_specs('report_results_every', False, 2, 'Path to the json or pb config file. '),
	get_option_specs('init_capital', False, None, 'Path to the json or pb config file. '),
	get_option_specs('init_capital_frac', False, 0.001, 'Path to the json or pb config file. '),
	get_option_specs('num_init_evals', False, 2, 'Path to the json or pb config file. ')]
options = load_options(dragonfly_args)
config_params = {'domain': domain_vars}
config = load_config(config_params)
max_num_evals = 60 * 60 * 10
moo_objectives = [runtime_eval, acc_eval]
pareto_opt_vals, pareto_opt_pts, history = multiobjective_maximise_functions(moo_objectives, config.domain,max_num_evals,capital_type='realtime',config=config,options=options)
f = open("./output.log","w+")
print(pareto_opt_pts,file=f)
print("\n",file=f)
print(pareto_opt_vals,file=f)
print("\n",file=f)
print(history,file=f)