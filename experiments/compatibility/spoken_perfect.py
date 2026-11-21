"""Replay the development evidence in spoken-perfect-development.md (no weekday results)."""

import argparse
from collections import Counter
from html import unescape
from pathlib import Path
import re
import wave
from zipfile import ZipFile

import numpy as np


SAMPLER = "KBA KCL KBP KD1 KCM KBT KCX KCS KBU KBM KCJ KCR".split()
WEEKDAY = re.compile(r"\b(?:mon|tues|wednes|thurs|fri|satur|sun)days?\b", re.I)
YESTERDAY = re.compile(r"\byesterday\b", re.I)
AUX = re.compile(r"\b(?:has|have)\b|['’](?:ve|s)\b", re.I)
# Unit, grid division, word just before and just after the selected 'yesterday'.
CASES = (
    ("KBD/6028", "064205_KBD_17", "{GAP_ANONYMIZATION}", "ABOUT"),
    ("KBE/3003", "009204_KBE_14", "IT", "HIS"),
    ("KCM/137", "053203_KCM_2", "ME", "I"),
    ("KCC/480", "053603_KCC_2", "PHONED", "WE"),
    ("KCW/1441", "052807_KCW_7", "CLOSED", "MM"),
    ("KCS/2556", "063004_KCS_15", "ER", "MORNING"),
    ("KCJ/175", "075201_KCJ_1", "THOUGH", "WHEN"),
    ("KBT/321", "060304_KBT_4", "ON", "THEY'VE"),
    ("KBH/205", "003902_KBH_2", "ANY", "DID"),
)


def sentence_units(path):
    """Official sampler HTML numbers multiple sentence units within each speaker row."""
    html = path.read_text(encoding="latin1")
    seen = set()
    for row in re.findall(r"<tr\b[^>]*>.*?</tr>", html, re.I | re.S):
        cells = re.findall(r"<td\b[^>]*>(.*?)</td>", row, re.I | re.S)
        if len(cells) != 2:
            continue
        speech = unescape(re.sub(r"<[^>]+>", " ", cells[1]))
        for match in re.finditer(r"\[(\d+)\](.*?)(?=\[\d+\]|\Z)", speech, re.S):
            number = int(match[1])
            if number in seen:
                raise ValueError(f"Duplicate sentence number {number} in {path}")
            seen.add(number)
            yield number, " ".join(match[2].split())
    if not seen or len(seen) != max(seen) or min(seen) != 1:
        raise ValueError(f"Incomplete sentence numbering in {path}")


def screen(directory):
    totals = Counter()
    hits = []
    for doc in SAMPLER:
        for number, sentence in sentence_units(directory / f"{doc}.html"):
            totals["all"] += 1
            if WEEKDAY.search(sentence) or not YESTERDAY.search(sentence):
                continue
            totals["yesterday"] += 1
            if AUX.search(sentence):
                hits.append(f"{doc}/{number}")
    print(f"{len(SAMPLER)} conversation files, {totals['all']} numbered units, "
          f"{totals['yesterday']} development units with yesterday, {len(hits)} candidates.")
    print("Candidate IDs:", " ".join(hits))
    assert (totals["yesterday"], len(hits)) == (88, 24)
    assert {"KCS/2556", "KCJ/175", "KBT/321", "KCM/137"}.issubset(hits)


def lexical_intervals(content):
    lines = content.decode("latin1").splitlines()
    tier = lines.index('"word"')
    first = tier + 4
    count = int(lines[tier + 3])
    words = []
    for i in range(first, first + 3 * count, 3):
        word = lines[i + 2].strip('"').upper()
        if word not in ("", "SP", "SIL"):
            words.append((word, float(lines[i]), float(lines[i + 1])))
    return words


def check_internal_position(archive, members):
    """Look for the declared auxiliary–yesterday order, skipping weekday windows."""
    grids = [name for name in members if name.endswith(".TextGrid")]
    inspected_dates = 0
    candidate_ids = []
    for name in grids:
        content = archive.read(name)
        if b'"word"' not in content:
            raise ValueError(f"Missing word tier in {name}")
        if b'"YESTERDAY"' not in content.upper():
            continue
        words = lexical_intervals(content)
        for i, (word, start, _) in enumerate(words):
            if word != "YESTERDAY":
                continue
            context = words[max(0, i - 12):i + 13]
            if any(WEEKDAY.search(token) for token, _, _ in context):
                continue
            inspected_dates += 1
            j = i - 1
            if j >= 0 and words[j][0] in ("JUST", "ONLY"):
                j -= 1
            if j < 0:
                continue
            before_date = words[j][0].replace("’", "'")
            if before_date in ("HAS", "HAVE") or before_date.endswith(("'S", "'VE")):
                division = Path(name).stem.split("_", 1)[1]
                candidate_ids.append(f"{division} at {start:.3f} s")
    print(f"Internal-position search: {len(grids)} grids, {inspected_dates} "
          f"development dates, {len(candidate_ids)} candidate sequences.")
    print("\n".join(candidate_ids))


def locate_date(words, previous, following):
    return [(left, date, right) for left, date, right in zip(words, words[1:], words[2:])
            if (left[0], date[0], right[0]) == (previous, "YESTERDAY", following)]


def check_grids(path):
    with ZipFile(path) as archive:
        members = archive.namelist()
        for unit, division, previous, following in CASES:
            member, = [m for m in members if m.endswith(f"_{division}.TextGrid")]
            words = lexical_intervals(archive.read(member))
            triple, = locate_date(words, previous, following)
            left, date, right = triple
            print(f"{unit:9} {division:15} {date[1]:9.3f}–{date[2]:.3f} s; "
                  f"gap before {date[1] - left[2]:.3f} s, after {right[1] - date[2]:.3f} s")
            if unit == "KCS/2556":
                index = words.index(date)
                obj, prep, hesitation = words[index - 3:index]
                assert (obj[0], prep[0], hesitation[0]) == ("ANTIBIOTICS", "ON", "ER")
                print(f"  Gap before the possible time phrase (object to on): "
                      f"{prep[1] - obj[2]:.3f} s")
        # Two published examples with no timing result. Do not impute a zero gap.
        kb9 = [m for m in members if "_KB9_" in m]
        assert len(kb9) == 41
        for member in kb9:
            words = lexical_intervals(archive.read(member))
            assert not any(a[0] == "PHONE" and b[0] == "YESTERDAY" for a, b in zip(words, words[1:]))
        assert not any("_KPV_" in m for m in members)
        print("No phone–yesterday adjacency in the KB9 grids; KPV has no grid in this release.")
        check_internal_position(archive, members)


def check_signal(path, clip_start):
    """10-ms RMS blocks. Time zero is the start of the official tape or supplied PCM excerpt."""
    with wave.open(str(path)) as recording:
        rate = recording.getframerate()
        if (recording.getnchannels(), recording.getsampwidth(), rate) != (1, 2, 16000):
            raise ValueError("Expected Oxford's mono 16-bit, 16-kHz PCM")
        for label, start, end in (("on + hesitation", 1436.7125, 1437.2425),
                                  ("intervening interval", 1437.2425, 1439.4925),
                                  ("date phrase", 1439.4925, 1440.2725)):
            recording.setpos(round((start - clip_start) * rate))
            frames = round((end - start) * rate)
            data = np.frombuffer(recording.readframes(frames), dtype="<i2").astype(float) / 32768
            if len(data) != frames:
                raise ValueError("The supplied recording ends before the specified interval")
            blocks = data[:frames // 160 * 160].reshape(-1, 160)
            rms = np.sqrt(np.mean(blocks ** 2, axis=1))
            print(f"{label}: median {20 * np.log10(np.median(rms)):.1f} dBFS")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sampler", type=Path, help="directory with the 12 Oxford transcript files")
    parser.add_argument("grids", type=Path, help="UK Data Service AudioBNCTextGrids.zip")
    parser.add_argument("--kcs-wav", type=Path, help="Oxford tape 0630 side B, or an excerpt")
    parser.add_argument("--clip-start", type=float, default=0, help="tape time of excerpt start, in seconds")
    args = parser.parse_args()
    screen(args.sampler)
    check_grids(args.grids)
    if args.kcs_wav:
        check_signal(args.kcs_wav, args.clip_start)
