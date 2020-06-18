import pathlib
import shutil
files = list(pathlib.Path('.').rglob('*.txt'))  # 対象の拡張子をここで指定する
prev_len = 0
for i, src in enumerate(files):
    dest = src.with_suffix('.py')  # 変更拡張子を指定する
    print(f'\r{" "*prev_len}', end='')  # 前回の残像をスペースで消す
    progress = f'{i+1}/{len(files)}:{src.name} -> {dest.name}'
    print(f'\r{progress}',end='')
    shutil.move(src, dest)
    prev_len = len(progress)
print()


