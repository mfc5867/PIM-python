class core:

  func = []
  A = 0
  B = 0
  Y = 0

  def __init__(self, N):
    self.N = N

  def setFunc(self, func, ind):
    self.func[ind] = func
    evaluate(self)

  def setA(self, A):
    self.A = A
    evaluate(self)

  def setB(self, B):
    self.B = B
    evaluate(self)

  def evaluate(self):
    for i in range(0,2*N-1):
      Y |= ((func[2*N-i] >> SEL) & 0x01 << i)
