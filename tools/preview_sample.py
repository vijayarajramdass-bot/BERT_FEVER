"""Print two annotated training examples from the upstream sample file."""

import csv
from itertools import takewhile
from pathlib import Path
import textwrap


def main():
    sample_file = Path(__file__).resolve().parents[1] / "data_samples.txt"
    section = "train_sentences_pos.tsv"
    lines = sample_file.read_text(encoding="utf-8").splitlines()
    header = lines.index(section + ":") + 1
    while not lines[header].strip():
        header += 1
    table = takewhile(str.strip, lines[header:])
    examples = {row["index"]: row for row in csv.DictReader(table, delimiter="\t")}

    print("BERT_FEVER | Dataset annotations")
    print("Source  {} / {}".format(sample_file.name, section))
    print("Labels  Ground-truth claim labels from the sample file")
    for index in ("1_0", "3_0"):
        row = examples[index]
        print()
        print("Row {}  |  {}".format(index, row["label"]))
        print("Claim     " + row["claim"])
        evidence = " ".join(row["evidence"].split())
        print(textwrap.fill(evidence, width=68, initial_indent="Evidence  ",
                            subsequent_indent=" " * 10))


if __name__ == "__main__":
    main()
