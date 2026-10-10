# SEAL (arxiv 2025)

**全名**: SEAL: Vision-Language Model-Based Safe End-to-End Cooperative Autonomous Driving with Adaptive Long-Tail Modeling

**链接**: https://arxiv.org/abs/2506.21041

## 核心一句话

> 用VLM做"协同自动驾驶"（车+路边单元），专门针对雪雾等长尾场景。

## 问题

单车智能在恶劣天气下感知退化 → 协同感知（V2X）能缓解，但现有方法没考虑长尾天气。

## 方案

1. **Prompt驱动的长尾数据生成**：用基础模型合成雪/雾数据
2. **门控多场景自适应注意力（GMSAA）**：用场景先验调制视觉流
3. **多任务场景感知对比学习**：提升跨场景特征可分性

## 创新点

- 第一个把 VLM + 协同感知 + 长尾天气 一起做
- 用foundation model生成训练数据（成本低）

## 复现可行性

| 维度 | 评估 |
|------|------|
| 代码 | 待查 |
| 硬件 | 中等（VLM base）|
| 时间 | 4-5个月 |

## 我的思考

- 课题契合度极高
- "长尾场景生成" 可延展到VLA的sim-to-real
- 工程复杂，需谨慎评估
