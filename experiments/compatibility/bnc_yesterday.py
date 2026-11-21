"""Replay the development-only BNC Baby screen. See english-perfect-contrast.md."""

import argparse
from collections import Counter
from pathlib import Path
import xml.etree.ElementTree as ET


WEEKDAYS = set("monday tuesday wednesday thursday friday saturday sunday".split())

# Retained on the masked pass. See the note for exclusions and ambiguous tense tags.
RETAINED = set("""
KB5/122 KB7/15060 KBD/2659 KBW/16832 KCC/49 KCC/328
KD1/754 KD3/619 KD3/3473 KD7/2031 KD8/3264 KD8/7331
KE4/770 KP2/83 KP5/59 KP5/726 KP5/1218 KP5/1666 KPX/314 KPX/369
""".split())


def screen(directory, view):
    totals = Counter()
    reviewed = set()
    files = sorted(directory.glob("*.xml"))
    if not files:
        raise ValueError(f"No conversational XML files in {directory}")
    for path in files:
        root = ET.parse(path).getroot()
        for div in root.findall(".//stext//div"):
            # A new conversation starts a new context. Skip nested divisions
            # here since we process each division's own utterances below.
            previous = []
            for utterance in div.findall("u"):
                for sentence in utterance.iter("s"):
                    words = list(sentence.iter("w"))
                    tokens = [" ".join(w.itertext()).strip().lower() for w in words]
                    line = " ".join(tokens)
                    day_in_line = bool(WEEKDAYS.intersection(tokens))
                    totals["units"] += 1
                    if "yesterday" in tokens and not day_in_line:
                        totals["yesterday units without weekday"] += 1
                        pairs = [(i, j) for j, word in enumerate(tokens) if word == "yesterday"
                                 for i in range(max(0, j - 10), j) if tokens[i] == "i"]
                        if pairs:
                            # Count each unit once. Take the nearest I to the
                            # first qualifying yesterday for the display.
                            i, j = min(pairs, key=lambda pair: (pair[1], -pair[0]))
                            totals["candidate units"] += 1
                            start = i + 1
                            verb = start
                            if tokens[start] in ("'ve", "’ve", "have"):
                                verb += 1
                            simple = verb < j and words[verb].get("c5", "").startswith("VV")
                            key = f"{path.stem}/{sentence.get('n')}"
                            if simple:
                                totals["direct lexical verb"] += 1
                                marker = "[" + words[verb].get("hw", "?") + "]"
                                masked = tokens[:start] + [marker] + tokens[verb + 1:]
                                if key in RETAINED:
                                    assert key not in reviewed
                                    reviewed.add(key)
                                    if verb != start:
                                        totals["retained with overt HAVE"] += 1
                                    else:
                                        totals["retained without HAVE, " + words[verb].get("c5", "?")] += 1
                                if view == "masked":
                                    print(key, "|", " / ".join(previous[-2:]), "|", " ".join(masked))
                            elif view == "masked":
                                # Keep unparsed cases visible without revealing their form.
                                print(key, "|", " / ".join(previous[-2:]), "|",
                                      " ".join(tokens[:start] + ["[span]"] + tokens[j:]))
                            if view == "forms":
                                print(key, "|", " ".join(tokens[i:j+1]), "|",
                                      " ".join(w.get("c5", "?") for w in words[i:j+1]))
                    previous = [*previous[-1:], "[weekday omitted]" if day_in_line else line]
    if reviewed != RETAINED:
        raise ValueError(f"Reviewed IDs missing from input: {sorted(RETAINED - reviewed)}")
    totals["retained with overt HAVE"] += 0
    print(f"{len(files)} texts | " + " | ".join(f"{k}: {n}" for k, n in totals.items()))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="BNC Baby conversation/Texts/dem directory")
    parser.add_argument("--view", choices=["summary", "masked", "forms"], default="summary")
    args = parser.parse_args()
    screen(args.directory, args.view)
