# HPO-Training

## Summary for Training on Dragonfly(2-obj) & NNI(1-obj)

| Model     | Dataset                                                      | Performance                                                  | Cumulative Best Performance                                  | NNI Best Performance | Dragonfly Best Performance |
| --------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------- | -------------------------- |
| VGG16     | [Cifar10](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10)(178M) | ![](https://lh3.googleusercontent.com/-x7V_k0oEr8s/XtiqW3KHnnI/AAAAAAAAAgI/z057EInnRWk6V2bYC_BlpmrG5eFL8n-YQCK8BGAsYHg/s512/2020-06-04.png) | ![](https://lh3.googleusercontent.com/-rMGcBHQEsFw/XtiqUi4y5II/AAAAAAAAAgE/asQ5o1LWnjwZXpCfKpxJfjqGSLwGxRHYACK8BGAsYHg/s512/2020-06-04.png) |                      | 0.853<br />17min20s        |
| LeNet-5   | [Cifar10](https://www.cs.toronto.edu/~kriz/cifar.html)(350M) | ![](https://lh3.googleusercontent.com/-0-NaPdza01M/Xt4WLcM51wI/AAAAAAAAAgg/redm3s_8Mus5G9kHOWhJDGnP4WOGY_K1ACK8BGAsYHg/s512/2020-06-08.png) | ![](https://lh3.googleusercontent.com/-K80sbMLMA4w/Xt4WNCdq5mI/AAAAAAAAAgk/TmetSc72BKcsHunB3qjav7bcTybYewk3ACK8BGAsYHg/s512/2020-06-08.png) |                      | 0.645<br />0min65s         |
| Inception | [Dog Classification](https://www.kaggle.com/careyai/inceptionv3-full-pretrained-model-instructions/data?select=train)(366M) | ![](https://lh3.googleusercontent.com/-hCI1XTyzvJM/XuYwba1Oo7I/AAAAAAAAAM0/YvStAYPpcmoB66N1oW8B111IpAL8cOE6QCK8BGAsYHg/s512/2020-06-14.png) | ![](https://lh3.googleusercontent.com/-05rXHv9TsjU/XuYwZn1O4fI/AAAAAAAAAMw/n-vSgQjmg2sOMP9UnROnCwh7IUVTrNorwCK8BGAsYHg/s512/2020-06-14.png) |                      | 0.878<br />32min42s        |
| ResNet50  | [plant_leaves](https://www.tensorflow.org/datasets/catalog/plant_leaves)(6.8G) | ![](https://lh3.googleusercontent.com/-4z_avY4Ffug/XuhPtLRUIxI/AAAAAAAAANA/7XLLw5wh2c0qBwSB5LpIBEgVlYXurXpkgCK8BGAsYHg/s512/2020-06-15.png) | ![](https://lh3.googleusercontent.com/-YUSDvWtoTRc/XuhPu1j0gPI/AAAAAAAAANE/-7HyOqN70GIIm8onRotWT7eHO-BqSp-ZwCK8BGAsYHg/s512/2020-06-15.png) | 0.923<br />75min21s  | 0.924<br />77min21s        |





