This project explores the security differences between insecure UDP communication and secure DTLS communication. It demonstrates how plaintext UDP traffic can be easily spoofed, intercepted, or replayed, and then shows how DTLS protects the same communication channel using encryption, certificate-based authentication, integrity checks, and anti-replay mechanisms.

The project is divided into multiple modules:

1. UDP Insecure Communication

A basic UDP client and server were implemented using Python. Because UDP provides no encryption or authentication, all messages appear in plaintext in Wireshark, and the server blindly accepts any data from any source.

2. UDP Spoofing & Replay Attacks

Using tools like hping3 and tcpreplay, spoofed packets and replayed packets were sent to the UDP server. Since UDP has no sequencing or validation, the server accepted all malicious packets, proving how vulnerable UDP is to injection and replay attacks.

3. TCP + TLS Secure Communication

TLS was added to standard TCP communication, demonstrating how encryption and certificate validation protect data. Wireshark shows the TLS handshake and encrypted “Application Data,” proving that plaintext is fully protected.

4. DTLS Secure Communication

DTLS was used to secure UDP traffic. The DTLS handshake, certificate exchange, and encrypted application packets were captured in Wireshark. This module shows how DTLS brings TLS-grade security to datagram networks.

5. DTLS Anti-Replay Protection

Replaying previously captured DTLS packets failed completely. DTLS rejected these packets using sequence numbers, epochs, and a sliding replay window. This proved that DTLS prevents replay attacks, unlike normal UDP.

6. ICMP Tunneling Detection

ICMP packets were analyzed to detect suspicious oversized payloads—an indicator of covert data exfiltration. This module demonstrates how attackers bypass secure channels by using non-encrypted protocols like ICMP.

Overall, the project demonstrates practical differences between insecure and secure transport-layer protocols, supported by real packet captures, Python scripts, OpenSSL-based DTLS setup, and replay/spoofing attack simulations.
