import sys


def binlst2int(bin_lst: list) -> int:
    ans = 0
    for i in range(len(bin_lst)):
        ans = ans * 2 + bin_lst[i]
    return ans


def mkrom():
    header = "v3.0 hex words plain\n"

    if len(sys.argv) != 4:
        print("usage: mkrom <addr_width> <data_width> <rule_path>")
        return

    addr_width = int(sys.argv[1])
    data_width = int(sys.argv[2])
    rule_path = sys.argv[3]

    if addr_width > 20:
        print("addr_width too large!")
        return

    blank = "".join(["0" for _ in range((data_width + 3) // 4)])

    rom_data = [blank for _ in range(1 << addr_width)]

    rule_fd = open(rule_path)
    rule = rule_fd.readlines()
    rule_fd.close()

    for line in rule:
        # 1. ignore annotations
        anno_idx = line.find("#")
        if anno_idx != -1:
            line = line[:anno_idx]

        # 2. extract address and data -> entry[0], entry[1]
        entry = line.split()
        addr = [
            ord(ch) - 48 for ch in entry[0] if ch != "-"
        ]  # convert to a binary list (each element is an **integer**)
        data = "".join([ch for ch in entry[1] if ch != "-"])  # convert data to hex

        if len(addr) != addr_width or len(data) != data_width:
            print(f"Invalid entry: {addr} {data}")
            print("Aborted.")
            return

        data = hex(int(data, 2))[2:]

        # padding
        padding_num = (data_width + 3) // 4 - len(data)
        data = "".join(["0"] * padding_num) + data

        # 3. enumerate every possible address and set data
        x_idx = []
        for i in range(len(addr)):
            if addr[i] == ord("x") - 48 or addr[i] == ord("X") - 48:
                x_idx.append(i)

        for i in range(1 << len(x_idx)):
            for j in range(len(x_idx)):
                addr[x_idx[j]] = i >> j & 1
            rom_data[binlst2int(addr)] = data

        if len(x_idx) == 0:
            rom_data[binlst2int(addr)] = data

    res_fd = open("rom.txt", "w")
    res_fd.write(header)
    for i in range(len(rom_data)):
        res_fd.write(rom_data[i])
        if i % 8 == 7:
            res_fd.write("\n")
        else:
            res_fd.write(" ")
    res_fd.close()


if __name__ == "__main__":
    mkrom()
