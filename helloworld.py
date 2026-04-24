original_data = "AAABBBCCAA"


def compress(data):
    compressed = []
    count = 1
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            count += 1
        else:
            compressed.append(f"{data[i]}{count}")
            count = 1
    compressed.append(f"{data[-1]}{count}")
    return "".join(compressed)


compressed_data = compress(original_data)
print(compressed_data)
