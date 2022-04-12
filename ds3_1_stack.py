'''

Stack ( based on Array )

  * 스택의 특징
    - 스택은 LIFO: 후입선출의 선형 자료구조이다.
    - 상단으로 들어오고 상단으로 나간다 : 삽입/삭제가 한쪽에서 수행된다.

  * 주요 데이터
    - top: 스택 항목을 저장하는 파이썬 리스트를 지칭
    - 항목의 개수 : len(top)

  * 스택의 주요연산 
    - push(elem)
    - pop()
    - isEmpty() 
    - peek() 

  * 파이썬 Array 기반 스택 구현 시 항목의 삽입,삭제 위치는 최후단이 유리하다
    why? : 파이썬 내장 리스트인 array는 최후단삽입을 기본으로 한다 
      - 후단 이용 삽입/삭제 시 : O(1)
      - 전단 이용 삽입/삭제 시 : O(n)

  * 스택의 응용 
    - 괄호검사
    - 후위표기 계산,중위표기 계산
    - 중위-> 후위 표기식 변환
    - DFS : 깊이우선 탐색 : 미로
    - 문자열 역순출력
    - 회문 판별 

    - (+ 뒤로가기, 되돌리기 / 콜백,재귀호출 )
'''

class Stack :
  def __init__( self ) :
    self.top = []

  def push(self, elem) :
    self.top.append(elem)

  def pop(self) :
    if not self.isEmpty() == True :
      self.top.pop(-1)

  def isEmpty(self) :
    return self.size() == 0

  def size(self) :
    return len(self.top)

  def clear(self) :
    self.top = []

  def peek(self) :
    return self.top[-1]

  def __str__( self ) :
    return str(self.top[::-1])
