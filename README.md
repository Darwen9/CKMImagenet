# CKMImageNet

# CKMImagenet
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://github.com/Darwen9/CKMImagenet/blob/main/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Darwen9/CKMImagenet?style=flat-square&color=61DAFB)](https://github.com/Darwen9/CKMImagenet/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Darwen9/CKMImagenet?style=flat-square&color=36CFC9)](https://github.com/Darwen9/CKMImagenet/network/members)
[![Last Commit](https://img.shields.io/github/last-commit/Darwen9/CKMImagenet?style=flat-square&color=FF7D00)](https://github.com/Darwen9/CKMImagenet/commits/main)


## 1. Dataset Overview（数据集概述）
CKMImageNet is an image dataset that incorporates **location-based channel knowledge**. The dataset is categorized by different application scenarios, and each scenario folder contains detailed channel characteristic data and scenario-related information.
CKMImageNet 是一个融合了**基于位置的信道知识**的图像数据集。该数据集按不同应用场景进行分类，每个场景文件夹内包含详细的信道特征数据及场景相关信息。

## 2. Dataset Structure（数据集结构）
### 2.1 Directory Hierarchy（目录层级）

CKMImageNet adopts a 4-layer tree architecture of [Root Directory → Scenario Type → Specific Location → Area], where each layer corresponds to the actual directory/data classification of the dataset:

Root: CKMImageNet
The root directory of the dataset, which contains all scenarios, configuration files, and documentation.

Level 1: Scenario Type
Categorized by environment type (e.g., Urban, Rural, Indoor), corresponding to the first-level subfolders in the repository (e.g., Scenario_Urban/).

Level 2: Specific Location
Actual geographic/spatial locations under each scenario (e.g., London, Nanjing under the Urban scenario), corresponding to the second-level subfolders within the scenario folder (e.g., Scenario_Urban/Nanjing/).

Level 3: Area
Divided regions under a single location (e.g., Area1 to Area6), corresponding to the third-level subfolders within the location folder (e.g., Scenario_Urban/Nanjing/Area6/).



CKMImageNet 采用**「根目录→场景类型→具体地点→区域」**的4层树形架构，每层对应数据集的实际目录/数据分类：
1. **Root: CKMImageNet**  
   数据集根目录，包含所有场景、配置文件与说明文档。
2. **Level 1: Scenario Type（场景类型）**  
   按环境类型划分，如 `Urban`（城市）、`Rural`（乡村）、`Indoor`（室内）等，对应仓库中的一级子文件夹（如 `Scenario_Urban/`）。
3. **Level 2: Specific Location（具体地点）**  
   每个场景下的实际地理/空间地点，如 `Urban` 场景下的 `London`、`Nanjing`，对应场景文件夹内的二级子文件夹（如 `Scenario_Urban/Nanjing/`）。
4. **Level 3: Area（区域）**  
   单个地点下的划分区域（如 `Area1`~`Area6`），对应地点文件夹内的三级子文件夹（如 `Scenario_Urban/Nanjing/NJ1/`）。


## 3. Channel Knowledge Types
Each subarea file contains the following key channel knowledge:
- **Channel Gain** (信道增益)
- **Propagation Delay** (时延)
- **AOA (Angle of Arrival)** (到达角)
- **AOD (Angle of Departure)** (离开角)


## 4. Citation（引用方式）
If you use this dataset in your research, please cite it as follows:
@article{wu2025ckmimagenet,
  title={CKMImageNet: A Dataset for AI-Based Channel Knowledge Map Towards Environment-Aware Communication and Sensing},
  author={Wu, Zijian and Wu, Di and Fu, Shen and Qiu, Yuelong and Zeng, Yong},
  journal={arXiv preprint arXiv:2504.09849},
  year={2025}
}

### 模块5：添加锚点导航（提升阅读体验，适配长 README）
在 README 顶部（徽章下方）添加锚点导航，方便快速跳转：
```markdown
## Table of Contents
- [1. Dataset Overview](#1-dataset-overview)
- [2. Dataset Structure](#2-dataset-structure)
- [3. Contributor Stats](#3-contributor-stats)
- [4. Data Generation & Preprocessing](#4-data-generation--preprocessing)
- [5. Citation](#5-citation)
- [6. License](#6-license)
- [7. Contact](#7-contact)

This Dataset is developed by Southeast University and Purple Mountain Laboratories. For any further information, please contact Prof. Yong Zeng yong_zeng@seu.edu.cn; Mr. Zijian Wu wuzijian@seu.edu.cn
