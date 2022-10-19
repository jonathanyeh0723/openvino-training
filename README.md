# openvino-training
Keep updating. All the materials to equip you from zero to hero!

The Edge AI training course can be referred to [Edge AI工程師的20堂必修課程- Cupoy](https://www.cupoy.com/openvino-2022)

## Inference Fundamental

Refer to notebook [ov_training_2022_ie_assignment_1.ipynb](https://github.com/jonathanyeh0723/openvino-training/blob/main/ov_training_2022_ie_assignment_1.ipynb)

Google Colab: https://colab.research.google.com/drive/1uwqOZyfsSx96uEl878AIYbWJ0aaCkar2?usp=sharing

Solution notebook can be referred to [here](https://github.com/jonathanyeh0723/openvino-training/blob/main/ov_training_2022_ie_assignment_1_solution.ipynb)

## OpenVINO Runtime - Classification, Object Detection

Refer to notebook [ov_training_2022_ie_assignment_2.ipynb](https://github.com/jonathanyeh0723/openvino-training/blob/main/ov_training_2022_ie_assignment_2.ipynb)

Solution notebook can be referred to [here](https://github.com/jonathanyeh0723/openvino-training/blob/main/ov_training_2022_ie_assignment_2_solution.ipynb)

## OpenVINO Runtime - Benchmark Performance App

Refer to notebook [ov_training_2022_ie_assignment_3.ipynb](https://github.com/jonathanyeh0723/openvino-training/blob/main/ov_training_2022_ie_assignment_3.ipynb)

## OpenVINO™ integration with TensorFlow (Version 2.2.0)

Demo using Google Colab: [My OpenVINO_TensorFlow Integration](https://colab.research.google.com/drive/1K-EjJAaYPZnOHGvzACoGtjmB9s2z6xMr#scrollTo=Hl4Wsjl5UiVl)

This demo trained MNIST using TensorFlow. 

The model architecture is quite straightforward, a flatten layer followed by a 1024 neuros dense layer and a output 10 classes in accordance with MNIST 0 to 9 numbers. A custom callback function is defined so that upon reaching 99% training accuracy the model will stop training instantly to avoid overfitting. 

Once it is done, we grab some data to verify the availability. And furthermore, we saved the validated model and used OpenVINO for inference reconfirmation.

Note the TensorFlow installed version is 2.9.1 and Op (`pip install tensorflow==2.9.1`, `pip install openvino-tensorflow==2.2.0`)

For more information with regards to OpenVINO™ Integration with TensorFlow, visit [here](https://www.intel.com/content/www/us/en/developer/tools/devcloud/edge/build/ovtfoverview.html)

