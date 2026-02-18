"""
Formula 1 Penalty Detection - Inference Script
Run trained model on images/videos
"""

from ultralytics import YOLO
import cv2
from pathlib import Path
import argparse

def predict_image(model_path, image_path, save_dir="runs/predict"):
    """Run inference on a single image"""
    model = YOLO(model_path)
    results = model.predict(
        source=image_path,
        save=True,
        save_txt=True,
        conf=0.25,
        project=save_dir,
        name="image_inference"
    )
    
    # Print results
    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            label = r.names[cls]
            print(f"Detected: {label} (confidence: {conf:.2f})")
    
    return results

def predict_video(model_path, video_path, save_dir="runs/predict"):
    """Run inference on a video"""
    model = YOLO(model_path)
    results = model.predict(
        source=video_path,
        save=True,
        conf=0.25,
        stream=True,  # Stream for videos
        project=save_dir,
        name="video_inference"
    )
    
    for r in results:
        boxes = r.boxes
        print(f"Frame: {len(boxes)} detections")
    
    return results

def predict_webcam(model_path):
    """Run real-time inference on webcam"""
    model = YOLO(model_path)
    results = model.predict(
        source=0,  # 0 for default webcam
        show=True,
        conf=0.25,
        stream=True
    )
    
    for r in results:
        pass  # Display happens automatically
    
    return results

def main():
    parser = argparse.ArgumentParser(description='F1 Penalty Detection Inference')
    parser.add_argument('--model', type=str, required=True, help='Path to trained model weights')
    parser.add_argument('--source', type=str, required=True, help='Image/video path or 0 for webcam')
    parser.add_argument('--type', type=str, choices=['image', 'video', 'webcam'], default='image')
    parser.add_argument('--save-dir', type=str, default='runs/predict', help='Save directory')
    
    args = parser.parse_args()
    
    print(f"🏎️ F1 Penalty Detection - Running Inference")
    print(f"📦 Model: {args.model}")
    print(f"📸 Source: {args.source}")
    print(f"🔍 Type: {args.type}\n")
    
    if args.type == 'image':
        results = predict_image(args.model, args.source, args.save_dir)
        print(f"\n✅ Results saved to: {args.save_dir}/image_inference/")
    
    elif args.type == 'video':
        results = predict_video(args.model, args.source, args.save_dir)
        print(f"\n✅ Results saved to: {args.save_dir}/video_inference/")
    
    elif args.type == 'webcam':
        results = predict_webcam(args.model)
    
    print("\n🏁 Inference complete!")

if __name__ == "__main__":
    main()

# Example usage:
# python inference.py --model runs/f1_penalty/yolov8n_baseline/weights/best.pt --source "Formula 1.v1i.yolov8/test/images/00000052_jpg.rf.cfc38c938994310513e517e0fa1c2819.jpg" --type image
# python inference.py --model runs/f1_penalty/yolov8n_baseline/weights/best.pt --source video.mp4 --type video
# python inference.py --model runs/f1_penalty/yolov8n_baseline/weights/best.pt --source 0 --type webcam
