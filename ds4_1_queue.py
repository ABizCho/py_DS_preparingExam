'''
큐 Queue 
(= Circular Queue )

  * 큐의 특징 
    - 큐는 FIFO(선입선출)의 일방향 선형 자료구조 이다.
    - ( -> [front / rear] -> ) : 전단으로 들어와서 후단으로 나간다.

  * 큐의 종류 
    - 선형 큐 : Linear Queue
        - 삽입 : O(1)
        - 삭제 : O(n) : 맨앞 item을 삭제하면 뒤의 항목을 모두 앞으로 이동해야 하기에 비효율

        - 문제점 : front, rear의 값이 삽입/삭제와 관계없이 증가만 하기 때문에 앞부분이 비어있더라도 배열의 끝에 도달하여 추가삽입이 불가능하다.

    - 원형 큐 : Circular Queue
      - 특징 
        - 배열을 원형으로 사용하여 구현하는 큐
        - 시계방향으로 회전한다
        - 큐는 일반적으로 Circular queue를 말한다.

  * 주요 키워드
      큐는 삽입 삭제를 위해 front,rear(전/후단)의 두가지 방향을 사용한다.
      - 삽입 : rear(후단) : 첫번째 item 하나 앞의 인덱스
      - 삭제 : front(전단) : 마지막 요소의 인덱스

  * 시계방향 회전방법 
    - front:  (front+1) % MAX_QSIZE
    - rear:  (rear+1) % MAX_QSIZE

  * 원형 큐의 상태판별
    원형 큐는 상태판별을 위해 하나의 공간은 항상 남겨둔다.
    가득 찬 경우 오류상태이다.
    - 공백상태 : front == rear
    - 포화상태 : front % M == (rear+1) % M 
      -> 원형 큐를 위한 리스트의 크기가 미리 결정되어야 하기 때문에 포화상태가 존재

  * 주요 연산
    - enqueue(elem)
    - dequeue()

  * 큐의 응용
    - BFS (Breadth Fisrt Search, 너비우선탐색)
      - 미로탐색
      - (+ 이진트리의 레벨순회, 기수정렬의 레코드 정렬, 그래프탐색의 너비우선 탐색)

    - 피보나치 수열의 효과적 계산

    - (+ 서비스센터의 콜, 인쇄 순서, 버퍼링, 대기열 시뮬레이션, 통신 데이터 패킷 모델링)

'''

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
    if not self.isFull :                    #포화상태가 아니면
      self.rear = (self.rear+1) % MAX_QSIZE  # rear 회전
      self.items[self.rear] = elem            # rear 위치에 삽입

  def dequeue( self ) : # 큐 맨앞의 항목을 꺼내며 반환
    if not self.isEmpty :                    #공백상태가 아니면
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
      
  
    