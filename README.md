
## Overview

Emotional expressions are behaviors that communicate one’s emotional state or attitude to others, conveyed through both verbal and non-verbal channels. A comprehensive understanding of complex human behavior necessitates an analysis of physical features derived from a multitude of modalities, predominantly those pertaining to the face, voice, and physical gestures. Recent studies in multimodal emotion recognition underscore the necessity of integrating these modalities for a comprehensive analysis of human behavior.

In this project, we introduce a novel approach to audio-visual emotion recognition using the CREMA-D dataset, focusing on enhancing safety and user experience in autonomous vehicles. Our approach investigates advanced feature extraction techniques and fusion strategies, including early, late, and hybrid fusion techniques. We employ pre-trained models, such as VGG19, to extract features from both audio and video modalities, aiming to improve the accuracy of emotion recognition in real-world driving scenarios.

### Key Contributions:
- **Feature Extraction**: Utilizes state-of-the-art models, such as VGG19, for extracting detailed visual features from video frames and mel spectrograms from audio signals.
- **Fusion Techniques**: Applies early fusion techniques by combining audio and video features into a unified representation, enhancing the overall performance of the system.
- **Classification**: Uses Support Vector Machines (SVM) to classify integrated feature vectors into discrete emotion categories.
- **Enhanced Driver Experience**: Aims to go beyond accident prevention by improving driver comfort, reducing stress, and enabling adaptive in-car systems that respond to the driver’s emotional state.

Our results demonstrate significant improvements in emotion recognition accuracy, providing valuable insights into the integration of emotion analysis in automotive systems to enhance safety, comfort, and overall driving experience.

## Introduction

Multimodal emotion detection has gained prominence in recent years due to its potential to enhance the accuracy and robustness of emotion recognition systems. By integrating multiple modalities, including audio and visual data, a more comprehensive understanding of emotional expressions can be achieved by capturing complementary information that may be overlooked when relying on a single modality.

### Dataset

The CREMA-D dataset, comprising 7,442 video and audio files, serves as a valuable resource for investigating multimodal approaches as it includes a diverse range of emotional expressions in both modalities.

### Methodology

1. **Feature Extraction**:
   - **Visual Features**: The Visual Geometry Group 19 (VGG19) convolutional neural network (CNN) is used for extracting detailed visual features from video frames.
   - **Audio Features**: Mel spectrograms, which convert audio signals into visual representations, allow for the application of VGG19 to audio data by resizing the spectrograms to align with the input specifications of the model.

2. **Fusion Techniques**:
   - **Early Fusion**: This involves concatenating or combining features from audio and video data to create a comprehensive, unified representation that capitalizes on the strengths of both modalities.

3. **Classification**:
   - The integrated features are analyzed using machine learning algorithms, specifically Support Vector Machines (SVMs), to classify the data into discrete emotion categories. Cross-validation techniques are employed to evaluate the model’s performance and determine the optimal configuration.


