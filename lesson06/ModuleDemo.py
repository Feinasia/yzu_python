import math  # 導入一個模組
import math as m  #導入一個模組  並給予簡稱
from math import pi  # 直接導入模組中某功能

import lesson06.Utils as u  #導入一個 PY 檔，可用裡面的 自訂函式 def
from lesson06.Utils import sub  # 直接導入PY 中某 def

print(math.pi)
print(m.pi)
print(pi)

print(u.add(10,20))
print(sub(10, 20))