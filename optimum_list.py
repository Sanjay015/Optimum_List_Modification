"""Optimumm way to do List operations."""
DICT_MAP = {}
config = raw_input().split()

for operation in range(int(config[0])):
    input_data = map(int, raw_input().split())
    for data_index in range(input_data[0], input_data[1]):
        if data_index not in DICT_MAP:
            DICT_MAP[data_index] = input_data[2]
        else:
            DICT_MAP[data_index] = DICT_MAP[data_index] + input_data[2]
print max(DICT_MAP.values())
