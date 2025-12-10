# fastcompute

A performance-focused exploration of high-frequency financial data processing. Building foundational skills in systems programming through practical binary parsing and optimization.

## Overview

This repository is part of a 3-month intensive learning journey focused on core systems programming competencies:

- **Performance-aware programming** - understanding hardware constraints
- **Systems design** - building production-grade, scalable infrastructure
- **Optimization** - squeezing performance from modern hardware
- **Data structure mastery** - memory layouts and cache efficiency

This project builds these foundational skills through real code, real benchmarks, and documented learning.

## Project Goals

1. **Learn binary protocol parsing** - a common task in high-frequency systems
2. **Profile and optimize iteratively** - measure where time is actually spent
3. **Build production-quality code** - proper error handling, testing, documentation
4. **Document the learning process** - teaching others by sharing discoveries

## Current Progress

### Version 1: Baseline Implementation
- **Status**: Completed
- **Approach**: Straightforward binary parser using Python's `struct` module
- **Performance**: 5-7.5 microseconds per tick (5,000-7,500 ns)
- **Throughput**: 130-190k ticks/second
- **Target Gap**: ~5-7x slower than ideal for high-frequency systems

**Key Learnings**:
- File I/O dominance - reading from disk is millions of times slower than memory access
- Importance of reading files entirely into memory first
- Binary format parsing requires understanding struct packing and alignment
- Need for systematic profiling to identify bottlenecks

### Version 2: Profiling & Analysis
- **Status**: Completed
- **Focus**: Identifying where time is actually spent
- **Bottleneck Analysis**:
  - `struct.unpack()` - 10% of runtime
  - Object creation (`TickData.__init__`) - 8% of runtime
  - List append operations - 8% of runtime
  - Remaining time in I/O and iteration

**Key Learnings**:
- Python's dynamic object creation has measurable cost at scale
- List resizing is expensive when size unknown ahead of time
- Need to explore language alternatives or deeper optimizations

## Project Structure

```
fastcompute/
├── Version1/                    # Initial naive implementation
│   ├── naive_binary_parser.py  # Baseline parser
│   ├── test_data_generator.py  # Generate test data
│   ├── learning-notes.txt      # Design decisions and learnings
│   └── README.md
│
├── Version2/                    # Profiling and optimization
│   ├── naive_binary_parser.py  # Optimized parser
│   ├── profile_parser.py       # Profiling harness
│   ├── learning-notes.txt      # Performance analysis
│   └── README.md
│
├── test_data/                   # Shared test data
│   └── test_data_generator.py  # Test fixture generation
│
└── README.md                    # This file
```

## The Data Format

The project parses financial market tick data in binary format:

```
Record Format (24 bytes per record):
- timestamp: uint64 (8 bytes)    - millisecond timestamp
- symbol_id: uint32 (4 bytes)    - which financial instrument
- price: double (8 bytes)         - quoted price
- volume: uint32 (4 bytes)        - quantity traded
```

**Why this format?**
- Common in real financial systems (similar to ITCH, FIX protocols)
- Forces engagement with binary serialization challenges
- Allows benchmarking against real-world performance targets

## Running the Code

### Generate Test Data

```bash
python test_data/test_data_generator.py
```

Generates binary files with 1k, 10k, 100k, and 1M tick records.

### Run Version 1 (Baseline)

```bash
cd Version1
python naive_binary_parser.py
```

Output:
```
Execution time: X seconds for 1000 run
Time per tick: 5000ns
Ops per second: 200000
```

### Run Version 2 (With Profiling)

```bash
cd Version2
python profile_parser.py
```

Generates profiling output showing time spent in each function.

## Performance Targets

The goal is to achieve sub-microsecond parsing:

| Metric | Current | Target |
|--------|---------|--------|
| Time per tick | 5-7.5 μs | 500-1000 ns |
| Throughput | 130-190k ops/s | 1-2M ops/s |
| Gap | — | 5-7x improvement needed |

## Next Steps

Potential optimizations to explore:

1. **Compiled alternatives** - C/Rust implementations
2. **Memory pre-allocation** - pre-size collections to avoid resizing
3. **Batch processing** - amortize overhead across multiple records
4. **Lower-level languages** - where hardware-aware optimization is easier
5. **Algorithmic improvements** - avoid creating intermediate objects

## Learning Journey Context

This project is **Week 1-2** of a structured 3-month curriculum:

**Month 1: Foundations** (Weeks 1-4)
- Performance-aware programming & CPU architecture
- Memory hierarchies and cache optimization
- Data structures at scale
- Proper benchmarking (this project)

**Month 2: Concurrency & Systems** (Weeks 5-8)
- Multi-threading and lock-free programming
- Distributed systems design
- Advanced optimization techniques

**Month 3: Production Systems** (Weeks 9-12)
- Capstone project integration
- Production observability and monitoring
- System design documentation

## Resources

**Books & References**:
- Computer Systems: A Programmer's Perspective (Bryant & O'Hallaron)
- Fluent Python (Ramalho)
- C++ Concurrency in Action (Williams)
- Designing Data-Intensive Applications (Kleppmann)
- Performance-Aware Programming (Muratori)

**Why These Skills Matter**:
- Performance optimization applies to any system with high throughput requirements
- Systems design principles are foundational across all engineering domains
- Understanding hardware constraints is essential for building efficient systems

## Technical Notes

### Binary Format Considerations

Real financial systems typically use:
- **Fixed-point integers** - store prices as cents/basis points to avoid floating-point precision issues
- **Decimal types** - for arbitrary precision
- **64-bit floats** - used sometimes, but have precision limitations

This project uses 64-bit floats for learning purposes, but the precision trade-off is worth understanding.

### File I/O Performance

Key insight: **File I/O is 10 million times slower than memory access**

- RAM access: ~1 nanosecond
- Disk access: ~10,000,000 nanoseconds (requires syscall, disk seek, copy)

This is why reading the entire file once, then parsing in memory, dramatically outperforms streaming approaches.

## Documentation

All work is thoroughly documented:
- **GitHub**: Public commits and clear code
- **Blog posts**: Technical deep-dives and learnings (coming weekly)
- **Performance benchmarks**: Real measurements from real code
- **Learning notes**: What worked, what didn't, why

This documentation approach provides accountability and enables peer learning.

---

**Status**: Active learning project
**Last Updated**: December 2025
**Next Milestone**: Version 3 - Compiled language optimization
