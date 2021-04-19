# Computer_Network_03_HDLC(2)

## 11.3 protocols

- 시퀀스 넘버라는 프레임의 순서 번호를 사용
  - 시퀀스 넘버는 Header에 들어감
- ACK(acknowledgement): 잘 받았다는 메세지
  - ACK1: 온전한 데이터를 받았을 때 번호도 같이 보낸다
  - ACK 숫자의미: 다음 받을 프레임 번호 ex) ACK1 = 1번 프레임 받아야함
  - Frame 0을 받으면 ACK1을 보내 Frame 1을 요청한다
  - ACK는 다음 받을 프레임 번호를 응답해주기 때문에 이전 프레임에 대해 헌꺼번에 ACK해준다
- NAK(negative acknowledgement): 온전한 데이터를 받지 못함
- Piggybacking: 송신 데이터와 수신 데이터에 대한 응답을 한 프레임에 조합하는 것
  - 별도의 ACK를 보내지 않고 데이터 프레임에 확인 응답을 포함 시켜 전송



### Stop-And-Wait ARQ(Automatic Repeat Request)

![image-20210420013021534](Computer_Network_03_HDLC(2).assets/image-20210420013021534.png)

- 프레임을 보내고 ACK가 순서대로 오는 것을 기대
- 데이터를 전송할 때 타이머를 동작 => 프레임 보냈는데 ACK나 NAK가 안 올 경우 무한정 기다리는 것을 방지
- 타이머 타임아웃이 되면 다시 보낸다 
- 타이머는 각 프레임 마다 존재
- 넘버링을 하지 않으면(ACK Number) 중복해서 보냈다는 것을 확인할 수 없다.
- Frame 소실된 경우 예시
  - Frame 1 소실(Lost) => ACK 0(다음 Frame 번호) 를 보낼 수 없음
  - Sender는 타임아웃이 될 때까지 ACK 0 기다림
  - 타임아웃 되면 Frame 1을 재전송
- 해당 프로토콜은 현재 사용하지 않음



### Go-Back-N ARQ

![image-20210420011932823](Computer_Network_03_HDLC(2).assets/image-20210420011932823.png)

- 여러 프레임들을 연속적으로 보내고, 수신측에서 NAK를 보내면 그 부분 부터 최근 보낸 프레임들을 재전송
- window size: outstanding 프레임수 (보낸 frame에 대한 ACK나 NAK 안 온 프레임)
- Stop-And-Wait 방식과의 차이점
  - Stop-And-Wait은 프레임 하나 보낼 때마다 ACK가 와야함 => 오래 걸림
  - Go-Back-N은 window size만큼 보낼 수 있다
- 최대 윈도우 사이즈는 bit 개수가 m 일때 2^(m-1)개
- 프레임이 에러  나거나 순서 상관없는 것이 왔다면 가만히 있거나 NAK를 보냄
- ACK가 오지 않으면 다시 보내야할 수 있으니 계속 갖고 있다가 ACK가 오면 더 이상 hold할 필요 없어서 해제한다. => ACK2가 오지 않아서 Frame 1, 2, 3 hold
- 에러가 나면 **에러가 발생한 프레임부터 최근에 내가 보낸 프레임들을 모두 다시 보낸다.** 에러가 발생한 프레임만 보내는 것 아님



### Selective-Reject ARQ

![image-20210420030146574](Computer_Network_03_HDLC(2).assets/image-20210420030146574.png)



- 에러난 프레임만 다시 보냄
- Go-Back-N ARQ에서는 NAK1을 보낸 후 2번 프레임이 들어오면 에러 체크 안하고 버림.
- Selective-Reject ARQ는 에러 체크하고 갖고 있음 => Receiver window



![image-20210420030244555](Computer_Network_03_HDLC(2).assets/image-20210420030244555.png)

- 윈도우 사이즈가 2^(m-1)보다 크면 문제가 발생하는 이유
  - 위 예시에서 2^(m-1)일 경우
    - 수신자는 0과 1 받았지만 ACK1, ACK2가 소실됨
    - 송신자는 ACK1, 2가 오지 않아 Frame 0을 보냄
    - 수신자는 해당 Frame 0은 이미 받았으므로(수신자의 윈도우에 0 없음) 중복처리해서 버림
  - 위 예시에서 2^(m-1)보다 큰 경우
    - 수신자는 Frame 0, 1, 2. 모두 받았지만 ACK 1, 2, 3이 소실됨
    - 송신자는 ACK 1, 2, 3이 없어서 Frame 0부터 재전송함
    - 그 때 수신자의 윈도우는 0을 가지고 있어서 송신자가 보낸 Frame 0가 이전의 Frame 0이 아닌 새로운 Frame 0으로 인식
- Sender의 window size + Receiver의 window size <= 시퀀스 번호 공간 크기