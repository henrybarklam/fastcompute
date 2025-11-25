from dataclasses import dataclass
import struct 


import timeit


@dataclass
class TickData: 
    timestamp: int
    symbol_id: int
    price: float
    volume: int

class DataParser:
    @staticmethod
    def parse_ticks(filename: str) -> list[TickData]:
        parsed_data = []
        try: 
            with open(filename, 'rb') as file:
                file_content = file.read()
                file_size = len(file_content)
                if file_size % 24 != 0:
                    raise ValueError
                for chunk in range(0, file_size, 24):

                    # Impossible to know if there are any corruptions in the middle of the file, have to assume there aren't
                    current_tick_data = file_content[chunk:chunk+24]
                    try:
                        tick_data = struct.unpack('=QIdI', current_tick_data)
                        parsed_data.append(
                            TickData(
                                timestamp=tick_data[0],
                                symbol_id=tick_data[1],
                                price=tick_data[2],
                                volume=tick_data[3]
                            )
                        )

                    except Exception as e:
                        print(f"Exception {e}, file read error")
                        return parsed_data

                return parsed_data

        except FileNotFoundError as e:
            print("File not found")
            return parsed_data


if __name__=="__main__":
    data_parser = DataParser()
    tick_numbers = ['1000', '10000', '100000', '1000000']
    for tick_number in tick_numbers:
        execution_time = timeit.timeit(lambda: data_parser.parse_ticks(f'test_ticks_{tick_number}.bin'),number=10)
        print(f"Execution time: {execution_time} seconds for {tick_number} run")
        print(f"Time per tick: {int(1_000_000_000*execution_time/int(tick_number))}ns")
        print(f"Ops per second: {int(int(tick_number)/execution_time)}")


