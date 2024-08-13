# import os

# # 対象ディレクトリ
# labels_dir = r'C:/Users/iniad/Downloads/me2-20240728T092948Z-001/me2_output/data/labels'

# # ディレクトリ内のすべてのテキストファイルを処理
# for filename in os.listdir(labels_dir):
#     if filename.endswith('.txt'):
#         file_path = os.path.join(labels_dir, filename)
        
#         # ファイルの内容を読み込む
#         with open(file_path, 'r') as file:
#             lines = file.readlines()
        
#         # 先頭のクラス番号を0から1に書き換えた新しい内容を生成
#         new_lines = [line.replace('0', '2', 1) if line.startswith('0') else line for line in lines]
        
#         # ファイルに書き戻す
#         with open(file_path, 'w') as file:
#             file.writelines(new_lines)

# print("All label files have been updated.")

import cv2
import os

# 動画ファイルのパス
video_path = 'C:/Users/iniad/Pictures/Camera Roll/WIN_20240813_18_24_49_Pro.mp4'

# 画像を保存するディレクトリ
output_dir = 'C:/Users/iniad/Pictures/Camera Roll'
os.makedirs(output_dir, exist_ok=True)

# 動画を読み込む
cap = cv2.VideoCapture(video_path)

# フレームカウント用の変数
frame_count = 0

# 動画が開けない場合のエラーメッセージ
if not cap.isOpened():
    print("Error: 動画を開けません")
    exit()

# 動画のフレームを1つずつ読み込むループ
while True:
    ret, frame = cap.read()

    # フレームが取得できなかった場合、終了する
    if not ret:
        break

    # フレームを画像として保存
    frame_filename = f"{output_dir}/frame_{frame_count:04d}.jpg"
    cv2.imwrite(frame_filename, frame)

    # フレームカウントをインクリメント
    frame_count += 1

# 動画ファイルを閉じる
cap.release()

print(f"保存されたフレームの数: {frame_count}")
print("フレーム画像が正常に保存されました")
