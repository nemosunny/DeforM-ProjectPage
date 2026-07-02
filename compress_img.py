import os
from PIL import Image

# ======================
# 配置路径
# ======================
input_dir = "/Users/sunnyli/desktop/ECCV/Project_Page/project_page/static/teaser"

# ======================
# 最大分辨率（核心参数）
# ECCV project page 推荐 1200~1600
# ======================
MAX_WIDTH = 1600
MAX_HEIGHT = 1600

# ======================
# 压缩函数
# ======================
def resize_image(img):
    w, h = img.size

    # 如果已经很小就不动
    if w <= MAX_WIDTH and h <= MAX_HEIGHT:
        return img

    # 等比缩放
    scale = min(MAX_WIDTH / w, MAX_HEIGHT / h)
    new_size = (int(w * scale), int(h * scale))

    return img.resize(new_size, Image.LANCZOS)


def process_png(path):
    try:
        img = Image.open(path)

        # 保留透明通道
        if img.mode not in ("RGBA", "RGB"):
            img = img.convert("RGBA")

        # 1. resize（关键压缩点）
        img = resize_image(img)

        # 2. 重新保存 PNG（轻量优化）
        img.save(
            path,
            format="PNG",
            optimize=True
        )

        print(f"[OK] {os.path.basename(path)} -> {img.size}")

    except Exception as e:
        print(f"[FAIL] {path} -> {e}")


def main():
    for file in os.listdir(input_dir):
        if file.lower().endswith(".png"):
            full_path = os.path.join(input_dir, file)
            process_png(full_path)


if __name__ == "__main__":
    main()