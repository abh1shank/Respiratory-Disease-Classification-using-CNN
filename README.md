<h1 style="color: blue;">Pneumonia Detection using Convolutional Neural Networks (CNN)</h1>

<h2 style="color: blue;">Overview</h2>

<p>This project aims to classify chest X-ray images into two classes: pneumonic lungs and non-pneumonic lungs, using Convolutional Neural Networks (CNNs). Pneumonia is a serious lung infection that can be diagnosed through chest X-ray images. By automating the classification process with CNNs, we can assist medical professionals in diagnosing pneumonia more efficiently.</p>

<h2 style="color: blue;">CNN Dataset</h2>

<p>The dataset used in this project consists of chest X-ray images collected from Kaggle. It contains images labeled as either "pneumonia" or "normal" (non-pneumonia). The dataset is split into training, validation, and test sets for model training, validation, and evaluation, respectively.</p>

<h2 style="color: blue;">CNN Architecture</h2>

<p>The CNN architecture used for classification consists of multiple convolutional layers followed by max-pooling layers for feature extraction. Dropout layers are added to prevent overfitting, and the final layer uses a sigmoid activation function to output the classification probability.</p>

<h2 style="color: blue;">Training</h2>

<p>The model is trained using the training set with data augmentation techniques to improve generalization. Data augmentation includes random rotations, shifts, flips, and zooms to increase the variability of the training data. The model is trained using binary cross-entropy loss and optimized using the RMSprop optimizer.</p>

<h2 style="color: blue;">Evaluation Metrics</h2>

<p>After training the model, various evaluation metrics are calculated to assess its performance on the test set. These metrics include:</p>
<ul>
  <li><strong>Accuracy</strong>: The proportion of correctly classified samples among all samples.</li>
  <li><strong>Precision</strong>: The proportion of true positive predictions among all positive predictions. It measures the model's ability to avoid false positives.</li>
  <li><strong>Recall (Sensitivity)</strong>: The proportion of true positive predictions among all actual positive samples. It measures the model's ability to detect positive instances.</li>
  <li><strong>F1 Score</strong>: The harmonic mean of precision and recall. It provides a balance between precision and recall.</li>
</ul>

<h2 style="color: blue;">Results</h2>

<p>The trained CNN achieved the following performance metrics on the test set:</p>
<ul>
  <li><strong>Accuracy</strong>: 78.37333%</li>
  <li><strong>Recall</strong>: 0.846153</li>
  <li><strong>Precision</strong>: 0.621468</li>
  <li><strong>F1 Score</strong>: 0.716612</li>
</ul>
<p>Confusion Matrix:</p>
<p><img width="362" alt="image" src="https://github.com/abh1shank/Respiratory-Disease-Classification-using-CNN/assets/97939389/e9f19831-0eb1-42e5-b116-df955ce0ee06"></p>

<h2 style="color: blue;">Conclusion</h2>

<p>The CNN classifier demonstrates promising performance in distinguishing between pneumonic and non-pneumonic lungs. With further refinement and validation, it has the potential to be integrated into medical systems for assisting radiologists in diagnosing pneumonia more accurately and efficiently.</p>
