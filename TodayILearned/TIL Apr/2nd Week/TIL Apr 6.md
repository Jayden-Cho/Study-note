# Algorithm

### 이분 탐색(이진 탐색)

**이진 탐색 알고리즘**

~~~python
def binary_search(a, v):
  start = 0 
  end = len(a) - 1
  while start <= end:
    mid = (start+end) // 2
    if v == a[mid]:
      return mid
    elif v < a[mid]:
      end = mid - 1
    else:
      start = mid + 1

  return -1

d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36))
~~~

<br>

**알고리즘 분석**

- 비교할 때 마다 찾는 값이 있을 범위를 절반씩 좁히면서 탐색하는 효율적인 탐색 알고리즘.
- 계산복잡도는 $O(\log n)$. 순차 탐색의 계산 복잡도($O(n)$)보다 낮다.
- 미리 정렬해야 한다는 단점이 있지만, 여러 번 탐색해야 한다면 자료를 한 번 정렬한 후에 이분 탐색을 이용하는게 효율적이다.