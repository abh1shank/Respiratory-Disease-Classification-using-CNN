Live App- https://respiratory-disease-classification-using-cnn-jsorfpwjj8enuwech.streamlit.app/
Pneumonia Detection using Convolutional Neural Networks (CNN)
Overview
This project aims to classify chest X-ray images into two classes: pneumonic lungs and non-pneumonic lungs, using Convolutional Neural Networks (CNNs). Pneumonia is a serious lung infection that can be diagnosed through chest X-ray images. By automating the classification process with CNNs, we can assist medical professionals in diagnosing pneumonia more efficiently.

Dataset:
The dataset used in this project consists of chest X-ray images collected from kaggle. It contains images labeled as either "pneumonia" or "normal" (non-pneumonia). The dataset is split into training, validation, and test sets for model training, validation, and evaluation, respectively.

CNN Architecture:
The CNN architecture used for classification consists of multiple convolutional layers followed by max-pooling layers for feature extraction. Dropout layers are added to prevent overfitting, and the final layer uses a sigmoid activation function to output the classification probability.

Training
The model is trained using the training set with data augmentation techniques to improve generalization. Data augmentation includes random rotations, shifts, flips, and zooms to increase the variability of the training data. The model is trained using binary cross-entropy loss and optimized using the RMSprop optimizer.

Evaluation Metrics
After training the model, various evaluation metrics are calculated to assess its performance on the test set. These metrics include:

Accuracy: The proportion of correctly classified samples among all samples.
Precision: The proportion of true positive predictions among all positive predictions. It measures the model's ability to avoid false positives.
Recall (Sensitivity): The proportion of true positive predictions among all actual positive samples. It measures the model's ability to detect positive instances.
F1 Score: The harmonic mean of precision and recall. It provides a balance between precision and recall.
Results
The trained CNN achieved the following performance metrics on the test set:

Accuracy: 78.37333%
Recall: 0.846153
Precision: 0.621468
F1 Score: 0.716612
Confusion Matrix:
<img width="362" alt="image" src="https://github.com/abh1shank/Respiratory-Disease-Classification-using-CNN/assets/97939389/e9f19831-0eb1-42e5-b116-df955ce0ee06">
Conclusion
The CNN classifier demonstrates promising performance in distinguishing between pneumonic and non-pneumonic lungs. With further refinement and validation, it has the potential to be integrated into medical systems for assisting radiologists in diagnosing pneumonia more accurately and efficiently.

