# IronMask: Deep Neural Network for Voice Recognition

## Overview

"IronMask" is a project focused on developing a deep neural network model for voice recognition. This binary model can identify when the "target" person speaks (outputting a 1) or when any other person speaks (outputting a 0).

## Description

This repository contains all the necessary steps for constructing, training, and saving the model, including audio preprocessing, feature extraction, and storage. The process involves creating a neural network using TensorFlow's sequential model, experimenting with various loss functions and optimizers during training, and finally evaluating the model's performance and saving it.

### Key Terms

- **Deep Neural Network (DNN):** A type of artificial neural network with multiple layers between the input and output layers, capable of capturing complex patterns in data.
- **Binary Model:** A model that provides two possible outputs. In this case, 1 for the target person's voice and 0 for any other person's voice.
- **Sequential Model:** A linear stack of layers in TensorFlow, where each layer has exactly one input tensor and one output tensor.

### Contents

- **Audio Preprocessing:** Steps for cleaning and preparing audio data for training and testing.
- **Feature Extraction:** Methods to extract meaningful features from audio data.
- **Model Construction:** Scripts for building the neural network using TensorFlow's sequential model.
- **Training:** Experiments with different loss functions and optimizers to train the model.
- **Evaluation:** Assessing the model's performance and saving the best-performing model.

### Files and Directories

- **`IronMaskff.py`:** Script for using the trained model to recognize the target voice.
- **`model/`:** Directory containing multiple trained models, with varying performance levels.
- **`IronMaskF.ipynb`:** Jupyter notebook detailing data post-processing, model creation, training, performance evaluation, and model saving.
- **`robotArm/`:** Contains Arduino code to move a robotic arm to a specific position when the target voice is recognized. This arm is intended to be replaced by an IronMan-style mask in the future.

## Usage

1. **Preprocess Audio Data:** Clean and prepare audio files for feature extraction.
2. **Extract Features:** Use the provided scripts to extract relevant features from the audio data.
3. **Build the Model:** Utilize the sequential model in TensorFlow to create the neural network, adding layers as needed.
4. **Train the Model:** Experiment with different loss functions and optimizers to train the model using the collected data.
5. **Evaluate and Save the Model:** Review the model's performance and save the best version.
6. **Deploy the Model:** Use `IronMaskff.py` to recognize the target voice in real-time.

### Future Directions

The current implementation controls a robotic arm based on voice recognition. The ultimate goal is to replace this arm with an IronMan-style mask, from which the project derives its name, "IronMask."
