# test_data_gen.py
import struct
import random
import time

def generate_and_save(
    num_records=1_000_000,
    num_symbols=10,
    filename="test_ticks.bin"
):
    print(f"Generating {num_records:,} records with {num_symbols} symbols...")
    
    start = time.time()
    
    records = []
    base_timestamp = int(time.time() * 1_000_000)
    symbol_weights = [1.0 / (i + 1) for i in range(num_symbols)]
    total = sum(symbol_weights)
    symbol_weights = [w / total for w in symbol_weights]
    
    for i in range(num_records):
        timestamp = base_timestamp + i * 100
        symbol_id = random.choices(range(num_symbols), weights=symbol_weights)[0]
        price = 100.0 + symbol_id * 10.0 + random.gauss(0, 1.0)
        volume = random.randint(100, 10000)
        records.append((timestamp, symbol_id, price, volume))
    
    num_shuffled = int(num_records * 0.10)
    for _ in range(num_shuffled):
        idx = random.randint(0, num_records - 1)
        swap_idx = random.randint(max(0, idx - 100), min(num_records - 1, idx + 100))
        records[idx], records[swap_idx] = records[swap_idx], records[idx]
    
    with open(filename, "wb") as f:
        for rec in records:
            f.write(struct.pack("=QIdI", *rec))
    
    elapsed = time.time() - start

    # The 24 here is depedent on the size of the QIdI from earlier, bare that in mind
    
    file_size_mb = len(records) * 24 / (1024 * 1024)
    
    print(f"✓ Generated in {elapsed:.2f}s")
    print(f"✓ File size: {file_size_mb:.2f} MB")
    print(f"✓ Saved to {filename}")
    
    return filename

if __name__ == "__main__":
    for size in [1_000, 10_000, 100_000, 1_000_000]:
        generate_and_save(size, filename=f"test_ticks_{size}.bin")