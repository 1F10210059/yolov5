#アノーテーションファイルのラベル変更
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


# #動画から写真へ
# import cv2
# import os

# # 動画ファイルのパス
# video_path = 'C:/Users/iniad/Pictures/Camera Roll/WIN_20240904_22_09_56_Pro.mp4'
# # 画像を保存するディレクトリ
# output_dir = 'C:/Users/iniad/Pictures/Camera Roll'
# os.makedirs(output_dir, exist_ok=True)

# # 動画を読み込む
# cap = cv2.VideoCapture(video_path)

# # フレームカウント用の変数
# frame_count = 0

# # 動画が開けない場合のエラーメッセージ
# if not cap.isOpened():
#     print("Error: 動画を開けません")
#     exit()

# # 動画のフレームを1つずつ読み込むループ
# while True:
#     ret, frame = cap.read()

#     # フレームが取得できなかった場合、終了する
#     if not ret:
#         break

#     # フレームを画像として保存
#     frame_filename = f"{output_dir}/frame_{frame_count:04d}.jpg"
#     cv2.imwrite(frame_filename, frame)

#     # フレームカウントをインクリメント
#     frame_count += 1

# # 動画ファイルを閉じる
# cap.release()

# print(f"保存されたフレームの数: {frame_count}")
# print("フレーム画像が正常に保存されました")


#画像ファイルの名前変更
import os

# 画像が保存されているディレクトリのパス
images_dir = 'C:/Users/iniad/Downloads/add_box_output/data/obj'

# フォルダ内のすべてのファイルを取得
files = os.listdir(images_dir)

# 画像ファイルのみをフィルタリング
image_files = [f for f in files if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg')]

# ファイルのリネーム処理
for i, filename in enumerate(image_files, start=1):
    # 現在のファイルパス
    old_file_path = os.path.join(images_dir, filename)
    
    # 新しいファイル名とファイルパス
    new_filename = f"sakanaka_{i}.jpg"
    new_file_path = os.path.join(images_dir, new_filename)
    
    # ファイル名の変更
    os.rename(old_file_path, new_file_path)

print("すべての画像の名前が変更されました。")


# import os

# # 対象ディレクトリ
# labels_dir = r'C:/Users/iniad/yolov5/data/val/labels'

# # ディレクトリ内のすべてのテキストファイルを処理
# for filename in os.listdir(labels_dir):
#     if filename.endswith('.txt'):
#         file_path = os.path.join(labels_dir, filename)
        
#         # ファイルの内容を読み込む
#         with open(file_path, 'r') as file:
#             lines = file.readlines()
        
#         # 新しい内容を生成
#         new_lines = []
#         for line in lines:
#             if line.startswith('1'):
#                 continue  # 1から始まる行をスキップ
#             elif line.startswith('2'):
#                 new_lines.append(line.replace('2', '1', 1))  # 2から始まる行の2を1に変更
#             else:
#                 new_lines.append(line)  # それ以外の行はそのまま保持
        
#         # ファイルに書き戻す
#         with open(file_path, 'w') as file:
#             file.writelines(new_lines)

# print("All label files have been updated.")
