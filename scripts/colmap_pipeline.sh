# Step 1: Extract SIFT features from all images
colmap feature_extractor \
  --database_path /share/uav_mapping/database.db \
  --image_path /share/uav_mapping/images \
  --ImageReader.camera_model OPENCV

# Step 2: Match features exhaustively across all image pairs
colmap exhaustive_matcher \
  --database_path /share/uav_mapping/database.db

# Step 3: Incremental sparse reconstruction with bundle adjustment
colmap mapper \
  --database_path /share/uav_mapping/database.db \
  --image_path /share/uav_mapping/images \
  --output_path /share/uav_mapping/sparse
