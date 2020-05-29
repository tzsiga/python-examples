from utils import create_subtitle

# classes
subtitle = create_subtitle('classes')

# ----------
print(next(subtitle))

class SampleClass:
  def __init__(self, arr):
    self.arr = arr

  def arrLength(self):
    return len(self.arr)

print(SampleClass([1, 2, 3]).arrLength())
