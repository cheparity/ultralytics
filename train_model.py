from ultralytics import YOLO
import torch
if not torch.backends.mps.is_available():
    if not torch.backends.mps.is_built():
        print("MPS not available because the current PyTorch install was not built with MPS enabled.")
    else:
        print(
            "MPS not available because the current MacOS version is not 12.3+ "
            "and/or you do not have an MPS-enabled device on this machine."
        )

# 加载模型
model = YOLO("yolo11n.pt")

# 训练模型
train_results = model.train(
    data="/Users/liuyucheng/Projects/yolov11/ultralytics/cfg/datasets/tinyperson.yaml",  # 数据集 YAML 路径
    epochs=100,  # 训练轮次
    imgsz=640,  # 训练图像尺寸
    device='mps',  # 运行设备，例如 device=0 或 device=0,1,2,3 或 device=cpu
)

# 评估模型在验证集上的性能
metrics = model.val()

# 在图像上执行对象检测
results = model(
    "/Users/liuyucheng/Projects/yolov11/ultralytics/cfg/datasets/tinyperson/test/images/baidu_P000_4_jpg.rf.b5255d9f0b569e85fab6d0998a6dbfb0.jpg"
)
results[0].show()

# 将模型导出为 ONNX 格式
path = model.export(format="onnx")  # 返回导出模型的路径
