import yt_dlp
import os

DOWNLOAD_FOLDER = "videos"

url = "https://www.youtube.com/watch?v=sisCYlyTDfca"

# Ensure the download folder exists
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

ydl_opts = {
    'format': 'best',
    'restrictfilenames': True,
    'noplaylist': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    # 비디오 정보 추출
    info_dict = ydl.extract_info(url, download=False)

    # 비디오 제목 설정
    video_title = (info_dict.get('title', 'video')
                   .replace(' ', '_')
                   .replace('/', '_'))

    # 파일 확장명 설정
    video_ext = 'mp4'
    output_filename = f"{video_title}.{video_ext}"

    # 다운로드 경로 설정
    ydl_opts['outtmpl'] = os.path.join(DOWNLOAD_FOLDER, output_filename)

    ydl = yt_dlp.YoutubeDL(ydl_opts)
    ydl.download([url])

file_path = os.path.join(DOWNLOAD_FOLDER, output_filename)
print(f"Video downloaded successfully to {file_path}")
