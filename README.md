# Can 3DMM seperate identity and expression data?

<p align="center"> 
<workflow src="docs/Workflow.png">
</p>
<p align="center">Overview of the modules and their workflow in the game.<p align="center">


Description

The main features:

* **Reconstruction:** produces head pose, shape, detailed face geometry, and lighting information from a single image.
* **Animation:** animate the face with realistic wrinkle deformations.
* **Robustness:** tested on facial images in unconstrained conditions.  Our method is robust to various poses, illuminations and occlusions. 
* **Accurate:** state-of-the-art 3D face shape reconstruction on the [NoW Challenge](https://ringnet.is.tue.mpg.de/challenge) benchmark dataset.
  
## Getting Started
Clone the repo:
  ```bash
  git clone https://github.com/fenjaWagner/Anwendungspraktikum-SS24.git
  cd src
  ```  

### Requirements
These are the packages and versions used in the programming process. The game might run with older ones. 
* Python 3.12
* pygame 2.6
* numpy 1.26.4
* matplotlib 3.9.1

  
### Usage
To run the game use
```bash
python3 run.py
```

### Config Settings
All necessary setting changes can be implemented through the [configs](src/conf.py).
Conf:
* **detail_modes:** 
* **order:** The order states whether the user is given a processed image and has to choose from unprocessed pictures or vice versa.
* **game_modes:** Sets in which combination images of people with certain characteristics are shown to the user to choose from. 
* **layout:** Layout settings for the game screen

Image_conf:
* **game_modes:** 

## Evaluation
DECA (ours) achieves 9% lower mean shape reconstruction error on the [NoW Challenge](https://ringnet.is.tue.mpg.de/challenge) dataset compared to the previous state-of-the-art method.  
The left figure compares the cumulative error of our approach and other recent methods (RingNet and Deng et al. have nearly identitical performance, so their curves overlap each other). Here we use point-to-surface distance as the error metric, following the NoW Challenge.  
<p align="left"> 
<img src="Doc/images/DECA_evaluation_github.png">
</p>

For more details of the evaluation, please check our [arXiv paper](https://arxiv.org/abs/2012.04012). 

## Training
1. Prepare Training Data

    a. Download image data  
    In DECA, we use [VGGFace2](https://arxiv.org/pdf/1710.08092.pdf), [BUPT-Balancedface](http://www.whdeng.cn/RFW/Trainingdataste.html) and [VoxCeleb2](https://www.robots.ox.ac.uk/~vgg/data/voxceleb/vox2.html)  

    b. Prepare label  
    [FAN](https://github.com/1adrianb/2D-and-3D-face-alignment) to predict 68 2D landmark  
    [face_segmentation](https://github.com/YuvalNirkin/face_segmentation) to get skin mask  

    c. Modify dataloader   
    Dataloaders for different datasets are in decalib/datasets, use the right path for prepared images and labels. 

2. Download face recognition trained model  
    We use the model from [VGGFace2-pytorch](https://github.com/cydonia999/VGGFace2-pytorch) for calculating identity loss,
    download [resnet50_ft](https://drive.google.com/file/d/1A94PAAnwk6L7hXdBXLFosB_s0SzEhAFU/view),
    and put it into ./data  

3. Start training

    Train from scratch: 
    ```bash
    python main_train.py --cfg configs/release_version/deca_pretrain.yml 
    python main_train.py --cfg configs/release_version/deca_coarse.yml 
    python main_train.py --cfg configs/release_version/deca_detail.yml 
    ```
    In the yml files, write the right path for 'output_dir' and 'pretrained_modelpath'.  
    You can also use [released model](https://drive.google.com/file/d/1rp8kdyLPvErw2dTmqtjISRVvQLj6Yzje/view) as pretrained model, then ignor the pretrain step.

## Related works:  
* for better emotion prediction: [EMOCA](https://github.com/radekd91/emoca)  
* for better skin estimation: [TRUST](https://github.com/HavenFeng/TRUST)

## Citation
If you find our work useful to your research, please consider citing:
```
@inproceedings{DECA:Siggraph2021,
  title={Learning an Animatable Detailed {3D} Face Model from In-The-Wild Images},
  author={Feng, Yao and Feng, Haiwen and Black, Michael J. and Bolkart, Timo},
  journal = {ACM Transactions on Graphics, (Proc. SIGGRAPH)}, 
  volume = {40}, 
  number = {8}, 
  year = {2021}, 
  url = {https://doi.org/10.1145/3450626.3459936} 
}
```

<!-- ## Notes
1. Training code will also be released in the future. -->

## License
This code and model are available for non-commercial scientific research purposes as defined in the [LICENSE](https://github.com/YadiraF/DECA/blob/master/LICENSE) file.
By downloading and using the code and model you agree to the terms in the [LICENSE](https://github.com/YadiraF/DECA/blob/master/LICENSE). 

## Acknowledgements
For functions or scripts that are based on external sources, we acknowledge the origin individually in each file.  
Here are some great resources we benefit:  
- [FLAME_PyTorch](https://github.com/soubhiksanyal/FLAME_PyTorch) and [TF_FLAME](https://github.com/TimoBolkart/TF_FLAME) for the FLAME model  
- [Pytorch3D](https://pytorch3d.org/), [neural_renderer](https://github.com/daniilidis-group/neural_renderer), [SoftRas](https://github.com/ShichenLiu/SoftRas) for rendering  
- [kornia](https://github.com/kornia/kornia) for image/rotation processing  
- [face-alignment](https://github.com/1adrianb/face-alignment) for cropping   
- [FAN](https://github.com/1adrianb/2D-and-3D-face-alignment) for landmark detection
- [face_segmentation](https://github.com/YuvalNirkin/face_segmentation) for skin mask
- [VGGFace2-pytorch](https://github.com/cydonia999/VGGFace2-pytorch) for identity loss  

We would also like to thank other recent public 3D face reconstruction works that allow us to easily perform quantitative and qualitative comparisons :)  
[RingNet](https://github.com/soubhiksanyal/RingNet), 
[Deep3DFaceReconstruction](https://github.com/microsoft/Deep3DFaceReconstruction/blob/master/renderer/rasterize_triangles.py), 
[Nonlinear_Face_3DMM](https://github.com/tranluan/Nonlinear_Face_3DMM),
[3DDFA-v2](https://github.com/cleardusk/3DDFA_V2),
[extreme_3d_faces](https://github.com/anhttran/extreme_3d_faces),
[facescape](https://github.com/zhuhao-nju/facescape)
<!-- 3DMMasSTN, DenseReg, 3dmm_cnn, vrn, pix2vertex -->