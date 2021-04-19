# Computer_Network_01_Data Link Control

> framing, flow control, error control, protocols

- 라우터: 신호를 다른 컴퓨터로 연결하는 장치 (일종의 컴퓨터)
- End System(실제 우리가 다루는 컴퓨터) 사이에 전송되는 Data를 관리하는 기술을 Data Link Control이라 한다



## Data Link Layer의 역할

- Frame Synchronization Frame: Data는 여러 조각(blocks)으로 분리해서 보낸다. 보내는 쪽과 받는 쪽의 데이터 조각이 동기화 되어야함
- Flow Control: 수신자가 송신자의 데이터를 통제하는 것(데이터 양 관리)
- **Error Control**:에러 검출 및 복구
- Physical addressing: 통신 할 대상을 특정하는 물리적 주소 (식별자)
- Access Control: 여러 장치가 같은 링크에 연결되어 있을 대, 어떤 장치가 연결될 지 결정하는 것



## Poll / Select

- multidrop (multipoint)
  - 여러 터미널이 선 하나를 공유 => transmission line cost를 줄일 수 있다.
  - **한 번에 message block 하나**만 보낼 수 있다. => 현재는 거의 사용 안함 (Primary Computer와 Secondary Computer 나뉘던 컴퓨터에서 사용)
- Polling: secondary가 send할 때 사용
  - Roll-call Polling: Primary가 하나씩 다 물어보는 것
  - Hub Polling: Poll command를 secondary에게 주고 secondary가 서로 command를 돌리며 poll을 결정
- Select: primary가 send할 때 사용



## Framing

- Data Link Layer는 bits를 frame에 넣어 보낸다 => 각각 구분될 수 있는 frame에 넣어 데이터 구분
- 만약 message가 매우 큰 frame 하나에 담겨져 보내졌을 때 하나의 error가 전체 데이터에 큰 영향을 끼치기 때문에 여러 frame으로 나누어 전송

