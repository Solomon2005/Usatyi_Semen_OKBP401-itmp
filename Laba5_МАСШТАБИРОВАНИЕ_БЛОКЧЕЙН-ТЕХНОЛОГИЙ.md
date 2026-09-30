# Отчёт по 5 Лабораторной работе
## Практическая часть
```python
import hashlib
import random
```
### Задание 1
```python
def calculate_network_throughput():
    print("=====================")
    print("Задание 1")
    networks = {
        "Ethereum": 30,
        "Binance Smart Chain": 160,
        "Solana": 50000
    }

    for name, tps in networks.items():
        hourly_transactions = tps * 3600
        print(f"{name}: {hourly_transactions:,} транзакций/час")

    leader = max(networks, key=networks.get)
    print(f"Лидер: {leader}")
    print("=====================")


calculate_network_throughput()
```
```terminaloutput
Ethereum: 108,000 транзакций/час
Binance Smart Chain: 576,000 транзакций/час
Solana: 180,000,000 транзакций/час
Лидер: Solana
```

### Задание 2
```python
def calculate_read_write_ratio(write_operations):
    min_reads = write_operations * 100
    max_reads = write_operations * 10000
    return min_reads, max_reads


writes_per_second = 500
min_r, max_r = calculate_read_write_ratio(writes_per_second)

print("Задание 2")
print(f"Записей в секунду: {writes_per_second}")
print(f"Минимум чтений/с: {min_r:,}")
print(f"Максимум чтений/с: {max_r:,}")
print("=====================")
```
```terminaloutput
Записей в секунду: 500
Минимум чтений/с: 50,000
Максимум чтений/с: 5,000,000
```

### Задание 3
```python
class Block:
    def __init__(self, index, data, prev_hash):
        self.index = index
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        string_to_hash = str(self.index) + str(self.data) + str(self.prev_hash)
        return hashlib.sha256(string_to_hash.encode()).hexdigest()


chain = []
genesis_block = Block(index=0, data="Genesis Data", prev_hash="0")
chain.append(genesis_block)

block_1 = Block(index=1, data="First Transaction Data", prev_hash=chain[-1].hash)
chain.append(block_1)

block_2 = Block(index=2, data="Second Transaction Data", prev_hash=chain[-1].hash)
chain.append(block_2)

print("Задание 3")
for block in chain:
    print(f"Блок {block.index}: hash={block.hash[:16]}... prev={block.prev_hash[:16]}...")
print("=====================")
```
```terminaloutput
Блок 0: hash=8df0119e5af4f5e0... prev=0...
Блок 1: hash=19c968f9b9ff1b31... prev=8df0119e5af4f5e0...
Блок 2: hash=c108257088b907be... prev=19c968f9b9ff1b31...
```

### Задание 4
```python
def get_sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()


target_string = "blockchain"
result_hash = get_sha256_hash(target_string)

print("Задание 4")
print(f"SHA-256('{target_string}') =")
print(result_hash)
print("=====================")
```
```terminaloutput
SHA-256('blockchain') =
ef7797e13d3a154a54332d3d012d4a514e88cbd5600f11c77f32957a4106e530
```

### Задание 5
```python
def mine_block(data, difficulty):
    prefix = "0" * difficulty
    nonce = 0

    while True:
        string_to_hash = data + str(nonce)
        current_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()

        if current_hash.startswith(prefix):
            return nonce, current_hash

        nonce += 1


block_data = "block1"
target_difficulty = 4
found_nonce, final_hash = mine_block(block_data, target_difficulty)

print("Задание 5")
print(f"difficulty={target_difficulty}, nonce={found_nonce}")
print(f"hash={final_hash}")
print("=====================")
```
```terminaloutput
difficulty=4, nonce=67781
hash=0000bf7983693fb1d06371cb240fae41da928236da4cfb8bc27e2469d718b532
```

### Задание 6
```python
def calculate_merkle_root(tx_list):
    current_level = [hashlib.sha256(tx.encode()).hexdigest() for tx in tx_list]

    while len(current_level) > 1:
        next_level = []
        if len(current_level) % 2 != 0:
            current_level.append(current_level[-1])

        for i in range(0, len(current_level), 2):
            combined = current_level[i] + current_level[i + 1]
            parent_hash = hashlib.sha256(combined.encode()).hexdigest()
            next_level.append(parent_hash)
        current_level = next_level

    return current_level[0]


transactions = ["tx1", "tx2", "tx3", "tx4"]
merkle_root = calculate_merkle_root(transactions)

print("Задание 6")
print(f"Merkle root: {merkle_root}")
print("=====================")
```
```terminaloutput
Merkle root: d127453df8a9a4b375b42d54e58f000b213b2c9dfdf5cf9667793d596ec961c0
```

### Задание 7
```python
def check_51_attack_threat(p):
    if p > 0.5:
        return f"Доля мощности {p:.0%}: УГРОЗА (атака 51%)"
    else:
        return f"Доля мощности {p:.0%}: безопасно"


shares = [0.3, 0.51, 0.49, 0.6]

print("Задание 7")
for share in shares:
    print(check_51_attack_threat(share))
print("=====================")
```
```terminaloutput
Доля мощности 30%: безопасно
Доля мощности 51%: УГРОЗА (атака 51%)
Доля мощности 49%: безопасно
Доля мощности 60%: УГРОЗА (атака 51%)
```

### Задание 8
```python
random.seed(42)

print("Задание 8")
for i in range(6):
    if i in (0, 1):
        print(f"Транзакция {i} подтверждает: — (начальная)")
    else:
        references = sorted(random.sample(range(i), 2))
        print(f"Транзакция {i} подтверждает: {references}")
print("=====================")
```
```terminaloutput
Транзакция 0 подтверждает: — (начальная)
Транзакция 1 подтверждает: — (начальная)
Транзакция 2 подтверждает: [0, 1]
Транзакция 3 подтверждает: [0, 2]
Транзакция 4 подтверждает: [1, 2]
Транзакция 5 подтверждает: [1, 4]
```

### Задание 9
```python
def calculate_confirmation_time(n, k=1000):
    return k / n


tx_counts = [10, 100, 1000]

print("Задание 9")
for n in tx_counts:
    t = calculate_confirmation_time(n)
    print(f"n={n:>4} транзакций -> время подтверждения = {t:.2f} усл.ед.")
print("=====================")
```
```terminaloutput
n=  10 транзакций -> время подтверждения = 1000.00 усл.ед.
n= 100 транзакций -> время подтверждения = 100.00 усл.ед.
n=1000 транзакций -> время подтверждения = 1.00 усл.ед.
```

### Задание 10
```python
def get_address_index(transactions_list, addr):
    user_txs = [tx for tx in transactions_list if tx["from"] == addr or tx["to"] == addr]

    balance = 0
    for tx in user_txs:
        if tx["to"] == addr:
            balance += tx["amount"]
        if tx["from"] == addr:
            balance -= tx["amount"]

    return user_txs, balance


tx_history = [
    {"from": "Alice", "to": "Bob", "amount": 50},
    {"from": "Bob", "to": "Alice", "amount": 20},
    {"from": "Alice", "to": "Carol", "amount": 10}
]

target_user = "Alice"
found_txs, final_balance = get_address_index(tx_history, target_user)

print("Задание 10")
print(f"Транзакции {target_user} ({len(found_txs)}):")
for tx in found_txs:
    print(f"  {tx['from']} -> {tx['to']}: {tx['amount']}")
print(f"Баланс {target_user}: {final_balance}")
print("=====================")
```
```terminaloutput
Транзакции Alice (3):
  Alice -> Bob: 50
  Bob -> Alice: 20
  Alice -> Carol: 10
Баланс Alice: -40
```

### Задание 11
```python
def analyze_subgraph_stats(log):
    stats = {}
    for sg, cnt in log:
        stats[sg] = stats.get(sg, 0) + cnt

    most_loaded = max(stats, key=stats.get)
    total_requests = sum(stats.values())

    return stats, most_loaded, total_requests


query_log = [
    ("uniswap", 5000), ("aave", 8500), ("uniswap", 7500), ("compound", 4500)
]

subgraph_data, active_leader, grand_total = analyze_subgraph_stats(query_log)

print("Задание 11")
for subgraph, count in subgraph_data.items():
    print(f"{subgraph}: {count:,} запросов")
print(f"Самый нагруженный: {active_leader}")
print(f"Всего запросов: {grand_total:,}")
print("=====================")
```
```terminaloutput
uniswap: 12,500 запросов
aave: 8,500 запросов
compound: 4,500 запросов
Самый нагруженный: uniswap
Всего запросов: 25,500
```

### Задание 12
```python
def sign(message, private_key):
    return hashlib.sha256((message + private_key).encode()).hexdigest()


def verify(message, signature, private_key):
    return sign(message, private_key) == signature


msg = "Valid Blockchain Transaction"
fake_msg = "Hacked Blockchain Transaction"
secret_key = "my_secure_private_key"

sig = sign(msg, secret_key)

print("Задание 12")
print(f"Подпись: {sig[:24]} ...")
print(f"Проверка верной подписи: {verify(msg, sig, secret_key)}")
print(f"Проверка при подмене сообщения: {verify(fake_msg, sig, secret_key)}")
print("=====================")
```
```terminaloutput
Подпись: de858bd9e6231e34f71a0690 ...
Проверка верной подписи: True
Проверка при подмене сообщения: False
```

### Задание 13
```python
def compare_qubits(n):
    quantum_states = 2 ** n
    classical_states = n
    return quantum_states, classical_states


qubit_tests = [1, 2, 8, 127]

print("Задание 13")
for qubits in qubit_tests:
    q_states, c_states = compare_qubits(qubits)
    print(f"Кубитов: {qubits:<3} | Квантовых состояний: {q_states:,} | Классических: {c_states}")
print("=====================")
```
```terminaloutput
Кубитов: 1   | Квантовых состояний: 2 | Классических: 1
Кубитов: 2   | Квантовых состояний: 4 | Классических: 2
Кубитов: 8   | Квантовых состояний: 256 | Классических: 8
Кубитов: 127 | Квантовых состояний: 170,141,183,460,469,231,731,687,303,715,884,105,728 | Классических: 127
```

### Задание 14

```python
def factorize(n):
    factors = []
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    return factors


numbers_to_factor = [15, 21, 91]

print("Задание 14")
for num in numbers_to_factor:
    res_factors = factorize(num)
    print(f"{num} = {res_factors[0]} x {res_factors[1]}")
print("=====================")
```
```terminaloutput
15 = 3 x 5
21 = 3 x 7
91 = 7 x 13
```

### Задание 15

```python
def extrapolate_qubits(generations):
    rates = []
    for i in range(len(generations) - 1):
        rates.append(round(generations[i + 1] / generations[i], 2))

    avg_rate = sum(rates) / len(rates)
    forecast = round(generations[-1] * avg_rate)

    return rates, avg_rate, forecast


ibm_roadmap = [127, 433, 1121]
growth_rates, average_growth, next_generation = extrapolate_qubits(ibm_roadmap)

print("Задание 15")
print(f"Поколения кубитов: {ibm_roadmap}")
print(f"Коэффициенты роста: {growth_rates}")
print(f"Средний темп роста: x{average_growth:.2f}")
print(f"Прогноз следующего поколения: ~{next_generation} кубитов")
print("=====================")
```
```terminaloutput
Поколения кубитов: [127, 433, 1121]
Коэффициенты роста: [3.41, 2.59]
Средний темп роста: x3.00
Прогноз следующего поколения: ~3363 кубитов
```
