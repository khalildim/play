from tqdm import tqdm

# get the only the deutsch words
with open("data/de_50k.txt", encoding="utf-8") as f:
    lines = f.readlines()[:2000]
    data = ""
    for line in tqdm(lines):
        mod_line = line[:line.find(" ")]
        data += f"{mod_line}\n"
    # print(data)
    f.close()

    # save the word in the file
    with open("data/50k_deutsch.txt", "w", encoding="utf-8") as d:
        d.write(data)



