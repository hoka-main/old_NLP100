import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fp = FontProperties(fname=r'C:\WINDOWS\Fonts\meiryob.ttc', size=16)

# データ準備
x = np.linspace(0, 10, 5)  # 横軸の描画範囲指定
y1 = 2 * x + 3  # 式1 y = 2x + 3より、縦軸の値算出
y2 = 3 * x + 1  # 式2 y = 3x + 1より、縦軸の値算出

# グラフの装飾
# plt.title('日本語表示テスト', fontproperties=fp)  # タイトル
# plt.xlabel("x軸", fontproperties=fp)  # x軸ラベル
# plt.ylabel("y軸", fontproperties=fp)  # y軸ラベル

# グラフの描画
plt.plot(x, y1, label="式 y = 2x + 3")  # 式1の描画
plt.plot(x, y2, label="式 y = 3x + 1")  # 式2の描画
# plt.legend(loc="upper left", prop=fp)  # 凡例表示
plt.show()
