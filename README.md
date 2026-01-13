# CKMImageNet

## 1. Dataset Overview（数据集概述）
CKMImageNet is an image dataset that incorporates **location-based channel knowledge**. The dataset is categorized by different application scenarios, and each scenario folder contains detailed channel characteristic data and scenario-related information.
CKMImageNet 是一个融合了**基于位置的信道知识**的图像数据集。该数据集按不同应用场景进行分类，每个场景文件夹内包含详细的信道特征数据及场景相关信息。

## 2. Dataset Structure（数据集结构）
### 2.1 Directory Hierarchy（目录层级）

CKMImageNet adopts a 5-layer tree architecture of [Root Directory → Scenario Type → Specific Location → Area → Base Station], where each layer corresponds to the actual directory/data classification of the dataset:

Root: CKMImageNet
The root directory of the dataset, which contains all scenarios, configuration files, and documentation.

Level 1: Scenario Type
Categorized by environment type (e.g., Urban, Rural, Indoor), corresponding to the first-level subfolders in the repository (e.g., Scenario_Urban/).

Level 2: Specific Location
Actual geographic/spatial locations under each scenario (e.g., London, Nanjing under the Urban scenario), corresponding to the second-level subfolders within the scenario folder (e.g., Scenario_Urban/Nanjing/).

Level 3: Area
Divided regions under a single location (e.g., Area1 to Area6), corresponding to the third-level subfolders within the location folder (e.g., Scenario_Urban/Nanjing/Area6/).

Level 4: Base Station (BS)
Base stations within a single area (e.g., BS1 to BS6), corresponding to the fourth-level subfolders within the area folder (e.g., Scenario_Urban/Nanjing/Area6/BS6/). This serves as the core data storage unit of the dataset.

CKMImageNet 采用**「根目录→场景类型→具体地点→区域→基站」**的5层树形架构，每层对应数据集的实际目录/数据分类：
1. **Root: CKMImageNet**  
   数据集根目录，包含所有场景、配置文件与说明文档。
2. **Level 1: Scenario Type（场景类型）**  
   按环境类型划分，如 `Urban`（城市）、`Rural`（乡村）、`Indoor`（室内）等，对应仓库中的一级子文件夹（如 `Scenario_Urban/`）。
3. **Level 2: Specific Location（具体地点）**  
   每个场景下的实际地理/空间地点，如 `Urban` 场景下的 `London`、`Nanjing`，对应场景文件夹内的二级子文件夹（如 `Scenario_Urban/Nanjing/`）。
4. **Level 3: Area（区域）**  
   单个地点下的划分区域（如 `Area1`~`Area6`），对应地点文件夹内的三级子文件夹（如 `Scenario_Urban/Nanjing/Area6/`）。
5. **Level 4: Base Station (BS)（基站）**  
   单个区域内的基站（如 `BS1`~`BS6`），对应区域文件夹内的四级子文件夹（如 `Scenario_Urban/Nanjing/Area6/BS6/`），是数据集的核心数据存储单元

### 2.2 File Description（文件说明）
| 文件/文件夹 | 说明 |
|-------------|------|
| `Scenario_X/` | 按不同场景划分的根文件夹（建议命名为具体场景，如Urban/Indoor/Hilly） |
| `BS/` | 基站（Base Station）覆盖区域相关数据，覆盖范围为400m*100m |
| `area_XX.jpg` | 子区域XX的场景图像（超出部署范围的图像已被删除） |
| `area_XX.json` | 对应子区域的信道知识数据（建议用结构化格式存储） |
| `scenario_view.jpg` | 该场景的整体视图/拓扑图 |
| `params.json` | 该场景的参数配置（如基站位置、频段、采样率等） |

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

This Dataset is developed by Southeast University and Purple Mountain Laboratories. For any further information, please contact Prof. Yong Zeng yong_zeng@seu.edu.cn; Mr. Zijian Wu wuzijian@seu.edu.cn

