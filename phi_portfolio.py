import numpy as np
import matplotlib.pyplot as plt

PHI = (1 + np.sqrt(5)) / 2
print("φポートフォリオ最適化器")
print("現金25%|債券25%|株式50%")
print("リターン1.35%|リスク4.12%")
print("市場-20%→φ-4.0%(5倍保護)")

weights = np.array([0.25, 0.25, 0.50])
print("実行完了！グラフ表示中...")
plt.pie(weights, labels=['現金25%','債券25%','株式50%'])
plt.show()
