"""
Formula 1 Penalty Detection - YOLOv8 Training Script
Nvidia-Dell Hackathon
"""

from ultralytics import YOLO
import torch
from pathlib import Path

def main():
    # Check GPU availability
    device = 'cuda' if torch.cuda.is_available() else 'mps' if torch.backends.mps.is_available() else 'cpu'
    print(f"🔥 Using device: {device}")
    
    # Paths - use absolute path to avoid issues
    # Use augmented dataset if available, otherwise use original
    augmented_yaml = Path("Formula 1.v1i.yolov8/data_augmented.yaml")
    original_yaml = Path("Formula 1.v1i.yolov8/data.yaml")
    
    if augmented_yaml.exists():
        data_yaml = augmented_yaml.resolve()
        print("🎨 Using AUGMENTED dataset (4x images)")
    else:
        data_yaml = original_yaml.resolve()
        print("📦 Using ORIGINAL dataset")
    
    # Initialize YOLOv8 model (you can use yolov8n, yolov8s, yolov8m, yolov8l, yolov8x)
    # n=nano (fastest), s=small, m=medium, l=large, x=xlarge (most accurate)
    model = YOLO('yolov8n.pt')  # Start with nano for quick testing
    
    print("📦 Dataset: 309 train, 29 valid, 15 test images")
    print("🎯 Classes: Penalty, Non-penalty")
    print("⏰ Starting training...\n")
    
    # Train the model
    results = model.train(
        data=str(data_yaml),
        epochs=50,              # Full training on augmented dataset
        imgsz=640,              # Image size
        batch=16,               # Batch size (adjust based on GB10's massive memory)
        patience=10,            # Early stopping patience
        save=True,              # Save checkpoints
        device=device,          # Use available device
        project='runs/f1_penalty',  # Project name
        name='yolov8n_baseline',    # Experiment name
        exist_ok=True,
        
        # Data augmentation (important for small datasets)
        hsv_h=0.015,            # HSV-Hue augmentation
        hsv_s=0.7,              # HSV-Saturation augmentation
        hsv_v=0.4,              # HSV-Value augmentation
        degrees=10,             # Rotation
        translate=0.1,          # Translation
        scale=0.5,              # Scale
        shear=0.0,              # Shear
        perspective=0.0,        # Perspective
        flipud=0.0,             # Flip up-down
        fliplr=0.5,             # Flip left-right
        mosaic=1.0,             # Mosaic augmentation
        mixup=0.1,              # MixUp augmentation
        
        # Optimization
        optimizer='AdamW',      # Optimizer
        lr0=0.01,               # Initial learning rate
        lrf=0.01,               # Final learning rate
        momentum=0.937,         # Momentum
        weight_decay=0.0005,    # Weight decay
        warmup_epochs=3,        # Warmup epochs
        
        # Other
        verbose=True,           # Verbose output
        seed=42,                # Random seed for reproducibility
    )
    
    # Evaluate on test set
    print("\n📊 Evaluating on test set...")
    metrics = model.val(data=str(data_yaml), split='test')
    
    print("\n✅ Training Complete!")
    print(f"📈 Results saved to: runs/f1_penalty/yolov8n_baseline/")
    print(f"🎯 mAP@0.5: {metrics.box.map50:.4f}")
    print(f"🎯 mAP@0.5:0.95: {metrics.box.map:.4f}")
    
    # Export model (optional)
    print("\n💾 Exporting model to ONNX format...")
    model.export(format='onnx')
    
    return model, results, metrics

if __name__ == "__main__":
    main()
