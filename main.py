
MAX_QSIZE = 10
class CircularQueue :
  def __init__( self ) :
    self.front = 0
    self.rear = 0
    self.items = [None] * MAX_QSIZE

  def isEmpty( self ) :
    return self.front == self.rear

  def isFull( self ) :
    return self.front == (self.rear + 1) % MAX_QSIZE
    
  def enqueue( self, elem ) :
    if not self.isFull() :                    #포화상태가 아니면
      self.rear = (self.rear+1) % MAX_QSIZE  # rear 회전
      self.items[self.rear] = elem            # rear 위치에 삽입

  def dequeue( self ) : # 큐 맨앞의 항목을 꺼내며 반환
    if not self.isEmpty() :                    #공백상태가 아니면
      self.front = (self.front + 1) % MAX_QSIZE # front 회전
      return self.items[self.front]              # front 위치의 항목 반환

  def peek( self ) :  # 큐 맨앞의 항목을 반환
    if not self.isEmpty() :                  #공백상태가 아니면
      return self.items[( self.front +1 ) % MAX_QSIZE ]  # 현 front위치 바로 뒤의 항목을 반환

  def size( self ) :
    return ( self.rear - self.front + MAX_QSIZE ) % MAX_QSIZE

  def display( self ) :
    out = []
    if self.front < self.rear :
      out = self.items[ self.front+1 : self.rear + 1 ]
    else :
      out = self.items[self.front+1: MAX_QSIZE] + self.items[ 0 : self.rear + 1 ]
    print("[f=%s,r=%d] ==> "%(self.front, self.rear) ,out )
      


q= CircularQueue()
for i in range(8) : q.enqueue(i)
q.display()
for i in range(5) : q.dequeue();
q.display()
for i in range(8,14) : q.enqueue(i);
q.display()
