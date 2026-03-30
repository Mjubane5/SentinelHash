# 🛡️ SentinelHash: Cloud-Ready File Integrity Monitor (FIM)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![AWS](https://img.shields.io/badge/AWS-EC2_Tested-orange.svg)
![Security](https://img.shields.io/badge/Security-Cryptography-success.svg)

## 📌 Overview
**SentinelHash** is a lightweight, high-performance File Integrity Monitor (FIM) built in Python. It utilizes cryptographic hashing algorithms to establish a baseline fingerprint of sensitive files and continuously monitors for unauthorized modifications, data corruption, or malicious injections.

This project was built and tested on an **AWS EC2 Linux environment**, demonstrating practical application in cloud infrastructure security.

## 🧠 The Cryptographic Logic
At its core, SentinelHash relies on the **SHA-256 (Secure Hash Algorithm 256-bit)** one-way function. 
* It reads the target file in binary chunks (to efficiently handle large files without consuming massive RAM).
* It computes a deterministic, 64-character hexadecimal fingerprint.
* Because SHA-256 possesses the "avalanche effect," altering even a single byte of data in the file completely changes the resulting hash, instantly triggering a critical alert.

## 🚀 Key Features
* **Zero-Dependency Architecture:** Uses only built-in Python libraries (`hashlib`, `os`, `time`), meaning it can be dropped into any native Linux/Unix cloud server without complex installations.
* **Continuous Monitoring:** Implements an efficient `while` loop with sleep intervals to minimize CPU overhead while providing near real-time intrusion detection.
* **Cloud-Native Deployment:** Designed to run headlessly on virtualized cloud nodes (e.g., AWS EC2, Azure VMs).

