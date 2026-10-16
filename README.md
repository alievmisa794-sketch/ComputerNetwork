# Краткий конспект: DHCP, DNS, NAT, TCP/UDP

## DHCP

Dynamic Host Configuration Protocol выдаёт клиенту IPv4-адрес, маску, default gateway, DNS-серверы и срок аренды. Типичный обмен DORA: **Discover → Offer → Request → Acknowledge**. Сервер UDP/67, клиент UDP/68; передачи через маршрутизатор обычно требуют DHCP Relay (`ip helper-address`).

Пример на Cisco для одной LAN:

```text
ip dhcp excluded-address 192.168.10.1 192.168.10.19
ip dhcp pool LAN10
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 1.1.1.1
```

## DNS

Domain Name System разрешает доменные имена в записи A (IPv4), AAAA (IPv6) и другие (CNAME, MX, NS, TXT), используя иерархию корневых, TLD и авторитативных серверов; резолверы могут кэшировать ответы по TTL. Обычно UDP/53, при необходимости TCP/53. Для проверки: `nslookup example.org` или `dig example.org A`.

## NAT

NAT изменяет адреса в IP-пакетах при проходе через границу сетей. **Static NAT** — фиксированное 1:1 соответствие; **Dynamic NAT** — выделение адреса из пула; **PAT/NAT overload** — многие внутренние клиенты используют один внешний адрес с различными портами.

Пример фрагмента конфигурации Cisco с условными интерфейсами:

```text
interface GigabitEthernet0/0
 ip nat inside
interface GigabitEthernet0/1
 ip nat outside
access-list 1 permit 192.168.10.0 0.0.0.255
ip nat inside source list 1 interface GigabitEthernet0/1 overload
```

Для рабочего NAT необходимы правильные IP-адреса интерфейсов, маршрутизация до провайдера и обратная связность.

## TCP и UDP

- **TCP:** ориентирован на соединение, предоставляет подтверждение доставки, управление потоком и перегрузкой, упорядоченную доставку потока байтов; флаги SYN/ACK/PSH/FIN/RST.
- **UDP:** передаёт дейтаграммы без установления соединения и гарантий доставки/порядка на уровне протокола. DNS, DHCP и множество аудио/видео протоколов используют UDP.

Материалы — краткие ответы на темы презентаций из архива, а не запись живого эксперимента.
