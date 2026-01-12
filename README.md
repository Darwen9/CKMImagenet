# CKMImageNet
[![GitHub License](https://img.shields.io/github/license/your-username/CKMImageNet?style=flat-square&color=blue)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/your-username/CKMImageNet?style=flat-square&color=yellow)](https://github.com/your-username/CKMImageNet/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/your-username/CKMImageNet?style=flat-square&color=green)](https://github.com/your-username/CKMImageNet/network/members)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/your-username/CKMImageNet?style=flat-square&color=orange)](https://github.com/your-username/CKMImageNet/commits/main)
<!-- 可选：添加数据集大小徽章，需自己计算大小 -->
[![Dataset Size](https://img.shields.io/badge/dataset%20size-XX%20GB-blueviolet?style=flat-square)](https://github.com/your-username/CKMImageNet)

[![GitHub License](https://img.shields.io/github/license/your-username/CKMImageNet)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/your-username/CKMImageNet)](https://github.com/your-username/CKMImageNet/stargazers)

## 1. Dataset Overview（数据集概述）
CKMImageNet is an image dataset that incorporates **location-based channel knowledge**. The dataset is categorized by different application scenarios, and each scenario folder contains detailed channel characteristic data and scenario-related information.

> 中文说明（可选，方便中文用户）：  
> CKMImageNet 是一个融合了**基于位置的信道知识**的图像数据集。该数据集按不同应用场景进行分类，每个场景文件夹内包含详细的信道特征数据及场景相关信息。

## 2. Dataset Structure（数据集结构）
### 2.1 Directory Hierarchy（目录层级）


### 2.2 File Description（文件说明）
| 文件/文件夹 | 说明 |
|-------------|------|
| `Scenario_X/` | 按不同场景划分的根文件夹（建议命名为具体场景，如Urban/Indoor/Hilly） |
| `BS/` | 基站（Base Station）覆盖区域相关数据，最多包含81张图像（对应81个部分重叠的子区域） |
| `area_XX.jpg` | 子区域XX的场景图像（超出部署范围的图像已被删除） |
| `area_XX.json` | 对应子区域的信道知识数据（建议用结构化格式存储） |
| `scenario_view.jpg` | 该场景的整体视图/拓扑图 |
| `params.json` | 该场景的参数配置（如基站位置、频段、采样率等） |

## 3. Key Channel Knowledge（核心信道知识）
Each subarea file contains the following key channel parameters:
- **Channel Gain** (信道增益)：信号在信道传输中的功率增益/损耗
- **AOA (Angle of Arrival)** (到达角)：信号到达接收端的角度
- **AOD (Angle of Departure)** (离开角)：信号从发射端离开的角度
- Other parameters (其他参数)：可补充你数据集包含的其他信道特征

## 4. Data Collection & Preprocessing（数据采集与预处理）
（可选，补充数据集的采集方法、预处理流程，例如：）
- The BS coverage area is divided into 81 partially overlapping subareas based on grid division.
- Images and channel data beyond the effective deployment range are filtered out to ensure data validity



## 5. Citation（引用方式）
If you use this dataset in your research, please cite it as follows:
```bibtex
@misc{CKMImageNet2026,
  author = {Your Name},
  title = {CKMImageNet: An Image Dataset with Location-based Channel Knowledge},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/your-username/CKMImageNet}}
}



























This Dataset is developed by Southeast University and Purple Mountain Laboratories. For any further information, please contact Prof. Yong Zeng yong_zeng@seu.edu.cn; Mr. Zijian Wu wuzijian@seu.edu.cn

[1]D. Wu, Z. Wu, Y. Qiu, S. Fu, and Y. Zeng, “CKMImageNet: A comprehensive dataset to enable channel knowledge map construction via computer vision,” in 2024 IEEE/CIC Int. Conf. Commun. China (ICCC Workshops), 2024, pp. 114–119.

Related works of our group are listed as follows:

 Y. Zeng, J. Chen, J. Xu, D. Wu, X. Xu, S. Jin, X. Gao, D. Gesbert, S. Cui, and R. Zhang, “A tutorial on environment-aware communications via channel knowledge map for 6G,” IEEE Commun. Surv. Tutorials, pp. 1–1, 2024.
 
 Y. Zeng and X. Xu, “Toward environment-aware 6G communications via channel knowledge map,” IEEE Wireless Commun., vol. 28, no. 3, pp. 84–91, 2021.
 
 X. Xu and Y. Zeng, "How Much Data Is Needed for Channel Knowledge Map Construction?" in IEEE Transactions on Wireless Communications, vol. 23, no. 10, pp. 13011-13021, Oct. 2024.
 
 K. Li, P. Li, Y. Zeng, and J. Xu, “Channel knowledge map forenvironment-aware communications: EM algorithm for map construction,” in 2022 IEEE Wireless Communications and Networking Confer-ence (WCNC), 2022, pp. 1659–1664.
 
 S. Fu, Z. Wu, D. Wu, and Y. Zeng, “Generative CKM construction using partially observed data with diffusion model,” 2024. [Online]. Available: https://arxiv.org/abs/2412.14812.
 
 D. Wu, Y. Zeng, S. Jin, and R. Zhang, “Environment-aware hybrid beamforming by leveraging channel knowledge map,” IEEE Trans. Wireless Commun., 2023.
 
 Z. Xu, Z. Zhou, D. Wu and Y. Zeng, "Channel Knowledge Map-Enhanced Clutter Suppression for Integrated Sensing and Communication," 2024 IEEE/CIC International Conference on Communications in China (ICCC Workshops), Hangzhou, China, 2024, pp. 90-95.
 
 Y. Long, Y. Zeng, X. Xu, and Y. Huang, “Environment-Aware Wireless Localization Enabled by Channel Knowledge Map,” IEEE Globecom 2022.
 
 S. Zeng, X. Xu, Y. Zeng, and F. Liu, “CKM-assisted LoS identification and predictive beamforming for cellular-connected UAV,” IEEE ICC 2023.
 
 Y. Qiu, D. Wu and Y. Zeng, "CKM-Based Environment-Aware Pilot Reuse and Channel Estimation," 2024 16th International Conference on Wireless Communications and Signal Processing (WCSP), Hefei, China, 2024, pp. 169-174.
 
 D. Wu, Y. Qiu, Y. Zeng and F. Wen, "Environment-Aware Channel Estimation via Integrating Channel Knowledge Map and Dynamic Sensing Information," in IEEE Wireless Communications Letters, vol. 13, no. 12, pp. 3608-3612, Dec. 2024, doi: 10.1109/LWC.2024.3482357.
 
 D. Wu and Y. Zeng, "Environment-Aware Coordinated Multi-Point mmWave Beam Alignment Via Channel Knowledge Map," 2023 IEEE International Conference on Communications Workshops (ICC Workshops), Rome, Italy, 2023, pp. 1044-1049, doi 10.1109/ICCWorkshops57953.2023.10283607.
 
 Z. Dai, D. Wu, Z. Dong and Y. Zeng, “Prototyping and experimental results for environment-aware millimeter wave beam alignment via channel knowledge map,” in IEEE Transactions on Vehicular Technology, vol. 73, no. 11, pp. 16805-16816, Nov. 2024
 
 C. Zhang, Z. Zhou, X. Xu, Y. Zeng, Z. Zhang and S. Jin, "Prototyping and Experimental Results for ISAC-based Channel Knowledge Map," in IEEE Transactions on Vehicular Technology, doi: 10.1109/TVT.2025.3545785.

 S. Fu, Z. Wu, D. Wu, and Y. Zeng, “Generative CKM construction using partially observed data with diffusion model,” arXiv preprint arXiv:2412.14812, 2024.
 
 Z. Dai, D. Wu, X. Xu, and Y. Zeng, “Generating CKM using others’ data: Cross-AP CKM inference with deep learning,” arXiv preprint arXiv:2411.17716, 2024.

 S. Wang, X. Xu, and Y. Zeng, “Deep learning-based CKM construction with image super-resolution,” arXiv preprint arXiv:2411.08887, 2024.
