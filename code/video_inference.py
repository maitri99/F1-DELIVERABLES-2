"""
🎬 F1 Penalty Detection - Real-time Video Processing
Dell Pro Max GB10 + NVIDIA Hackathon 2026

Process F1 race videos in real-time and detect penalties frame-by-frame.
Optimized for Dell GB10 GPU for maximum FPS.
"""

import cv2
import numpy as np
from ultralytics import YOLO
from pathlib import Path
import time
from collections import deque
import argparse

class F1VideoProcessor:
    """Real-time F1 penalty detection on video streams"""
    
    def __init__(self, model_path, confidence=0.25, device='cuda'):
        """
        Initialize video processor
        
        Args:
            model_path: Path to trained YOLOv8 model
            confidence: Confidence threshold for detections
            device: 'cuda' or 'cpu'
        """
        print(f"🔧 Loading model from: {model_path}")
        self.model = YOLO(model_path)
        self.confidence = confidence
        self.device = device
        
        # Performance tracking
        self.fps_queue = deque(maxlen=30)  # Track last 30 frames
        self.frame_count = 0
        self.penalty_count = 0
        self.non_penalty_count = 0
        
        print(f"✅ Model loaded on device: {device}")
        print(f"🎯 Confidence threshold: {confidence}")
    
    def process_frame(self, frame):
        """
        Process a single frame
        
        Args:
            frame: Input frame (numpy array)
            
        Returns:
            annotated_frame: Frame with detections drawn
            detections: List of detection dictionaries
            fps: Current FPS
        """
        start_time = time.time()
        
        # Run inference
        results = self.model.predict(
            source=frame,
            conf=self.confidence,
            verbose=False,
            device=self.device
        )
        
        # Get annotated frame
        annotated_frame = results[0].plot()
        
        # Calculate FPS
        inference_time = time.time() - start_time
        fps = 1.0 / inference_time
        self.fps_queue.append(fps)
        
        # Extract detections
        detections = []
        for box in results[0].boxes:
            cls = int(box.cls)
            conf = float(box.conf)
            
            detection = {
                'class': 'Penalty' if cls == 1 else 'Non-Penalty',
                'confidence': conf,
                'bbox': box.xyxy[0].tolist()
            }
            detections.append(detection)
            
            # Update counters
            if cls == 1:
                self.penalty_count += 1
            else:
                self.non_penalty_count += 1
        
        self.frame_count += 1
        
        return annotated_frame, detections, fps
    
    def add_overlay(self, frame, fps, detections):
        """
        Add performance overlay to frame
        
        Args:
            frame: Input frame
            fps: Current FPS
            detections: List of detections
            
        Returns:
            frame: Frame with overlay
        """
        # Calculate average FPS
        avg_fps = np.mean(self.fps_queue) if self.fps_queue else 0
        
        # Add semi-transparent overlay box
        overlay = frame.copy()
        cv2.rectangle(overlay, (10, 10), (400, 180), (0, 0, 0), -1)
        frame = cv2.addWeighted(frame, 0.7, overlay, 0.3, 0)
        
        # Add text information
        font = cv2.FONT_HERSHEY_SIMPLEX
        y_offset = 40
        
        # Title
        cv2.putText(frame, "F1 PENALTY DETECTION - GB10", 
                    (20, y_offset), font, 0.6, (0, 255, 255), 2)
        y_offset += 30
        
        # FPS
        color = (0, 255, 0) if avg_fps >= 30 else (0, 165, 255)
        cv2.putText(frame, f"FPS: {avg_fps:.1f}", 
                    (20, y_offset), font, 0.6, color, 2)
        y_offset += 25
        
        # Frame count
        cv2.putText(frame, f"Frame: {self.frame_count}", 
                    (20, y_offset), font, 0.5, (255, 255, 255), 1)
        y_offset += 25
        
        # Detection counts
        cv2.putText(frame, f"Penalties: {self.penalty_count}", 
                    (20, y_offset), font, 0.5, (0, 0, 255), 1)
        y_offset += 20
        cv2.putText(frame, f"Non-Penalties: {self.non_penalty_count}", 
                    (20, y_offset), font, 0.5, (0, 255, 0), 1)
        y_offset += 25
        
        # Current frame detections
        cv2.putText(frame, f"Current: {len(detections)} detections", 
                    (20, y_offset), font, 0.5, (255, 255, 255), 1)
        
        return frame
    
    def process_video(self, video_path, output_path=None, display=True):
        """
        Process entire video file
        
        Args:
            video_path: Path to input video
            output_path: Path to save output video (optional)
            display: Whether to display video while processing
        """
        print(f"\n{'='*70}")
        print(f"🎬 PROCESSING VIDEO: {video_path}")
        print(f"{'='*70}\n")
        
        # Open video
        cap = cv2.VideoCapture(str(video_path))
        
        if not cap.isOpened():
            print(f"❌ Error: Could not open video {video_path}")
            return
        
        # Get video properties
        fps_input = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        print(f"📹 Video Properties:")
        print(f"  Resolution: {width}x{height}")
        print(f"  Input FPS: {fps_input}")
        print(f"  Total Frames: {total_frames}")
        print(f"  Duration: {total_frames/fps_input:.2f}s\n")
        
        # Setup video writer if output path specified
        writer = None
        if output_path:
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            writer = cv2.VideoWriter(str(output_path), fourcc, fps_input, (width, height))
            print(f"💾 Output will be saved to: {output_path}\n")
        
        print("🚀 Processing started... Press 'q' to quit\n")
        
        # Process frames
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            # Process frame
            annotated_frame, detections, fps = self.process_frame(frame)
            
            # Add overlay
            annotated_frame = self.add_overlay(annotated_frame, fps, detections)
            
            # Write to output file
            if writer:
                writer.write(annotated_frame)
            
            # Display frame
            if display:
                cv2.imshow('F1 Penalty Detection - Dell GB10', annotated_frame)
                
                # Check for quit
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("\n⚠️  Processing interrupted by user")
                    break
            
            # Print progress every 30 frames
            if self.frame_count % 30 == 0:
                progress = (self.frame_count / total_frames) * 100
                print(f"Progress: {progress:.1f}% | Frame: {self.frame_count}/{total_frames} | "
                      f"FPS: {np.mean(self.fps_queue):.1f}", end='\r')
        
        # Cleanup
        cap.release()
        if writer:
            writer.release()
        if display:
            cv2.destroyAllWindows()
        
        # Print summary
        print(f"\n\n{'='*70}")
        print("✅ PROCESSING COMPLETE!")
        print(f"{'='*70}")
        print(f"\n📊 Summary:")
        print(f"  Frames Processed: {self.frame_count}")
        print(f"  Average FPS: {np.mean(self.fps_queue):.1f}")
        print(f"  Total Penalties: {self.penalty_count}")
        print(f"  Total Non-Penalties: {self.non_penalty_count}")
        if output_path:
            print(f"  Output Saved: {output_path}")
        print()

def main():
    parser = argparse.ArgumentParser(
        description="F1 Penalty Detection - Real-time Video Processing"
    )
    parser.add_argument(
        '--video', '-v',
        type=str,
        required=True,
        help='Path to input video file'
    )
    parser.add_argument(
        '--model', '-m',
        type=str,
        default='runs/f1_penalty_gb10/yolov8n_optimized/weights/best.pt',
        help='Path to trained model (default: best.pt from training)'
    )
    parser.add_argument(
        '--output', '-o',
        type=str,
        default=None,
        help='Path to save output video (optional)'
    )
    parser.add_argument(
        '--confidence', '-c',
        type=float,
        default=0.25,
        help='Confidence threshold (0-1, default: 0.25)'
    )
    parser.add_argument(
        '--device', '-d',
        type=str,
        default='cuda',
        choices=['cuda', 'cpu', 'mps'],
        help='Device to run inference on'
    )
    parser.add_argument(
        '--no-display',
        action='store_true',
        help='Do not display video while processing'
    )
    
    args = parser.parse_args()
    
    # Initialize processor
    processor = F1VideoProcessor(
        model_path=args.model,
        confidence=args.confidence,
        device=args.device
    )
    
    # Process video
    processor.process_video(
        video_path=args.video,
        output_path=args.output,
        display=not args.no_display
    )

if __name__ == "__main__":
    # Example usage:
    # python video_inference.py --video race_footage.mp4 --output results.mp4
    # python video_inference.py -v test.mp4 -o output.mp4 -c 0.3 -d cuda
    
    main()
