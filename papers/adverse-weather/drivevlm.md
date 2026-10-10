# DriveVLM (CoRL 2024)

**全名**: DriveVLM: The Convergence of Autonomous Driving and Large Vision-Language Models

**作者/机构**: 清华MARS Lab + 玄玑 + Pegasus Tech

**链接**: https://arxiv.org/abs/2402.12289

## 核心一句话

> 用VLM做"层次化驾驶规划"，**显式把天气作为输入**。

## 问题

复杂城市场景+长尾场景，传统pipeline做不好。

## 方案

```
Chain-of-Thought:
1. Scene Description (含天气 E_weather)
2. Scene Analysis
3. Hierarchical Planning
```

**天气模块**：E_weather ∈ {sunny, cloudy, rainy, foggy, snowy}
- 影响visibility（能见度）
- 影响traction（抓地力）

## 创新点

- "天气"作为显式输入的VLM
- DriveVLM-Dual：和传统pipeline结合（解决VLM慢的问题）
- 真实车部署验证

## 复现可行性

| 维度 | 评估 |
|------|------|
| 代码 | 官方有CARLA demo |
| 数据集 | nuScenes公开 |
| 硬件 | VLM推理（中等）|
| 时间 | 5-6个月 |

## 我的思考

- 顶会，真实车部署
- 显式天气描述是个好的设计模式
- VLM推理慢是挑战
