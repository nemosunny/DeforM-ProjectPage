import os
import subprocess

video_dir = "/Users/sunnyli/desktop/ECCV/Project_Page/project_page/static/teaser"

def convert(video_path):
    tmp_path = video_path.replace(".mp4", "_tmp.mp4")

    cmd = [
        "ffmpeg",
        "-y",
        "-i", video_path,

        # ===== Safari 兼容核心 =====
        "-vcodec", "libx264",
        "-profile:v", "baseline",
        "-level", "3.0",
        "-pix_fmt", "yuv420p",

        # ===== 优化（可选）=====
        "-movflags", "+faststart",

        # 无音频（论文 project page 推荐）
        "-an",

        tmp_path
    ]

    subprocess.run(cmd, check=True)

    # 覆盖原文件（关键）
    os.replace(tmp_path, video_path)

    print(f"[OK] Safari-safe: {os.path.basename(video_path)}")


def main():
    for root, _, files in os.walk(video_dir):
        for f in files:
            if f.endswith(".mp4"):
                path = os.path.join(root, f)
                convert(path)


if __name__ == "__main__":
    main()