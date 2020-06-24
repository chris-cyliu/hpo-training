# HPO-Training using Dragonfly(multi-obj) & NNI

## Configuration

|   Model   |                           Dataset                            |                      Tuning Parameter*                       | Runtime |
| :-------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :-----: |
|   VGG16   | [Cifar10](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10) (178M) | BATCH_SIZE, LEARNING_RATE, DROP_OUT, DENSE_UNIT, OPTIMIZER, KERNEL_SIZE, TRAIN_STEPS | 700min  |
|  LeNet-5  | [Cifar10 ](https://www.cs.toronto.edu/~kriz/cifar.html)(350M) |          BATCH_SIZE, LEARNING_RATE, NKERN1, NKERN2           |  80min  |
| Inception | [Breeds of Dog](https://www.kaggle.com/careyai/inceptionv3-full-pretrained-model-instructions/data?select=train) (366M) |       BATCH_SIZE, LEARNING_RATE, NUM_EPOCH, DENSE_UNIT       |  10hrs  |
| ResNet50  | [plant_leaves](https://www.tensorflow.org/datasets/catalog/plant_leaves) (6.8G) |             BATCH_SIZE, LEARNING_RATE, NUM_EPOCH             |  12hrs  |

***Tuning Parameter**: include the following hardware parameters by default: ``inter_op_parallelism_threads, intra_op_parallelism_threads, max_folded_constant, build_cost_model, do_common_subexpression_elimination, do_function_inlining, global_jit_level, infer_shapes, place_pruned_graph, enable_bfloat16_sendrecv``

## Performance

|           |    Dragonfly     |       TPE        |    Hyperband    |                            Result                            |                   Cumulative Best accuracy                   |
| :-------: | :--------------: | :--------------: | :-------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|   VGG16   | 0.853 (17min20s) | 0.87 (65min21s)  | 0.826 (6min53s) | ![](https://lh3.googleusercontent.com/-rBBWlBI47ZE/XvMsgNYl7FI/AAAAAAAAAPQ/qQglaGHuxK8H3yBPfsjYLQ8byfXVGvA9QCK8BGAsYHg/s512/2020-06-24.png) | ![](https://lh3.googleusercontent.com/-dnw077p5pCM/Xu8QbwcV73I/AAAAAAAAANk/8W2gsUGNMBYmYmCcBnyPoU6itFGdVjLFgCK8BGAsYHg/s512/2020-06-21.png) |
|  LeNet-5  |  0.645 (1min5s)  | 0.652 (1min21s)  | 0.613 (2min2s)  | ![](https://lh3.googleusercontent.com/-Zwp1028BOks/XvMsZkG6FVI/AAAAAAAAAPM/AgUmmyJH8zUcgdFLUlT8-br0J823nOxKwCK8BGAsYHg/s512/2020-06-24.png) | ![](https://lh3.googleusercontent.com/-Bo22LOKSOO0/XvEEBGtQpVI/AAAAAAAAAOE/FHksoSUg7WcERRFlJPShSQST0ovau7wZACK8BGAsYHg/s512/2020-06-22.png) |
| Inception | 0.878 (32min42s) | 0.866 (15min15s) | 0.889 (32min8s) | ![](https://lh3.googleusercontent.com/-dmCMjiPqu8M/XvMsQgqY5pI/AAAAAAAAAPI/4UxL-CaywQsRJb17bP1S96UcMFaRWAFxQCK8BGAsYHg/s512/2020-06-24.png) | ![](https://lh3.googleusercontent.com/-g7AWvZQ5YF8/Xuu7IxlwPdI/AAAAAAAAAhw/L34Sw9Z0jv0xrg8BRSC9RKfogI3ziXWowCK8BGAsYHg/s512/2020-06-18.png) |
| ResNet50  | 0.924 (77min21s) | 0.923 (75min21s) | 0.886 (67min5s) | ![](https://lh3.googleusercontent.com/-9pIHqTL3Zi0/XvMr-gHilXI/AAAAAAAAAPA/iXxC7JbekYEE1uUDvAMi1p9bL0gz06DnwCK8BGAsYHg/s512/2020-06-24.png) | ![](https://lh3.googleusercontent.com/-0o4gDW65aQ8/Xuu7X9KZ1JI/AAAAAAAAAh4/Zg9fmmxLAAklY1yr509itEPjphfURw5tQCK8BGAsYHg/s512/2020-06-18.png) |

