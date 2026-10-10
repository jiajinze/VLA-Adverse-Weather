# 数据集索引

> 恶劣天气 + 自动驾驶 相关数据集

## 仿真数据集（推荐入门）

### Adver-City
- **场景**：CARLA仿真，6种天气（clear / soft rain / heavy rain / fog / foggy heavy rain / glare）
- **规模**：24k+帧，890k+标注
- **链接**: https://github.com/quarrg/adver-city
- **特点**: 含LiDAR+RGB+语义相机+GNSS+IMU

### CARLA 恶劣天气
- 官方CARLA + set_weather API
- 适合闭环仿真

## 真实世界数据集

### IDD-AW
- **场景**: 印度复杂路况 + 雨/雾/雪/低光
- **规模**: 5000对图像 + 像素级标注 + NIR
- **链接**: https://iddaw.github.io/
- **特点**: 含近红外配对数据

### K-Radar
- **场景**: 毫米波雷达 + 雨/雪/雾
- **特点**: 恶劣天气下的雷达数据

## 通用自动驾驶数据集（含部分恶劣天气）

| 数据集 | 天气覆盖 | 传感器 | 规模 |
|--------|---------|--------|------|
| nuScenes | 少部分雨夜 | LiDAR+Cam+Rad | 40k帧 |
| Waymo Open | 部分 | LiDAR+Cam | 大 |
| KITTI | 晴为主 | Cam+LiDAR | 中 |

## VLM/MLLM相关

### DrivingContexts
- 1.6M 环境上下文查询对
- 24种环境类别
- 适合VLM微调

### Bench2Drive
- 闭环benchmark
- 多天气覆盖

## 下载指南

每个数据集的详细下载步骤在 `links.md` 中。
