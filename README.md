# 4. 퀵 정렬 
## 4-1. 분할 정복
> 분할 정복이란? 주어진 문제를 작은 사례로 나누고(Divide) 각각의 작은 문제들을 해결하여 정복 (Conquer)하며, 작은 사례에 대한 해답을 통합(Combine)하여 원래 사례의 해답을 구한다. 이런 분할 정복은 퀵 정렬에서 사용된다.

- 분할(Divide): 문제 사례를 2개 이상으로 분리 한다.(재귀 단계)
- 정복(Conquer): 문제가 더 분할이 가능하면(재귀 단계), 또 다시 분할. 그렇지 않으면 문제 푼다.
- 통합(Combine): Conquer한 문제를 통합하여 원래의 문제의 답을 얻는다.
* [분할 정복 문제. sum 함수 작성](https://github.com/JUNGEEYOU/QuickSort/blob/master/2_sum_function.py)
* [분할 정복 문제. 가장 큰 수 찾기](https://github.com/JUNGEEYOU/QuickSort/blob/master/1_basic_quick_sort.py)
---

## 4-2. 퀵 정렬

- 퀵 정렬 순서
1. 분할(Divide): 피벗(기준 원소) 기준으로 왼쪽(피벗보다 작은 값) + 피벗 + 오른쪽(피벗보다 큰 값)으로 분리한다. 
2. 정복(Conquer): 문제가 분할 가능하면 재귀함수 호출, 그렇지 않으면 정렬한다. 
3. 통합(Combine): 정복한 문제를 통합한다. 
* [퀵 정렬 문제](https://github.com/JUNGEEYOU/QuickSort/blob/master/1_basic_quick_sort.py)

---

## 4-3. 빅오 표기법 복습

> 퀵 정렬은 최선의 경우와 평균의 경우 O(n*logn)이며 최악의 경우 O(n^2) 이다.

- 최선, 평균의 경우: O(n): 원소 비교 * O(logn) : 중간 값을 피벗으로 선택할 경우 logn 의 깊이가 나온다.
- 최악의 경우: 가장 작은 혹은 가장 큰 값을 피벗으로 선택할 경우 O(n): 원소 비교 * O(n): 깊이
