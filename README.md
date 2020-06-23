# HPO-Training

## Summary for Training on Dragonfly(2-obj) & NNI(1-obj)

| Model     | Dataset                                                      | Tuning Parameter                                             | Runtime | Performance                                                  | Cumulative Best Performance                                  | Best Accuracy                                                |
| --------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| VGG16     | [Cifar10](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10) (178M) | BATCH_SIZE, LEARNING_RATE, DROP_OUT, DENSE_UNIT, OPTIMIZER, KERNEL_SIZE, TRAIN_STEPS, Hardware Para* | 700min  | ![](https://lh3.googleusercontent.com/-9KgNHArMQko/Xu8QdcJF1bI/AAAAAAAAANo/jjAY36wB_psk-r5KGuzhUF0CJAEjMk7IgCK8BGAsYHg/s512/2020-06-21.png) | ![](https://lh3.googleusercontent.com/-dnw077p5pCM/Xu8QbwcV73I/AAAAAAAAANk/8W2gsUGNMBYmYmCcBnyPoU6itFGdVjLFgCK8BGAsYHg/s512/2020-06-21.png) | Hyperband: 0.826 (6min53s)<br />TPE: 0.87 (65min21s)<br />Dragonfly: 0.853 (17min20s) |
| LeNet-5   | [Cifar10 ](https://www.cs.toronto.edu/~kriz/cifar.html)(350M) | BATCH_SIZE, LEARNING_RATE, NKERN1, NKERN2, Hardware Para*    | 80min   | ![](https://lh3.googleusercontent.com/-xdO3JhkZkko/XvEEB0tyfvI/AAAAAAAAAOI/rpwCqKfsBks9V-0tOnDHaB1yfOuqEXcpACK8BGAsYHg/s512/2020-06-22.png) | ![](https://lh3.googleusercontent.com/-Bo22LOKSOO0/XvEEBGtQpVI/AAAAAAAAAOE/FHksoSUg7WcERRFlJPShSQST0ovau7wZACK8BGAsYHg/s512/2020-06-22.png) | Hyperband: 0.613 (2min2s)<br />TPE: 0.652 (1min21s)<br />Dragonfly: 0.645 (1min5s) |
| Inception | [Dog Classification](https://www.kaggle.com/careyai/inceptionv3-full-pretrained-model-instructions/data?select=train) (366M) | BATCH_SIZE, LEARNING_RATE, NUM_EPOCH, DENSE_UNIT, Hardware Para* | 10hrs   | ![](https://lh3.googleusercontent.com/-oNUOeGrkn2c/Xuu7HYuFORI/AAAAAAAAAhs/47V_qlgTetA2u-0D-68gkvx9OR5npeTZwCK8BGAsYHg/s512/2020-06-18.png) | ![](https://lh3.googleusercontent.com/-g7AWvZQ5YF8/Xuu7IxlwPdI/AAAAAAAAAhw/L34Sw9Z0jv0xrg8BRSC9RKfogI3ziXWowCK8BGAsYHg/s512/2020-06-18.png) | Hyperband: 0.889 (32min8s)<br />TPE: 0.866 (15min15s)<br />Dragonfly: 0.878 (32min42s) |
| ResNet50  | [plant_leaves](https://www.tensorflow.org/datasets/catalog/plant_leaves) (6.8G) | BATCH_SIZE, LEARNING_RATE, NUM_EPOCH, Hardware Para*         | 12hrs   | ![](https://lh3.googleusercontent.com/-rWZ3VEDWZw4/Xuu7W8zl2tI/AAAAAAAAAh0/Jux00t4_T88yTY44bfTCe7SUPKUsBwpDgCK8BGAsYHg/s512/2020-06-18.png) | ![](https://lh3.googleusercontent.com/-0o4gDW65aQ8/Xuu7X9KZ1JI/AAAAAAAAAh4/Zg9fmmxLAAklY1yr509itEPjphfURw5tQCK8BGAsYHg/s512/2020-06-18.png) | Hyperband: 0.886 (67min5s)<br />TPE: 0.923 (75min21s)<br />Dragonfly: 0.924 (77min21s) |

*Hardware Para: inter_op_parallelism_threads, intra_op_parallelism_threads, max_folded_constant, build_cost_model, do_common_subexpression_elimination, do_function_inlining, global_jit_level, infer_shapes, place_pruned_graph, enable_bfloat16_sendrecv



