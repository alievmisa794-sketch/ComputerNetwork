# Лабораторная работа: Анализ сетевого трафика в Wireshark

## Скриншот 1: TCP с флагом SYN (начало соединения)

**Фильтр:** `tcp.flags.syn == 1 && tcp.flags.ack == 0`

Этот пакет показывает начало TCP-соединения. Клиент отправляет серверу пакет с флагом **SYN** (synchronize), чтобы инициировать handshake (рукопожатие).

В поле Flags видно:
- `Flags: 0x002 (SYN)`
- `.... .... ..1. = Syn: Set` — флаг SYN установлен
- Все остальные флаги (ACK, PSH, RST, FIN) = Not set

<img width="954" height="1080" alt="1_image" src="https://github.com/user-attachments/assets/8a77da21-49c1-45c6-adc7-9eaa47f3b61b" />




## Скриншот 2: TCP с флагами PSH и ACK (передача данных)

**Фильтр:** `tcp.flags.push == 1 && tcp.flags.ack == 1`

Этот пакет показывает передачу данных с подтверждением получения:
- **PSH (Push)** — протолкнуть данные приложению немедленно
- **ACK (Acknowledgment)** — подтверждение получения предыдущих данных

В поле Flags видно:
- `Flags: 0x018 (PSH, ACK)`
- `.... ...1 .... = Acknowledgment: Set`
- `.... .... 1... = Push: Set`

<img width="1117" height="1080" alt="2_image" src="https://github.com/user-attachments/assets/829ec973-f546-47fb-aaa8-8f5463feab98" />




## Скриншот 3: UDP (DNS-запрос)

**Фильтр:** `udp`

Этот пакет показывает UDP-трафик — DNS-запрос к домену `aplus.qwen.ai`. UDP не использует флаги SYN/ACK, так как это протокол без установления соединения.

В поле User Datagram Protocol видно:
- `Source Port: 65429`
- `Destination Port: 53` (стандартный порт DNS)
- `Length: 39`
- `Checksum: 0x88a7`

<img width="1120" height="1080" alt="3_image" src="https://github.com/user-attachments/assets/c15e79c4-ed17-47ef-b8b2-3c27436f2a63" />


## Вывод

- **TCP** — надёжный протокол с установлением соединения, использует флаги (SYN, ACK, PSH, FIN, RST)
- **UDP** — быстрый протокол без установления соединения, не использует флаги, подходит для DNS, видео-стриминга, онлайн-игр
