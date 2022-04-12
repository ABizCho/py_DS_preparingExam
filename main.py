'''
1. List based on array

  * List의 특징 :
    - 순서가 있고 중복을 허용하는 items의 collection
    - items는 나열된 순서에 따라 위치(index)를 갖는다.
    - index를 이용해 전후단 뿐 아니라 임의의 위치에서 삽입/삭제 가 가능하다.
    - 가장 자유로운 선형 자료구조
    - 삽입 : insert / 삭제 : delete


  * ArrayList 주요 연산 
    - insert( pos, elem )  :  pos에 elem 삽입 
    - delete( pos )  :  pos 위치의 elem 삭제
    - isEmpty( )  :  공백 판별
    - getEntry( pos )  :  pos위치의 elem 반환 


  * ArrayList와 LinkedList의 비교
      ArrayList
        - 탐색 O(1)
        - 삽입/삭제 O(n)
        - 구현이 쉬웁
        - 메모리 제한 / 애초에 크기를 정하여 넉넉히 할당 => 크기증가가 필요할 때, 더 큰 배열에 복사-이동 및 기존배열 삭제

      Linked-List 
        - 탐색 O(n)
        - 삽입/삭제 O(1)
        - 구현이 어려움
        - 메모리 제한 X / 필요시마다 메모리 증가


  * ArrayList의 응용 종류
    - 라인편집기
    - 다항식 클래스 : Polynomial


  * 파이썬 리스트 

    - 파이썬 리스트 : 동적 Array로 구현됨
    
    - 동적 배열 구조의 메모리 증가 과정 :
        1. 용량을 확장한 새로운 배열 할당
        2. 기존 배열을 새로만든 배열에 복사
        3. 메모리가 부족해 삽입하지 못했던 elem 새 배열에 삽입
        4. 기존 배열 해제 및 새 배열 사용

    - 파이썬 내장 Array 의 연산 시간복잡도
        
        - append( elem ) : 대부분 O(1)  
            -왜 대부분? : append는 최후단에 item을 삽입하는 연산이다, 이를 응용하여 최전단에 elem 삽입 시, 모든 items를 한칸씩 뒤로 옮겨야 하기 때문에 n개의 item에 대해 이동을 수행하게 됨(O(n))
        
        - insert( pos, elem ) : O(n)
        - pop( pos ) : O(n)
''' 


class ArrayList : 
  def __init__( self ) :
    self.items = []

  def insert(self, pos, elem) :
      self.items.append(None)
      for i in range(len(self.items)-2, pos-1, -1) :
          self.items[i+1] = self.items[i]
      self.items[pos] = elem

  def delete(self, pos) :
    # self.items.pop(pos)
    for i in range(pos,len(self.items)-1):
      self.items[i] = self.items[i+1]
    self.items.pop(-1)

  def getEntry(self,pos) :
    return self.items[pos]

  def isEmpty(self):
    return self.size() == 0

  def size(self) :
    return len(self.items)

  def clear(self) :
    self.items = []

  def find(self,item) :
    #self.items.index(elem)
    for i in range(self.size()):
      if self.items[i] == item :
        return i 
        
  def replace(self, pos, elem) :
    self.items[pos] = elem

  def sort(self) :
    self.items.sort()

  def merge(self, lst) :
    #self.items.extend(lst)
    self.items += lst

  def display(self, msg='ArrayList:'):
    print(msg, '항목수:',self.size(),self.items)



s = ArrayList()
s.display('파이썬 리스트로 구현한 리스트 테스트')
s.insert(0, 10)
s.insert(0, 20)
s.insert(1, 30)
s.insert(s.size(), 40)
s.insert(2, 50)
s.display("파이썬 리스트로 구현한 List(삽입x5): ")
s.sort()
s.display("파이썬 리스트로 구현한 List(정렬후): ")
s.replace(2, 90)
s.display("파이썬 리스트로 구현한 List(교체x1): ")

print("find 90 pos: ", s.find(90))
print("find 15 pos: ", s.find(15))

s.delete(2);	s.delete(s.size() - 1);	s.delete(0)
s.display("파이썬 리스트로 구현한 List(삭제x3): ")
lst = [ 1, 2, 3 ]
s.merge(lst)
s.display("파이썬 리스트로 구현한 List(병합+3): ")
s.clear()
s.display("파이썬 리스트로 구현한 List(정리후): ")

