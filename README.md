# Multi-Sensor 3DGS Reconstruction — NPU Chang'an Campus

Real-time photorealistic 3D reconstruction of a university campus using 
fused LiDAR, panoramic camera, and UAV aerial photography, rendered 
via 3D Gaussian Splatting with an interactive browser-based WebGL viewer.

---

## Demo

<img width="959" height="436" alt="after" src="https://github.com/user-attachments/assets/0e2c9e6b-fdb3-44e1-beda-6eff9220969d" />
<img width="1843" height="842" alt="cs" src="https://github.com/user-attachments/assets/ade2a915-3858-48ad-8c1c-9d7309b7cd5f" />
<img width="959" height="437" alt="uav8" src="https://github.com/user-attachments/assets/25e366ad-0f10-45fa-9530-3a83c5b59ddd" />
<img width="959" height="437" alt="uav4" src="https://github.com/user-attachments/assets/b693a660-fc95-4ab6-9892-36d532f99a08" />
<img width="959" height="441" alt="uav9" src="https://github.com/user-attachments/assets/cc21783a-0b77-49ca-99ea-3aab8788fb5c" />


---

## What This Does

Reconstructs large-scale outdoor and indoor scenes by fusing five sensor 
modalities into a single 3DGS pipeline:

- Livox Mid-360 LiDAR → geometric depth and SLAM pose estimation
- Hikvision industrial camera → synchronized RGB capture
- Insta360 ONE X2 panoramic camera → 360° ground-level texture
- DJI Matrice 300 RTK UAV → aerial photogrammetry at campus scale
- iPhone 13 Pro Max → indoor baseline capture

Output: interactive 3D models navigable in any browser via WebGL,
no software installation required.

---

## Results

| Site | Method | Splats | Status |
|------|--------|--------|--------|
| CS building exterior | UAV drone | 2,876,225 | ✅ Complete |
| Full campus aerial | UAV (4-block survey) | 7,874,493 | ✅ Complete 
---

## Pipeline
Sensors
└── Calibration (AprilTag board → OpenCV + FastLIVO2)
└── Pose Estimation
├── Outdoor: COLMAP SfM (SIFT + bundle adjustment)
└── Indoor:  FastLIVO2 LiDAR-visual-inertial SLAM
└── 3DGS Training (30,000 iterations, RTX 3080)
└── SuperSplat refinement
└── WebGL HTML export (PlayCanvas)

---

## Key Finding

LiDAR depth initialization (FastLIVO2) is essential for indoor 3DGS quality.
Camera-only methods (COLMAP + phone) produce severe floating artifacts in 
low-texture environments. Drone video COLMAP failed entirely after 72h.
Mean reprojection error: 0.24px across all sites.

---

## Stack

- **SLAM**: FastLIVO2 on Ubuntu 20.04 + ROS Noetic
- **Photogrammetry**: COLMAP
- **Neural rendering**: 3D Gaussian Splatting (Kerbl et al. 2023)
- **Post-processing**: SuperSplat v2.24
- **Training**: PyTorch 2.2.0 / CUDA 12.4 / dual RTX 3080
- **Viewer**: PlayCanvas WebGL 2.0

---

## Scripts

`scripts/extract_frames.py` — extract frames from video at configurable interval
`scripts/colmap_pipeline.sh` — full COLMAP feature extraction + matching + mapping
`scripts/rosbag_record.sh` — synchronized LiDAR + camera + IMU recording

---

## Calibration Parameters

Camera intrinsics and LiDAR-camera extrinsics in `calibration/camera_params.yaml`

Mean reprojection error: **0.24 px**
