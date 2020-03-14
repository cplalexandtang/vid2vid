# Training & Testing
## Project Implementation
### Background

* Given a series of annotations, Vid2Vid, a GAN, can generate a photorealistic video

* E.g. Street scene generation, edge to face

### Our Goal

* Use GTA5 Dataset to generate photorealistic cityscape video

### Input & Output

* Input : GTA5 dataset's street scence annotations
* Output : Photorealistic video/frames

### Training Process

* Start from the pretrained conditional GAN model
* Manually pick 250 out of 2500 frames from GTA5 dataset, forming 25 sequences
* Clip the Cityscape dataset to 10 frames/sequence
* Training data:
    * 25*k sequences from cityscape dataset (k >= 1)
    * 25 sequences from GTA5 dataset
    * Tried different k to find the best one
* Single K80 GPU, each resolution with 100 epochs

## Requirements

1. Nvidia GPU environment with `nvidia-smi` driver installed

## Install

1. Build Docker

        $ cd vid2vid/docker
        $ docker build -t <img_name> .

2. Run Docker environment

        $ docker run --gpus all --shm-size 8G --name adl_env -itd -v $(pwd)/vid2vid:/vid2vid <img_name> bash
        $ docker exec -it adl_env bash

        ### ... In the container ... ###

3. Testing (Inside container)

    a. Download dataset: https://drive.google.com/file/d/11pjTlcsAnrwMDbDfTei-MZ8gCRx6xxQ3/view?usp=sharing

    b. Place the images to ~/vid2vid/datasets/gtaCity/test_A

    c. Download model

        # python ./scripts/download_mymodel.py

    d. Run testing code

        # ./scripts/street/test_2048.sh

    e. A video `output.mp4` will be generated

4. Training (Inside container)

    a. Train the low-resolution model

        # ./scripts/street/train_g1_256.sh

    b. Train the mid-resolution model

        # ./scripts/street/train_g1_512.sh
        # ./scripts/street/train_512.sh

    c. Train 1024 HD model

        # ./scripts/street/train_g1_1024.sh
        # ./scripts/street/train_1024.sh

    d. Train 2048px model

        # ./scripts/street/train_2048.sh

    e. Run testing code as mentioned above