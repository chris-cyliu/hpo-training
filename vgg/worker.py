from __future__ import absolute_import, division, print_function, unicode_literals

import json
import os

import tensorflow as tf
import tensorflow_datasets as tfds
from numpy.random import seed
from tensorflow.keras.initializers import glorot_uniform
import nni
import shutil
import time


def preprocess(image, label):
    image = tf.cast(image, tf.float32)
    image = tf.image.grayscale_to_rgb(image)
    image = (image / 127.5) - 1
    image = tf.image.resize(image, (IMG_SIZE, IMG_SIZE))
    return image, label


def train_input_fn(batch_size, dataset):
    data = tfds.load(dataset, as_supervised=True)
    train_data = data['train']
    train_data = train_data.map(preprocess).batch(batch_size)
    return train_data


def get_default_params():
    return {
        "BATCH_SIZE":32,
        "LEARNING_RATE":1e-1,
        "DROP_OUT":5e-1,
        "DENSE_UNIT":128,
        "OPTIMIZER":"grad",
        "KERNEL_SIZE":3,
        "inter_op_parallelism_threads":1,
        "intra_op_parallelism_threads":2,
        "max_folded_constant":6,
        "build_cost_model":4
    }


def model_fn(features, labels, mode):
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(input_shape=(IMG_SIZE, IMG_SIZE, 3), filters=64, kernel_size=(KS, KS), padding="same",
                               activation="relu", kernel_initializer='zeros'),
        tf.keras.layers.Conv2D(filters=64, kernel_size=(KS, KS), padding="same", activation="relu",
                               kernel_initializer='zeros'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
        tf.keras.layers.Conv2D(filters=128, kernel_size=(KS, KS), padding="same", activation="relu",
                               kernel_initializer='zeros'),
        tf.keras.layers.Conv2D(filters=128, kernel_size=(KS, KS), padding="same", activation="relu",
                               kernel_initializer='zeros'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
        tf.keras.layers.Conv2D(filters=256, kernel_size=(KS, KS), padding="same", activation="relu",
                               kernel_initializer='zeros'),
        tf.keras.layers.Conv2D(filters=256, kernel_size=(KS, KS), padding="same", activation="relu",
                               kernel_initializer='zeros'),
        tf.keras.layers.Conv2D(filters=256, kernel_size=(KS, KS), padding="same", activation="relu",
                               kernel_initializer='zeros'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
        tf.keras.layers.Conv2D(filters=512, kernel_size=(KS, KS), padding="same", activation="relu",
                               kernel_initializer='zeros'),
        tf.keras.layers.Conv2D(filters=512, kernel_size=(KS, KS), padding="same", activation="relu",
                               kernel_initializer='zeros'),
        tf.keras.layers.Conv2D(filters=512, kernel_size=(KS, KS), padding="same", activation="relu",
                               kernel_initializer='zeros'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
        tf.keras.layers.Conv2D(filters=512, kernel_size=(KS, KS), padding="same", activation="relu",
                               kernel_initializer='zeros'),
        tf.keras.layers.Conv2D(filters=512, kernel_size=(KS, KS), padding="same", activation="relu",
                               kernel_initializer='zeros'),
        tf.keras.layers.Conv2D(filters=512, kernel_size=(KS, KS), padding="same", activation="relu",
                               kernel_initializer='zeros'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(units=DENSE_UNIT, activation="relu", kernel_initializer='zeros'),
        tf.keras.layers.Dense(units=DENSE_UNIT, activation="relu", kernel_initializer='zeros'),
        tf.keras.layers.Dropout(DROP_OUT),
        tf.keras.layers.Dense(units=12, activation="softmax")
    ])

    logits = model(features, training=True)

    if mode == tf.estimator.ModeKeys.PREDICT:
        predictions = {'logits': logits}
        return tf.estimator.EstimatorSpec(labels=labels, predictions=predictions)

    if OPTIMIZER == 'adam':
        optimizer = tf.compat.v1.train.AdamOptimizer(learning_rate=LEARNING_RATE)
    elif OPTIMIZER == 'grad':
        optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate=LEARNING_RATE)
    elif OPTIMIZER == 'rmsp':
        optimizer = tf.compat.v1.train.RMSPropOptimizer(learning_rate=LEARNING_RATE)

    loss = tf.keras.losses.SparseCategoricalCrossentropy(
        from_logits=True, reduction=tf.losses.Reduction.NONE)(labels, logits)
    loss = tf.reduce_sum(loss) * (1. / BATCH_SIZE)
    if mode == tf.estimator.ModeKeys.EVAL:
        return tf.estimator.EstimatorSpec(mode, loss=loss)

    class NNIReportHook(tf.train.SessionRunHook):
        def __init__(self, loss):
            self.loss = loss

        def before_run(self, run_context):
            return tf.estimator.SessionRunArgs(self.loss)

        def after_run(self, run_context, run_values):
            self.result = run_values.results
            nni.report_intermediate_result(-self.result)

        def end(self,session):
            nni.report_final_result(-self.result)

    return tf.estimator.EstimatorSpec(
        mode=mode,
        loss=loss,
        train_op=optimizer.minimize(
            loss, tf.compat.v1.train.get_or_create_global_step()),
        training_hooks=[NNIReportHook(loss)])


def make_stop_fn():
    # Stop trial if runtime > 20min
    current_time = time.time()
    if current_time - START_TIME > 60 * 20:
        return True
    else:
        return False

seed(0)
tf.compat.v1.random.set_random_seed(0)
tf.compat.v1.disable_eager_execution()
tfds.disable_progress_bar()
BUFFER_SIZE = 10000

params = get_default_params()
received_params = nni.get_next_parameter()
params.update(received_params)
BATCH_SIZE = int(params['BATCH_SIZE'])
LEARNING_RATE = params['LEARNING_RATE']
DROP_OUT = int(params['DROP_OUT'])
DENSE_UNIT = int(params['DENSE_UNIT'])
OPTIMIZER = params['OPTIMIZER']
KS = int(params['KERNEL_SIZE'])
START_TIME = time.time()

IMG_SIZE = 48  # All images will be resized to IMG_SIZE*IMG_SIZE
# 160 for cats_vs_dogs(input_shape:None, None, 3); 28 for mnist(input_shape:28, 28, 1)
IMG_CLASS = 10

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.INFO)
FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('dataset', 'mnist', 'specify dataset')
tf.app.flags.DEFINE_string('model_dir', './estimator-original', 'model_dir')
tf.app.flags.DEFINE_integer('save_ckpt_steps', 150, 'save ckpt per n steps')
tf.app.flags.DEFINE_integer('train_steps', 150, 'train_steps')


my_config = tf.ConfigProto( 
    inter_op_parallelism_threads=int(params['inter_op_parallelism_threads']),
    intra_op_parallelism_threads=int(params['intra_op_parallelism_threads']),
    graph_options=tf.GraphOptions(
        build_cost_model=int(params['build_cost_model']),
        optimizer_options=tf.OptimizerOptions(max_folded_constant_in_bytes=int(params['max_folded_constant']))))

config = tf.estimator.RunConfig(save_checkpoints_steps=FLAGS.save_ckpt_steps,
                                save_checkpoints_secs=None,
                                log_step_count_steps=1,
                                session_config=my_config)

classifier = tf.estimator.Estimator(
    model_fn=model_fn, model_dir=FLAGS.model_dir, config=config)
early_stop_hook = tf.compat.v1.estimator.experimental.make_early_stopping_hook(classifier, should_stop_fn=make_stop_fn)

tf.estimator.train_and_evaluate(
    classifier,
    train_spec=tf.estimator.TrainSpec(input_fn=lambda: train_input_fn(BATCH_SIZE, FLAGS.dataset), max_steps=FLAGS.train_steps, hooks=[early_stop_hook]),
    eval_spec=tf.estimator.EvalSpec(input_fn=lambda: train_input_fn(BATCH_SIZE, FLAGS.dataset), steps=10)
)

# Delete the checkpoint and summary for next trial
if os.path.exists(FLAGS.model_dir):
    shutil.rmtree(FLAGS.model_dir)