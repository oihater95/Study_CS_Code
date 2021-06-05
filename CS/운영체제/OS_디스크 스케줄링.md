# OS_디스크 스케쥴링

## 디스크 스케쥴링

- 디스크 접근 시간

  - **Seek time** + rotational delay + transfer time
    - Seek time: 탐색 시간, 실런더에 헤드를 위치 시키는 시간
    - Rotational Delay: 헤드가 트랙 내에서 원하는 블록까지 가는 시간(회전 시간)
    - Transfer time: 블록의 섹터들과 이들 사이에 있는 갭들을 통과하는데 걸리는 시간(원하는 블록 읽는 시간?)
  - 탐색 시간(seek time)이 가장 크다

  

- 다중 프로그래밍 환경

  - 디스크 큐(Disk Queue)에는 많은 요청(request)들이 쌓여있다
  - 요청들을 어떻게 처리하면 **탐색 시간을 줄일** 수 있을까?

  

- 디스크 스케쥴링 알고리즘

  - FCFS (First Come First Served)