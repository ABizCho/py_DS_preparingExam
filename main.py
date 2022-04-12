import ds1_1_arrayList.py as AL

s = AL.ArrayList()
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